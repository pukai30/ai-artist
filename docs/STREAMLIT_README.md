# 🎨 AI Artist - Streamlit Prompt Builder

A comprehensive Streamlit UI for building sophisticated image generation prompts using Stable Diffusion. This interactive application provides a user-friendly interface to create, customize, and preview prompts before generating images.

## 📁 Project Structure

```
ai-artist/
├── streamlit_app.py           # Main Streamlit application
├── prompt_temp.py             # Template library with 50+ prompts
├── example_usage.py           # Example integration with Stable Diffusion
├── test_streamlit_integration.py  # Test suite
├── main.py                    # Original image generation script
├── STREAMLIT_GUIDE.md         # Detailed usage guide
└── pyproject.toml             # Project dependencies
```

## 🚀 Quick Start

### 1. Installation

Ensure you have Python 3.12+ installed. Install dependencies:

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install streamlit torch diffusers transformers pillow
```

### 2. Run Tests (Optional)

Verify everything is set up correctly:

```bash
python test_streamlit_integration.py
```

You should see:
```
✨ ALL TESTS COMPLETED
🚀 Ready to run Streamlit app!
```

### 3. Launch the Streamlit App

```bash
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`

## ✨ Features

### 📝 Template System

**10 Template Categories** with 5 variations each (50 total templates):
- 🎭 **Portrait** - Character portraits and headshots
- 🏞️ **Landscape** - Scenic views and nature
- 🐉 **Fantasy** - Magical creatures and fantasy scenes
- 🚀 **Sci-Fi** - Futuristic and cyberpunk imagery
- 🦁 **Animal** - Wildlife photography
- 🏛️ **Architecture** - Buildings and interiors
- 🎨 **Abstract** - Abstract art and concepts
- 🍕 **Food** - Food photography
- 👤 **Character** - Full character designs
- 📦 **Product** - Product photography

### 🎨 Customization Options

**Style Presets (14 options):**
- Realistic, Cinematic, Anime, Oil Painting, Watercolor
- Digital Art, Sketch, 3D Render, Pixel Art
- Impressionist, Film Noir, Steampunk, Minimalist, Psychedelic

**Lighting Options (10 options):**
- Soft diffused, Dramatic side, Golden hour, Studio
- Natural, Neon, Backlit, Rim, Volumetric, Cinematic

**Negative Prompts (9 types):**
- General, Portrait, Realistic, Artistic, Fantasy
- Minimal, Product, Landscape, Clean

**Quality Modifiers (5 presets):**
- Professional descriptions for optimal image quality
- 4K, 8K, masterpiece, ultra detailed options

### 🔧 Smart Features

1. **Dynamic Input Fields** - Automatically detects template placeholders
2. **Intelligent Suggestions** - Context-aware dropdown options
3. **Real-time Preview** - See formatted prompts instantly
4. **Parameter Control** - Fine-tune generation settings
5. **Copy-Friendly Output** - Easy-to-copy code blocks

## 📖 Usage Example

### Creating a Fantasy Dragon Portrait

1. **Select Template** (Sidebar)
   ```
   Category: Fantasy
   Template: Template 1
   ```

2. **Configure Options** (Sidebar)
   ```
   Style: Digital Art
   Lighting: Dramatic side lighting
   Negative: Fantasy
   ```

3. **Fill Parameters** (Main Area)
   ```
   Creature: majestic dragon
   Setting: misty mountain peak
   Mood: epic and mysterious
   Quality: masterpiece, best quality, ultra detailed, 8k
   ```

4. **Generate Preview**
   - Click "Generate Preview" button
   - View formatted prompt:
   ```
   a digital art illustration of majestic dragon in misty mountain peak,
   epic and mysterious atmosphere, masterpiece, best quality, ultra detailed, 8k
   ```

5. **Set Generation Parameters**
   ```
   Inference Steps: 30
   Guidance Scale: 7.5
   Seed: 42
   ```

6. **Generate Image** (Coming soon)

## 🎯 Features Breakdown

### Sidebar Navigation

```
🎯 Template Selection
   ├─ Template Category Dropdown
   ├─ Specific Template Selector
   └─ Template Preview

🎨 Style Options
   ├─ Use Style Preset (checkbox)
   └─ Style Dropdown/Input

💡 Lighting Options
   ├─ Use Lighting Preset (checkbox)
   └─ Lighting Dropdown/Input

🚫 Negative Prompt
   ├─ Negative Type Selector
   ├─ View Negative Prompt (expander)
   └─ Custom Negative Terms (textarea)
```

### Main Content Area

```
Column 1: Template Parameters
├─ Dynamic input fields based on template
├─ Smart suggestions for common fields
├─ Checkbox toggles for custom inputs
└─ Generate Preview button

Column 2: Prompt Preview
├─ Generated positive prompt
├─ Generated negative prompt
├─ Copyable code blocks
└─ Generation parameters sliders
```

### Generation Section

```
Column 1: Settings
├─ Image size selector
├─ Number of images slider
└─ Generate Image button

Column 2: Output
└─ Generated images display (coming soon)
```

## 🔌 Integration with Image Generation

The Streamlit app is designed to work seamlessly with your existing Stable Diffusion pipeline. The generation button collects all parameters:

```python
generation_config = {
    "prompt": "a digital art illustration of...",
    "negative_prompt": "blurry, low quality...",
    "steps": 30,
    "guidance_scale": 7.5,
    "seed": 42,
    "size": "512x512",
    "num_images": 1
}
```

To integrate with `main.py`:

```python
# In streamlit_app.py, replace the placeholder generation section with:
if st.button("Generate Image"):
    with st.spinner("Generating..."):
        from main import pipe
        image = pipe(
            prompt=st.session_state.generated_prompt,
            negative_prompt=st.session_state.generated_negative,
            num_inference_steps=num_steps,
            guidance_scale=guidance_scale,
            generator=torch.Generator().manual_seed(seed)
        ).images[0]
        st.image(image, caption="Generated Image")
```

## 📊 Template Library Details

### prompt_temp.py Contents

```python
# 50 Templates (10 categories × 5 variations)
PORTRAIT_TEMPLATES = [...]
LANDSCAPE_TEMPLATES = [...]
# ... etc

# 9 Negative Prompt Types
NEGATIVE_PROMPTS = {
    "general": "...",
    "portrait": "...",
    # ... etc
}

# 14 Style Presets
STYLES = {
    "realistic": "...",
    "cinematic": "...",
    # ... etc
}

# 10 Lighting Options
LIGHTING_OPTIONS = [...]

# 5 Quality Modifiers
QUALITY_MODIFIERS = [...]

# 10 Complete Example Prompts
EXAMPLE_PROMPTS = [...]

# Utility Functions
format_prompt(template, **kwargs)
create_custom_prompt(category, **kwargs)
print_example_prompts()
```

## 🎨 UI Screenshots Walkthrough

### Main Interface
- **Left Sidebar**: Template and style selection
- **Center Panel**: Dynamic parameter inputs
- **Right Panel**: Real-time prompt preview

### Prompt Preview
- **Formatted Prompt**: Highlighted in blue box
- **Negative Prompt**: Highlighted in yellow box
- **Code Blocks**: Easy copy-paste functionality

### Generation Section
- **Settings Panel**: Configure image parameters
- **Output Panel**: View generated images

## 💡 Pro Tips

1. **Use Style Presets** for consistent results across generations
2. **Combine Lighting Options** with time_of_day for realistic scenes
3. **Layer Negative Prompts** - use preset + custom terms
4. **Quality Modifiers** make a significant difference in output
5. **Save Successful Prompts** by copying from code blocks
6. **Experiment with Seeds** to get variations of the same concept
7. **Higher Inference Steps** (30-50) = better quality, slower generation
8. **Guidance Scale 7-8** works well for most cases

## 🔧 Customization

### Adding New Templates

Edit `prompt_temp.py`:

```python
# Add a new category
NATURE_TEMPLATES = [
    "{style} photo of {subject} in {environment}, {lighting}, {quality}",
    # ... more templates
]
```

Update `streamlit_app.py`:

```python
def get_template_categories():
    categories = {
        # ... existing categories
        "Nature": prompt_temp.NATURE_TEMPLATES,
    }
    return categories
```

### Adding New Styles

Edit `prompt_temp.py`:

```python
STYLES = {
    # ... existing styles
    "my_custom_style": "description of my custom style, detailed, artistic",
}
```

### Customizing UI Theme

Edit the CSS in `streamlit_app.py`:

```python
st.markdown("""
    <style>
    .main-header {
        color: #your-color;  /* Change header color */
    }
    /* ... more custom CSS */
    </style>
""", unsafe_allow_html=True)
```

## 📋 Keyboard Shortcuts

When the Streamlit app is running:

- `R` - Rerun the app
- `Ctrl/Cmd + R` - Clear cache and rerun
- `Ctrl/Cmd + K` - Open command palette
- `Esc` - Close sidebars

## 🐛 Troubleshooting

### App won't start
```bash
# Ensure Streamlit is installed
pip install streamlit

# Check version
streamlit --version
```

### Import errors
```bash
# Ensure prompt_temp.py is in the same directory
# Verify with:
python -c "import prompt_temp; print('OK')"
```

### Windows encoding issues
The test script handles this automatically. If you see encoding errors:
```python
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
```

## 🎯 Next Steps

1. **Test the UI** - Run and explore all features
2. **Integrate Generation** - Connect with Stable Diffusion pipeline
3. **Save/Load Prompts** - Add functionality to save favorite prompts
4. **History** - Track previously generated prompts
5. **Batch Generation** - Generate multiple variations at once
6. **Gallery** - Display history of generated images

## 📚 Additional Resources

- `STREAMLIT_GUIDE.md` - Detailed feature documentation
- `example_usage.py` - Integration examples
- `prompt_temp.py` - View all templates and options
- `test_streamlit_integration.py` - Verify setup

## 🤝 Contributing

To add new features:
1. Templates → Edit `prompt_temp.py`
2. UI Components → Edit `streamlit_app.py`
3. Test → Run `test_streamlit_integration.py`

## 📝 License

Part of the AI Artist project.

---

**Built with ❤️ using Streamlit, Stable Diffusion, and Python**

🚀 **Ready to create amazing AI art!**

