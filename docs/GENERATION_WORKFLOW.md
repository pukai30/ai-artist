# 🎨 Image Generation Workflow - Complete Guide

## ✅ Integration Status: COMPLETE!

The Streamlit app is **fully integrated** with the ImageGenerator from `main.py`. 

---

## 🔄 Complete Generation Workflow

### Step-by-Step Process:

```
1. User Creates Prompt in UI
   ↓
2. Prompt Preview Generated (with token count)
   ↓
3. User Clicks "Load Model" (one-time)
   ↓
4. ImageGenerator loads Stable Diffusion
   ↓
5. User Configures Generation (size, quantity)
   ↓
6. User Clicks "Generate Image"
   ↓
7. ImageGenerator.generate_image() called
   ↓
8. Images generated with all metadata
   ↓
9. Images saved to generated_images/
   ↓
10. Images displayed in UI
   ↓
11. Metadata shown with template inputs
```

---

## 📝 Detailed Integration Flow

### Phase 1: Prompt Creation

**In Streamlit UI:**
```python
# User selects and fills:
- Template Category: "Character"
- Template: Template 1
- Style: "anime style"
- Lighting: "dramatic side lighting"
- Mood: "epic"
- Inputs: character, pose, outfit, background, quality

# Click "Generate Preview"

# System creates:
generated_prompt = "a anime style character design of warrior princess..."
generated_negative = "photograph, photo, realistic..."
```

---

### Phase 2: Model Loading (One-Time)

**In Streamlit UI:**
```python
# User clicks "Load Stable Diffusion Model"

# System calls:
st.session_state.generator = ImageGenerator(device="cpu")
st.session_state.model_loaded = generator.load_model()

# In main.py:
def load_model(self):
    self.pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float32,
        safety_checker=None
    )
    self.pipe = self.pipe.to("cpu")
    return True
```

**Status in Terminal:**
```
torch version: 2.8.0+cpu
CUDA available: False
Loading Stable Diffusion pipeline...
Loading pipeline components... 17% | 1/6
```

---

### Phase 3: Image Generation

**In Streamlit UI:**
```python
# User clicks "Generate Image"

# System prepares template_info:
template_info = {
    "category": "Character",
    "template": "a {style} character design...",
    "template_index": 0,
    "inputs": {
        "character": "warrior princess",
        "pose": "dynamic action pose",
        "outfit": "ornate armor",
        "background": "fantasy castle",
        "quality": "detailed, 4k"
    },
    "style": "anime style",
    "lighting": "dramatic side lighting",
    "mood": "epic",
    "camera_details": None,
    "negative_prompt_type": "artistic"
}

# System calls ImageGenerator:
images, metadata = st.session_state.generator.generate_image(
    prompt=generated_prompt,
    negative_prompt=generated_negative,
    num_inference_steps=25,
    guidance_scale=7.5,
    seed=42,
    width=512,
    height=512,
    num_images=1,
    template_info=template_info  # ← All inputs included!
)
```

**In main.py:**
```python
def generate_image(self, ..., template_info=None):
    # Generate using Stable Diffusion
    result = self.pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=num_inference_steps,
        guidance_scale=guidance_scale,
        generator=generator,
        width=width,
        height=height,
        num_images_per_prompt=num_images
    )
    
    # Create metadata with template_info
    metadata = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        # ... all parameters ...
        "template_info": template_info  # ← Includes all inputs!
    }
    
    return result.images, metadata
```

---

### Phase 4: Image Saving

**In Streamlit UI:**
```python
# For each generated image:
for idx, img in enumerate(images):
    filepath = ImageGenerator.save_image_with_metadata(
        img,
        metadata,
        output_dir="generated_images"
    )
    saved_paths.append(filepath)
```

**In main.py:**
```python
@staticmethod
def save_image_with_metadata(image, metadata, output_dir):
    # Generate filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    subject = extract_subject_from_prompt(metadata['prompt'])
    filename = f"{timestamp}_{subject}.png"
    
    # Save PNG with embedded metadata
    png_info = PngInfo()
    png_info.add_text("prompt", metadata['prompt'])
    png_info.add_text("negative_prompt", metadata['negative_prompt'])
    png_info.add_text("parameters", json.dumps(metadata))
    
    image.save(filepath, "PNG", pnginfo=png_info)
    
    # Save JSON sidecar
    with open(json_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    return filepath
```

**Creates:**
```
generated_images/
├── 20241009_150030_warrior_princess.png  ← Image + metadata
└── 20241009_150030_warrior_princess.json ← Full JSON
```

---

### Phase 5: Display in UI

**In Streamlit UI:**
```python
# Display generated images
for idx, img in enumerate(images):
    st.image(img, caption=f"Generated Image {idx + 1}")
    st.caption(f"💾 Saved: {saved_paths[idx]}")

# Show metadata with template inputs
with st.expander("📋 View Full Metadata"):
    # Template Information
    st.markdown(f"Category: {template_info['category']}")
    
    # User Inputs ← YOUR INPUTS DISPLAYED!
    for key, value in template_info['inputs'].items():
        st.markdown(f"{key}: {value}")
    
    # Style Configuration
    st.markdown(f"Style: {template_info['style']}")
    st.markdown(f"Lighting: {template_info['lighting']}")
    st.markdown(f"Mood: {template_info['mood']}")
```

---

## 🎯 Integration Points

### 1. Import ImageGenerator
```python
# Line 10 in streamlit_app.py
from main import ImageGenerator
```

### 2. Initialize in Session State
```python
# Lines 564-569
if 'generator' not in st.session_state:
    st.session_state.generator = None
    st.session_state.model_loaded = False
```

### 3. Load Model Button
```python
# Lines 578-587
if st.button("🔄 Load Stable Diffusion Model"):
    with st.spinner("Loading model..."):
        st.session_state.generator = ImageGenerator(device="cpu")
        st.session_state.model_loaded = st.session_state.generator.load_model()
```

### 4. Generate Button with Template Info
```python
# Lines 613-668
if st.button("🚀 Generate Image"):
    # Prepare template_info with all inputs
    template_info = {
        "category": selected_category,
        "inputs": placeholder_values,  # All user inputs!
        "style": selected_style,
        # ... everything the user selected
    }
    
    # Call ImageGenerator
    images, metadata = st.session_state.generator.generate_image(
        prompt=st.session_state.generated_prompt,
        negative_prompt=st.session_state.generated_negative,
        template_info=template_info  # Pass all inputs!
    )
    
    # Save with metadata
    for img in images:
        filepath = ImageGenerator.save_image_with_metadata(img, metadata)
```

### 5. Display Results
```python
# Lines 685-729
if st.session_state.generated_images:
    # Show images
    for img in st.session_state.generated_images:
        st.image(img)
    
    # Show metadata with template inputs
    with st.expander("📋 View Full Metadata"):
        # Display template inputs nicely
```

---

## 📊 Data Flow Diagram

```
┌─────────────────────────────────────────────────┐
│           STREAMLIT UI (streamlit_app.py)       │
│                                                 │
│  User Input:                                   │
│  - Template: "Character"                       │
│  - Inputs: character="warrior princess"        │
│  - Style: "anime"                              │
│  - Lighting: "dramatic"                        │
│                                                 │
│  ↓ Click "Generate Preview"                    │
│                                                 │
│  Generated:                                    │
│  - prompt = "a anime style character..."       │
│  - negative = "photograph, photo..."           │
│                                                 │
│  ↓ Click "Generate Image"                      │
│                                                 │
│  Prepares:                                     │
│  template_info = {                             │
│    "category": "Character",                    │
│    "inputs": {"character": "warrior..."}, ...  │
│  }                                             │
│                                                 │
│  ↓ Calls ImageGenerator                        │
└─────────────────┬───────────────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────────────┐
│        IMAGE GENERATOR (main.py)                │
│                                                 │
│  generate_image(                               │
│    prompt,                                     │
│    negative_prompt,                            │
│    parameters,                                 │
│    template_info  ← Includes all user inputs   │
│  )                                             │
│                                                 │
│  ↓ Calls Stable Diffusion Pipeline             │
│                                                 │
│  result = self.pipe(                           │
│    prompt=prompt,                              │
│    negative_prompt=negative_prompt,            │
│    num_inference_steps=25,                     │
│    ...                                         │
│  )                                             │
│                                                 │
│  ↓ Creates metadata with template_info         │
│                                                 │
│  metadata = {                                  │
│    "prompt": "...",                            │
│    "template_info": template_info  ← Saved!    │
│  }                                             │
│                                                 │
│  ↓ Returns images and metadata                 │
└─────────────────┬───────────────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────────────┐
│            SAVE & DISPLAY                       │
│                                                 │
│  save_image_with_metadata()                    │
│  ↓                                             │
│  Creates:                                      │
│  - 20241009_150030_warrior_princess.png        │
│  - 20241009_150030_warrior_princess.json       │
│                                                 │
│  JSON Contains:                                │
│  {                                             │
│    "prompt": "Full prompt...",                 │
│    "template_info": {                          │
│      "inputs": {                               │
│        "character": "warrior princess", ...    │
│      }                                         │
│    }                                           │
│  }                                             │
│                                                 │
│  ↓ Display in Streamlit                        │
│                                                 │
│  Shows:                                        │
│  - Generated images                            │
│  - Save paths                                  │
│  - Template inputs in metadata viewer          │
└─────────────────────────────────────────────────┘
```

---

## 🎯 What's Integrated

### ✅ **Model Loading:**
- Button in UI triggers `ImageGenerator.load_model()`
- Model loaded once per session
- Status displayed in UI

### ✅ **Image Generation:**
- Button triggers `ImageGenerator.generate_image()`
- All parameters passed from UI
- Template info included
- Progress spinner shown

### ✅ **Metadata Tracking:**
- Template inputs collected
- Style/lighting/mood selections saved
- All parameters preserved
- Saved to PNG + JSON

### ✅ **File Management:**
- Auto-generated filenames
- Timestamp + subject
- Organized in `generated_images/`

### ✅ **Display:**
- Images shown in UI
- Save paths displayed
- Metadata viewer with template inputs

---

## 🧪 Test the Integration

### The App is Running!

Check: **http://localhost:8504**

### Complete Test Flow:

1. **Create Prompt:**
   - Select "Character" category
   - Choose Template 1
   - Style: "Anime"
   - Lighting: "Dramatic side lighting"
   - Mood: "Epic"
   - Fill inputs: character, pose, outfit, background, quality
   - Click "Generate Preview"

2. **Load Model:**
   - See "Model not loaded yet" warning
   - Click "Load Stable Diffusion Model"
   - Wait for loading (you can see it loading in terminal!)
   - See "✅ Model loaded successfully!"

3. **Generate Image:**
   - Select image size (512x512)
   - Choose number of images (1)
   - Adjust steps, guidance, seed if desired
   - Click "🚀 Generate Image"
   - Wait 30-60 seconds (on CPU)

4. **View Results:**
   - See generated image(s) in UI
   - Check save path: `generated_images/YYYYMMDD_HHMMSS_subject.png`
   - Click "View Full Metadata"
   - See all your inputs preserved!

5. **Check Files:**
   ```bash
   dir generated_images
   # or
   ls generated_images
   ```
   You'll see:
   - PNG file with image
   - JSON file with complete metadata

---

## 💾 Metadata Example from Your Generation

When you generate a Character image, the JSON will contain:

```json
{
  "prompt": "a anime style, cel shaded, vibrant colors character design of warrior princess, dynamic action pose, ornate armor with flowing cape, fantasy castle ruins, detailed, vibrant colors, 4k",
  "negative_prompt": "photograph, photo, realistic, photorealistic, blurry, low quality...",
  "num_inference_steps": 25,
  "guidance_scale": 7.5,
  "seed": 42,
  "width": 512,
  "height": 512,
  "num_images": 1,
  "generation_time": 45.67,
  "model": "runwayml/stable-diffusion-v1-5",
  "device": "cpu",
  "timestamp": "2024-10-09T15:00:30.123456",
  "template_info": {
    "category": "Character",
    "template": "a {style} character design of {character}, {pose}, {outfit}, {background}, {quality}",
    "template_index": 0,
    "inputs": {
      "character": "warrior princess",
      "pose": "dynamic action pose",
      "outfit": "ornate armor with flowing cape",
      "background": "fantasy castle ruins",
      "quality": "detailed, vibrant colors, 4k"
    },
    "style": "anime style, cel shaded, vibrant colors",
    "lighting": "dramatic side lighting",
    "mood": "epic",
    "camera_details": null,
    "negative_prompt_type": "artistic"
  }
}
```

**All your inputs are preserved!** ✅

---

## 🎨 UI Integration Features

### In the UI You'll See:

#### Before Model Load:
```
⚠️ Model not loaded yet
[🔄 Load Stable Diffusion Model]
```

#### After Model Load:
```
✅ Model loaded successfully!

Image Size: [512x512 ▼]
Number of Images: [1 ━━━━○━━━━ 4]

[🚀 Generate Image]
```

#### During Generation:
```
🎨 Generating 1 image(s)... Please wait...
[Progress spinner]
```

#### After Generation:
```
✅ Generated 1 image(s) successfully!
🎉 [Balloons animation]

🖼️ Generated Images
[Your image displayed]
💾 Saved: generated_images/20241009_150030_warrior_princess.png

📋 View Full Metadata
[Click to expand and see all inputs]
```

---

## 🔧 Key Integration Code Snippets

### Import (Line 10):
```python
from main import ImageGenerator
```

### Initialize (Lines 564-569):
```python
if 'generator' not in st.session_state:
    st.session_state.generator = None
    st.session_state.model_loaded = False
```

### Load Model (Lines 580-587):
```python
if st.button("🔄 Load Stable Diffusion Model"):
    with st.spinner("Loading model..."):
        st.session_state.generator = ImageGenerator(device="cpu")
        st.session_state.model_loaded = st.session_state.generator.load_model()
```

### Generate with Template Info (Lines 613-668):
```python
template_info = {
    "category": selected_category,
    "template": selected_template,
    "inputs": placeholder_values.copy(),  # ← All user inputs!
    "style": selected_style,
    "lighting": selected_lighting,
    "mood": selected_mood,
    "camera_details": camera_details,
    "negative_prompt_type": selected_negative_key
}

images, metadata = st.session_state.generator.generate_image(
    prompt=st.session_state.generated_prompt,
    negative_prompt=st.session_state.generated_negative,
    num_inference_steps=generation_params['num_steps'],
    guidance_scale=generation_params['guidance_scale'],
    seed=generation_params['seed'],
    width=width,
    height=height,
    num_images=num_images,
    template_info=template_info  # ← Passed to generator!
)
```

### Display Metadata (Lines 698-729):
```python
with st.expander("📋 View Full Metadata"):
    if 'template_info' in metadata:
        st.markdown("### 📝 User Inputs")
        for key, value in template_info['inputs'].items():
            st.markdown(f"**{key}:** {value}")
```

---

## 📊 What Gets Saved

### In PNG File (Embedded):
- Prompt text
- Negative prompt text
- All parameters as JSON

### In JSON File (Complete):
- Everything from PNG
- **Plus template_info with all inputs**
- Generation time
- Timestamp
- Full parameter set

---

## 🎯 Usage Example

### Complete Workflow in Action:

**Terminal shows:**
```
$ uv run streamlit run streamlit_app.py

  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8504

torch version: 2.8.0+cpu
CUDA available: False
Loading Stable Diffusion pipeline...
Loading pipeline components... [Progress]
Pipeline loaded successfully on cpu!
```

**In Browser:**
1. Fill Character template
2. Click "Load Model" (see terminal progress)
3. Click "Generate Image"
4. See progress in terminal and spinner in UI
5. Image appears with metadata

**Result:**
- Image displayed in browser
- File saved in `generated_images/`
- Complete metadata with all inputs
- Can reproduce exactly!

---

## 🎉 Integration Complete!

The Streamlit app is **fully integrated** with the ImageGenerator:

✅ All prompts created in UI
✅ All parameters passed to generator
✅ All inputs saved in metadata
✅ Images generated and saved
✅ Complete workflow functional

**Start creating your AI art now!** 🎨✨

Access the app at: **http://localhost:8504**

