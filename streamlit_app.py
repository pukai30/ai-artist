
"""
Streamlit UI for AI Artist - Image Generation Prompt Builder
Interactive interface for creating and previewing image generation prompts
"""

import streamlit as st
import prompt_temp
import re
import time
from typing import List, Dict
from main import ImageGenerator
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Artist - Prompt Builder",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    /* Hide sidebar completely */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Hide sidebar toggle button */
    button[kind="header"] {
        display: none;
    }
    
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #3498db;
        padding-bottom: 0.5rem;
    }
    .preview-box {
        background-color: #f8f9fa;
        border-left: 4px solid #3498db;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .negative-preview-box {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #d1ecf1;
        border-left: 4px solid #17a2b8;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    .stButton>button {
        width: 100%;
        background-color: #3498db;
        color: white;
        font-size: 1.2rem;
        padding: 0.75rem;
        border-radius: 0.5rem;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    </style>
""", unsafe_allow_html=True)


def extract_placeholders(template: str) -> List[str]:
    """Extract placeholder names from a template string."""
    return re.findall(r'\{(\w+)\}', template)


def estimate_tokens(text: str) -> int:
    """
    Estimate token count for a text string.
    Uses a simple approximation: ~0.75 tokens per word (based on GPT tokenization).
    This is a rough estimate; actual token count may vary slightly.
    """
    if not text:
        return 0
    
    # Split by whitespace and punctuation for a rough word count
    words = text.split()
    # Approximate: 1 word ≈ 1.3 tokens on average for English text
    # Or inversely: 0.75 words per token
    estimated_tokens = int(len(words) * 1.3)
    
    return estimated_tokens


def get_template_categories() -> Dict[str, List[str]]:
    """Get all template categories and their templates."""
    categories = {
        "Portrait": prompt_temp.PORTRAIT_TEMPLATES,
        "Landscape": prompt_temp.LANDSCAPE_TEMPLATES,
        "Fantasy": prompt_temp.FANTASY_TEMPLATES,
        "Sci-Fi": prompt_temp.SCI_FI_TEMPLATES,
        "Animal": prompt_temp.ANIMAL_TEMPLATES,
        "Architecture": prompt_temp.ARCHITECTURE_TEMPLATES,
        "Abstract": prompt_temp.ABSTRACT_TEMPLATES,
        "Food": prompt_temp.FOOD_TEMPLATES,
        "Character": prompt_temp.CHARACTER_TEMPLATES,
        "Product": prompt_temp.PRODUCT_TEMPLATES,
    }
    return categories


def get_placeholder_suggestions(placeholder: str, category: str = None) -> List[str]:
    """Get context-aware suggestions based on template category and placeholder."""
    # First, check if there are category-specific options
    if category and category in prompt_temp.TEMPLATE_SPECIFIC_OPTIONS:
        category_options = prompt_temp.TEMPLATE_SPECIFIC_OPTIONS[category]
        if placeholder in category_options:
            return category_options[placeholder]
    
    # Check default field options
    if placeholder in prompt_temp.DEFAULT_FIELD_OPTIONS:
        return prompt_temp.DEFAULT_FIELD_OPTIONS[placeholder]
    
    # Fallback to generic suggestions (kept for compatibility)
    generic_suggestions = {
        "style": list(prompt_temp.STYLES.keys()),
        "lighting": prompt_temp.LIGHTING_OPTIONS,
        "quality": prompt_temp.QUALITY_MODIFIERS,
        "mood": ["peaceful", "dramatic", "mysterious", "joyful", "melancholic", "epic", "serene", "intense", "atmospheric", "ethereal"],
    }
    return generic_suggestions.get(placeholder, [])


# Main app
def main():
    # Header
    st.markdown('<div class="main-header">🎨 AI Artist - Prompt Builder</div>', unsafe_allow_html=True)
    
    # Initialize session state
    if 'generated_prompt' not in st.session_state:
        st.session_state.generated_prompt = None
    if 'generated_negative' not in st.session_state:
        st.session_state.generated_negative = None
    if 'generated_images' not in st.session_state:
        st.session_state.generated_images = []
    
    # Initialize model loading state
    if 'model_loading_started' not in st.session_state:
        st.session_state.model_loading_started = False
    if 'generator' not in st.session_state:
        st.session_state.generator = None
        st.session_state.model_loaded = False
    
    # AUTOMATIC MODEL LOADING AT STARTUP
    if not st.session_state.model_loaded and not st.session_state.model_loading_started:
        st.markdown('<div class="section-header">⚡ Loading AI Model...</div>', unsafe_allow_html=True)
        st.info("**Loading Stable Diffusion model. Please wait...**")
        st.markdown("This is a one-time step. First-time use will download ~4GB model (takes 2-5 minutes).")
        
        # Create progress placeholder
        progress_text = st.empty()
        progress_bar = st.progress(0)
        
        progress_text.text("Initializing model loading...")
        progress_bar.progress(10)
        
        # Mark as started to prevent re-triggering
        st.session_state.model_loading_started = True
        
        try:
            progress_text.text("Creating ImageGenerator...")
            progress_bar.progress(20)
            
            st.session_state.generator = ImageGenerator(device="cpu")
            
            progress_text.text("Loading Stable Diffusion pipeline (this may take several minutes)...")
            progress_bar.progress(30)
            
            # Load the model
            st.session_state.model_loaded = st.session_state.generator.load_model()
            
            if st.session_state.model_loaded:
                progress_text.text("Model loaded successfully!")
                progress_bar.progress(100)
                st.success("✅ Model loaded successfully!")
                st.balloons()
                # Don't rerun - just continue showing the interface
            else:
                progress_text.text("Failed to load model")
                progress_bar.progress(0)
                st.error("❌ Failed to load model. Check terminal for details.")
                st.warning("Refresh the page to try again, or check TROUBLESHOOTING_MODEL_LOAD.md")
                st.stop()
        except Exception as e:
            progress_text.text("Error during model loading")
            progress_bar.progress(0)
            st.error(f"❌ Error loading model: {str(e)}")
            st.info("💡 Check terminal for full error details")
            st.warning("Refresh the page to try again")
            st.stop()
    
    # Show if model is still loading
    if not st.session_state.model_loaded:
        st.info("⏳ Model is loading... Please wait. Check terminal for progress.")
        st.stop()
    
    # Model is loaded - show success banner
    st.success("✅ Model Ready - Start Creating AI Art!")
    st.markdown("---")
    
    # Main content area - ALL sections here, NO SIDEBAR
    
    # Template Selection Section
    st.markdown('<div class="section-header">🎯 Template Selection</div>', unsafe_allow_html=True)
    
    # Get template categories
    categories = get_template_categories()
    
    # Category and template selection in 2 columns
    temp_col1, temp_col2 = st.columns(2)
    
    with temp_col1:
        selected_category = st.selectbox(
            "Template Category",
            options=list(categories.keys()),
            help="Select the type of image you want to generate"
        )
    
    with temp_col2:
        templates = categories[selected_category]
        template_options = [f"Template {i+1}" for i in range(len(templates))]
        selected_template_idx = st.selectbox(
            "Select Template",
            options=range(len(templates)),
            format_func=lambda x: template_options[x],
            help="Select a specific template variation"
        )
    
    selected_template = templates[selected_template_idx]
    
    # Show selected template
    with st.expander("📝 View Selected Template"):
        st.code(selected_template, language="text")
        placeholders = extract_placeholders(selected_template)
        st.markdown(f"**Required fields:** {', '.join(placeholders)}")
    
    st.markdown("---")
    
    # What to Avoid Selection Section (formerly Negative Prompt)
    st.markdown('<div class="section-header">🚫 What to Avoid</div>', unsafe_allow_html=True)
    
    neg_col1, neg_col2 = st.columns([1, 2])
    
    with neg_col1:
        negative_prompt_options = list(prompt_temp.NEGATIVE_PROMPTS.keys())
        selected_negative_key = st.selectbox(
            "Quality Control Type",
            options=negative_prompt_options,
            format_func=lambda x: x.replace("_", " ").title(),
            help="Tell the AI what you *don't* want in your image. This helps exclude unwanted elements, artifacts, and quality issues. It significantly improves the final output by guiding the model away from common problems like blurriness, distortion, or anatomical errors. Think of it as quality control for your AI-generated images - the more specific you are about what to avoid, the better your results will be."
        )
        
        selected_negative = prompt_temp.NEGATIVE_PROMPTS[selected_negative_key]
    
    with neg_col2:
        # Show label and selected negative prompt details
        st.markdown("**Exclude unwanted elements, artifacts, and quality issues**")
        st.text_area(
            "Items to Exclude",
            value=selected_negative,
            height=100,
            disabled=True,
            label_visibility="collapsed"
        )
    
    # Extract placeholders here after template selection
    placeholders = extract_placeholders(selected_template)
    
    st.markdown("---")
    
    # Template Parameters Section - with Style, Lighting, and Mood
    st.markdown('<div class="section-header">⚙️ Template Parameters</div>', unsafe_allow_html=True)
    
    # Style Options
    st.markdown("### 🎨 Style Options")
    style_col1, style_col2 = st.columns([1, 3])
    
    with style_col1:
        use_style_preset = st.checkbox("Use Style Preset", value=True, key="use_style_preset")
    
    with style_col2:
        if use_style_preset:
            selected_style_key = st.selectbox(
                "Select Style Preset",
                options=list(prompt_temp.STYLES.keys()),
                format_func=lambda x: x.replace("_", " ").title(),
                help="Choose a predefined style",
                label_visibility="collapsed"
            )
            selected_style = prompt_temp.STYLES[selected_style_key]
            st.caption(f"📌 {selected_style}")
        else:
            selected_style = st.text_input(
                "Enter Custom Style",
                value="",
                placeholder="e.g., realistic, detailed, high quality",
                help="Enter your custom style description",
                label_visibility="collapsed"
            )
    
    # Lighting Options
    st.markdown("### 💡 Lighting Options")
    lighting_col1, lighting_col2 = st.columns([1, 3])
    
    with lighting_col1:
        use_lighting_preset = st.checkbox("Use Lighting Preset", value=True, key="use_lighting_preset")
    
    with lighting_col2:
        if use_lighting_preset:
            selected_lighting = st.selectbox(
                "Select Lighting Preset",
                options=prompt_temp.LIGHTING_OPTIONS,
                help="Choose a predefined lighting option",
                label_visibility="collapsed"
            )
        else:
            selected_lighting = st.text_input(
                "Enter Custom Lighting",
                value="",
                placeholder="e.g., natural lighting, soft diffused light",
                help="Enter your custom lighting description",
                label_visibility="collapsed"
            )
    
    # Mood Options (always available)
    st.markdown("### 🎭 Mood Options")
    mood_col1, mood_col2 = st.columns([1, 3])
    
    with mood_col1:
        use_mood_preset = st.checkbox("Use Mood Preset", value=True, key="use_mood_preset")
    
    with mood_col2:
        if use_mood_preset:
            selected_mood = st.selectbox(
                "Select Mood",
                options=["peaceful", "dramatic", "mysterious", "joyful", "melancholic", "epic", "serene", "intense", "atmospheric", "ethereal"],
                help="Choose a mood for your image",
                label_visibility="collapsed"
            )
        else:
            selected_mood = st.text_input(
                "Enter Custom Mood",
                value="",
                placeholder="e.g., dark and moody, bright and cheerful",
                help="Enter your custom mood description",
                label_visibility="collapsed"
            )
    
    st.markdown("---")
    
    # Camera Details Section (Optional)
    st.markdown("### 📷 Camera Details (Optional)")
    camera_col1, camera_col2 = st.columns([1, 3])
    
    with camera_col1:
        use_camera_details = st.checkbox(
            "Add Camera Details", 
            value=False, 
            key="use_camera_details",
            help="Include technical camera specifications to control the artistic perspective and depth of your image"
        )
    
    with camera_col2:
        if use_camera_details:
            camera_presets = [
                "50mm lens, f/1.8, shallow depth of field",
                "85mm lens, f/2.8, portrait",
                "35mm lens, f/4, wide angle",
                "24mm lens, f/8, landscape",
                "100mm lens, f/2.0, macro",
                "200mm lens, f/5.6, telephoto",
                "18mm lens, f/11, ultra wide",
                "70-200mm lens, f/4, versatile zoom",
                "Custom"
            ]
            
            camera_selection = st.selectbox(
                "Camera Setup",
                options=camera_presets,
                help="Camera specifications help achieve specific artistic effects: wider aperture (f/1.8) creates background blur, longer focal length (85mm+) flatters portraits, wider angles (24mm-) capture expansive scenes. Use for realistic photography styles.",
                label_visibility="collapsed"
            )
            
            if camera_selection == "Custom":
                camera_details = st.text_input(
                    "Enter Custom Camera Details",
                    placeholder="e.g., 75mm lens, f/1.4, bokeh effect",
                    label_visibility="collapsed"
                )
            else:
                camera_details = camera_selection
                st.caption(f"📌 {camera_details}")
        else:
            camera_details = ""
    
    st.markdown("---")
    
    # Dynamic Template Parameters Section - 2 columns layout
    st.markdown("### 📝 Template-Specific Fields")
    
    # Dynamic input fields based on placeholders in 2-column layout
    placeholder_values = {}
    
    # Skip style, lighting, mood, and camera_details as they're handled separately
    skip_placeholders = {"style", "lighting", "mood", "camera_details"}
    
    # Filter out placeholders that are already handled
    filtered_placeholders = [p for p in placeholders if p not in skip_placeholders]
    
    # Show helpful info about context-aware suggestions
    if filtered_placeholders:
        st.caption(f"💡 Dropdown values are tailored for **{selected_category}** templates")
    
    # Add values for skipped placeholders
    if "style" in placeholders:
        placeholder_values["style"] = selected_style
    if "lighting" in placeholders:
        placeholder_values["lighting"] = selected_lighting
    if "mood" in placeholders:
        placeholder_values["mood"] = selected_mood
    if "camera_details" in placeholders:
        placeholder_values["camera_details"] = camera_details
    
    # Process remaining placeholders in pairs for 2-column layout
    for i in range(0, len(filtered_placeholders), 2):
        param_col1, param_col2 = st.columns(2)
        
        # First placeholder in the row
        with param_col1:
            placeholder = filtered_placeholders[i]
            suggestions = get_placeholder_suggestions(placeholder, selected_category)
            
            st.markdown(f"**{placeholder.replace('_', ' ').title()}**")
            
            if placeholder == "quality":
                quality_option = st.selectbox(
                    f"Select {placeholder}",
                    options=prompt_temp.QUALITY_MODIFIERS,
                    key=f"select_{placeholder}",
                    label_visibility="collapsed"
                )
                placeholder_values[placeholder] = quality_option
            
            elif suggestions:
                # If suggestions exist, offer dropdown with custom option
                use_custom = st.checkbox(f"Custom", key=f"custom_{placeholder}")
                
                if use_custom:
                    placeholder_values[placeholder] = st.text_input(
                        f"Enter {placeholder}",
                        key=f"input_{placeholder}",
                        placeholder=f"Enter custom {placeholder}",
                        label_visibility="collapsed"
                    )
                else:
                    placeholder_values[placeholder] = st.selectbox(
                        f"Select {placeholder}",
                        options=suggestions,
                        key=f"select_{placeholder}",
                        label_visibility="collapsed"
                    )
            else:
                # Generic text input
                placeholder_values[placeholder] = st.text_input(
                    f"Enter {placeholder}",
                    key=f"input_{placeholder}",
                    placeholder=f"Describe the {placeholder}",
                    label_visibility="collapsed"
                )
        
        # Second placeholder in the row (if exists)
        if i + 1 < len(filtered_placeholders):
            with param_col2:
                placeholder = filtered_placeholders[i + 1]
                suggestions = get_placeholder_suggestions(placeholder, selected_category)
                
                st.markdown(f"**{placeholder.replace('_', ' ').title()}**")
                
                if placeholder == "quality":
                    quality_option = st.selectbox(
                        f"Select {placeholder}",
                        options=prompt_temp.QUALITY_MODIFIERS,
                        key=f"select_{placeholder}",
                        label_visibility="collapsed"
                    )
                    placeholder_values[placeholder] = quality_option
                
                elif suggestions:
                    # If suggestions exist, offer dropdown with custom option
                    use_custom = st.checkbox(f"Custom", key=f"custom_{placeholder}")
                    
                    if use_custom:
                        placeholder_values[placeholder] = st.text_input(
                            f"Enter {placeholder}",
                            key=f"input_{placeholder}",
                            placeholder=f"Enter custom {placeholder}",
                            label_visibility="collapsed"
                        )
                    else:
                        placeholder_values[placeholder] = st.selectbox(
                            f"Select {placeholder}",
                            options=suggestions,
                            key=f"select_{placeholder}",
                            label_visibility="collapsed"
                        )
                else:
                    # Generic text input
                    placeholder_values[placeholder] = st.text_input(
                        f"Enter {placeholder}",
                        key=f"input_{placeholder}",
                        placeholder=f"Describe the {placeholder}",
                        label_visibility="collapsed"
                    )
    
    st.markdown("")  # Add spacing
    
    # Generate preview button - full width
    if st.button("🔄 Generate Preview", key="preview_button"):
        # Validate all fields are filled
        missing_fields = []
        
        # Check style, lighting, mood
        if not selected_style:
            missing_fields.append("Style")
        if not selected_lighting:
            missing_fields.append("Lighting")
        if "mood" in placeholders and not selected_mood:
            missing_fields.append("Mood")
        
        # Check template parameters
        missing_fields.extend([p for p, v in placeholder_values.items() if not v])
        
        if missing_fields:
            st.error(f"⚠️ Please fill in all required fields: {', '.join(missing_fields)}")
        else:
            # Generate the prompt
            final_prompt = prompt_temp.format_prompt(selected_template, **placeholder_values)
            
            # Use the selected negative prompt
            final_negative = selected_negative
            
            # Store in session state
            st.session_state.generated_prompt = final_prompt
            st.session_state.generated_negative = final_negative
            
            st.success("✅ Preview generated successfully!")
    
    # Prompt Preview Section - Full Width Single Row
    st.markdown("---")
    st.markdown('<div class="section-header">👁️ Prompt Preview</div>', unsafe_allow_html=True)
    
    if st.session_state.generated_prompt:
        # Calculate token counts
        prompt_tokens = estimate_tokens(st.session_state.generated_prompt)
        negative_tokens = estimate_tokens(st.session_state.generated_negative)
        total_tokens = prompt_tokens + negative_tokens
        
        # Display prompts in single row
        preview_col1, preview_col2 = st.columns([1, 1])
        
        with preview_col1:
            st.markdown(f"**✨ Generated Prompt:** `{prompt_tokens} tokens`")
            st.markdown(f'<div class="preview-box">{st.session_state.generated_prompt}</div>', 
                       unsafe_allow_html=True)
            st.code(st.session_state.generated_prompt, language="text")
        
        with preview_col2:
            st.markdown(f"**🚫 What to Avoid:** `{negative_tokens} tokens`")
            st.markdown(f'<div class="negative-preview-box">{st.session_state.generated_negative}</div>', 
                       unsafe_allow_html=True)
            st.code(st.session_state.generated_negative, language="text")
        
        # Show total token count
        st.info(f"📊 **Total Token Count:** {total_tokens} tokens (Prompt: {prompt_tokens} + Negative: {negative_tokens})")
        
        # Generation parameters in a single row
        st.markdown("")
        st.markdown("**⚙️ Generation Parameters:**")
        
        param_col1, param_col2, param_col3 = st.columns(3)
        
        with param_col1:
            num_steps = st.slider("Inference Steps", 10, 100, 25, 5)
        
        with param_col2:
            guidance_scale = st.slider("Guidance Scale", 1.0, 20.0, 7.5, 0.5)
        
        with param_col3:
            seed = st.number_input("Seed", min_value=0, value=42, step=1)
        
        st.markdown('<div class="info-box">💡 <b>Tip:</b> Higher inference steps = better quality but slower. Guidance scale controls how closely the model follows your prompt.</div>', 
                   unsafe_allow_html=True)
    else:
        st.info("👆 Fill in the template parameters and click 'Generate Preview' to see your prompt here.")
    
    # Image Generation Section
    st.markdown("---")
    st.markdown('<div class="section-header">🖼️ Step 2: Generate Image</div>', unsafe_allow_html=True)
    
    gen_col1, gen_col2 = st.columns([2, 3])
    
    with gen_col1:
        if st.session_state.generated_prompt:
            st.markdown("### 🎬 Generation Settings")
            
            # Generation parameters
            st.markdown("**📐 Image Configuration:**")
            
            image_size = st.selectbox(
                "Image Size",
                options=["512x512", "768x768", "512x768", "768x512"],
                index=0,
                key="image_size_select"
            )
            
            # Parse image size
            width, height = map(int, image_size.split('x'))
            
            num_images = st.slider("Number of Images", 1, 4, 1, key="num_images_slider")
            
            # Get generation parameters from preview section
            generation_params = {
                'num_steps': num_steps if 'num_steps' in locals() else 25,
                'guidance_scale': guidance_scale if 'guidance_scale' in locals() else 7.5,
                'seed': seed if 'seed' in locals() else None
            }
            
            st.markdown("")
            
            # Generate button - Model is already loaded at this point
            if st.button("🚀 Generate Image Now", key="generate_button", type="primary"):
                with st.spinner(f"🎨 Generating {num_images} image(s)... Please wait..."):
                    try:
                        # Prepare template info for metadata
                        template_info = {
                            "category": selected_category,
                            "template": selected_template,
                            "template_index": selected_template_idx,
                            "inputs": placeholder_values.copy(),
                            "style": selected_style,
                            "lighting": selected_lighting,
                            "mood": selected_mood,
                            "camera_details": camera_details if use_camera_details else None,
                            "negative_prompt_type": selected_negative_key
                        }
                        
                        # Generate images
                        images, metadata = st.session_state.generator.generate_image(
                            prompt=st.session_state.generated_prompt,
                            negative_prompt=st.session_state.generated_negative,
                            num_inference_steps=generation_params['num_steps'],
                            guidance_scale=generation_params['guidance_scale'],
                            seed=generation_params['seed'],
                            width=width,
                            height=height,
                            num_images=num_images,
                            template_info=template_info
                        )
                        
                        # Save images with metadata
                        saved_paths = []
                        for idx, img in enumerate(images):
                            # Add index to metadata if multiple images
                            img_metadata = metadata.copy()
                            if num_images > 1:
                                img_metadata['image_index'] = idx + 1
                            
                            # Save image
                            filepath = ImageGenerator.save_image_with_metadata(
                                img,
                                img_metadata,
                                output_dir="generated_images"
                            )
                            saved_paths.append(filepath)
                        
                        # Store in session state
                        st.session_state.generated_images = images
                        st.session_state.image_metadata = metadata
                        st.session_state.saved_paths = saved_paths
                        
                        st.success(f"✅ Generated {len(images)} image(s) successfully!")
                        st.balloons()
                        
                    except Exception as e:
                        st.error(f"❌ Error generating image: {str(e)}")
        else:
            st.warning("⚠️ Please generate a prompt preview first before generating images.")
    
    with gen_col2:
        st.markdown("### 🖼️ Generated Images")
        
        if st.session_state.generated_images:
            # Display generated images
            for idx, img in enumerate(st.session_state.generated_images):
                st.image(img, caption=f"Generated Image {idx + 1}", width='stretch')
                
                # Show saved path
                if hasattr(st.session_state, 'saved_paths') and idx < len(st.session_state.saved_paths):
                    st.caption(f"💾 Saved: {st.session_state.saved_paths[idx]}")
            
            # Show metadata if available
            if hasattr(st.session_state, 'image_metadata'):
                with st.expander("📋 View Full Metadata"):
                    # Show template inputs prominently
                    if 'template_info' in st.session_state.image_metadata:
                        template_info = st.session_state.image_metadata['template_info']
                        
                        st.markdown("### 🎯 Template Information")
                        st.markdown(f"**Category:** {template_info.get('category', 'N/A')}")
                        st.markdown(f"**Template:** {template_info.get('template', 'N/A')}")
                        
                        st.markdown("### 📝 User Inputs")
                        inputs = template_info.get('inputs', {})
                        if inputs:
                            # Display inputs in a nice format
                            input_cols = st.columns(2)
                            input_items = list(inputs.items())
                            
                            for idx, (key, value) in enumerate(input_items):
                                with input_cols[idx % 2]:
                                    st.markdown(f"**{key.replace('_', ' ').title()}:** {value}")
                        
                        st.markdown("### 🎨 Style Configuration")
                        st.markdown(f"**Style:** {template_info.get('style', 'N/A')}")
                        st.markdown(f"**Lighting:** {template_info.get('lighting', 'N/A')}")
                        st.markdown(f"**Mood:** {template_info.get('mood', 'N/A')}")
                        if template_info.get('camera_details'):
                            st.markdown(f"**Camera:** {template_info.get('camera_details')}")
                        st.markdown(f"**Negative Type:** {template_info.get('negative_prompt_type', 'N/A')}")
                        
                        st.markdown("---")
                    
                    st.markdown("### ⚙️ Complete Metadata")
                    st.json(st.session_state.image_metadata)
        else:
            st.markdown("*Generated images will appear here*")
            st.info("👆 Configure parameters and click 'Generate Image' to create your artwork!")
    
    # Footer
    st.markdown("---")
    st.markdown("""
        <div style="text-align: center; color: #7f8c8d; padding: 1rem;">
            <p>🎨 <b>AI Artist - Prompt Builder</b> | Built with Streamlit & Stable Diffusion</p>
            <p><i>Configure your prompts with precision and creativity!</i></p>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

