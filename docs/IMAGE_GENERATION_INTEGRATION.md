# 🖼️ Image Generation Integration Guide

## Overview

The AI Artist project now has **full image generation integration** with metadata support, automatic file naming, and embedded prompt information.

---

## What's Been Implemented

### ✅ 1. Refactored `main.py`

**New Structure:**
- `ImageGenerator` class for managing Stable Diffusion pipeline
- Metadata support with PNG embedding
- Automatic filename generation from prompts
- Timestamp-based file naming
- JSON sidecar files for metadata

**Original code:** Commented out for reference

---

### ✅ 2. Streamlit Integration

**Features:**
- Model loading button in UI
- Real-time image generation
- Multiple image support
- Parameter control from UI
- Display generated images
- Show save paths
- View metadata

---

## File Structure

```
ai-artist/
├── main.py                    # ImageGenerator class (refactored)
├── streamlit_app.py           # Streamlit UI (integrated)
├── prompt_temp.py             # Template library
├── generated_images/          # Output directory (created automatically)
│   ├── 20241009_123456_dragon.png
│   ├── 20241009_123456_dragon.json
│   ├── 20241009_123512_landscape.png
│   └── 20241009_123512_landscape.json
└── ...
```

---

## ImageGenerator Class

### Key Methods:

#### 1. `__init__(model_name, device)`
```python
generator = ImageGenerator(
    model_name="runwayml/stable-diffusion-v1-5",
    device="cpu"  # or "cuda" for GPU
)
```

#### 2. `load_model()`
```python
success = generator.load_model()
# Returns: True if loaded, False if failed
```

#### 3. `generate_image(...)`
```python
images, metadata = generator.generate_image(
    prompt="a dragon in mountains",
    negative_prompt="blurry, low quality",
    num_inference_steps=25,
    guidance_scale=7.5,
    seed=42,
    width=512,
    height=512,
    num_images=1
)
```

**Returns:**
- `images`: List of PIL Image objects
- `metadata`: Dict with all generation parameters

#### 4. `save_image_with_metadata(...)`
```python
filepath = ImageGenerator.save_image_with_metadata(
    image=images[0],
    metadata=metadata,
    output_dir="generated_images",
    custom_filename=None  # Auto-generated if None
)
```

**Saves:**
- PNG file with embedded metadata
- JSON sidecar file with full metadata

---

## Metadata Structure

### Embedded in PNG:
```
prompt: "Full generation prompt..."
negative_prompt: "Full negative prompt..."
parameters: {JSON of all other parameters}
```

### JSON Sidecar File:
```json
{
  "prompt": "a dragon flying through mountains...",
  "negative_prompt": "blurry, low quality...",
  "num_inference_steps": 25,
  "guidance_scale": 7.5,
  "seed": 42,
  "width": 512,
  "height": 512,
  "num_images": 1,
  "generation_time": 45.23,
  "model": "runwayml/stable-diffusion-v1-5",
  "device": "cpu",
  "timestamp": "2024-10-09T12:34:56.789",
  "image_index": 1
}
```

---

## Filename Generation

### Format:
```
{timestamp}_{subject}.png
```

### Examples:
```
20241009_123456_dragon_mountains.png
20241009_140512_young_woman_portrait.png
20241009_153022_fantasy_landscape.png
```

### Subject Extraction Logic:
1. Remove common prefixes ("a", "an", "the", "of", etc.)
2. Filter out style keywords ("digital", "art", "8k", etc.)
3. Take first 3 meaningful words
4. Sanitize (lowercase, underscores, no special chars)
5. Limit to 30 characters

---

## Streamlit UI Integration

### Workflow:

#### 1. **Generate Prompt Preview**
- Configure all parameters
- Click "Generate Preview"
- See formatted prompts with token counts

#### 2. **Load Model**
- Click "Load Stable Diffusion Model"
- Wait for model to load (first time only)
- Model stays loaded in session

#### 3. **Configure Generation**
- Select image size (512x512, 768x768, etc.)
- Choose number of images (1-4)
- Parameters from preview used automatically

#### 4. **Generate Images**
- Click "Generate Image"
- Watch progress spinner
- Images appear in preview
- Automatically saved with metadata

#### 5. **View Results**
- See generated images
- Check save paths
- View full metadata
- Download from `generated_images/` folder

---

## UI Features

### Left Column (Controls):
```
🎬 Ready to Generate!

⚠️ Model not loaded yet
[🔄 Load Stable Diffusion Model]

When loaded:
- Image Size: [Dropdown]
- Number of Images: [Slider 1-4]
- [🚀 Generate Image]

📊 Generation Info: [JSON display]
```

### Right Column (Output):
```
🖼️ Generated Images

[Image 1]
💾 Saved: generated_images/20241009_123456_dragon.png

[Image 2]
💾 Saved: generated_images/20241009_123457_dragon.png

📋 View Full Metadata [Expandable]
```

---

## Session State Management

### Variables:
```python
st.session_state.generator          # ImageGenerator instance
st.session_state.model_loaded       # Boolean: is model loaded?
st.session_state.generated_images   # List of PIL Images
st.session_state.image_metadata     # Dict of metadata
st.session_state.saved_paths        # List of file paths
```

---

## Example Usage (Standalone)

### Using ImageGenerator Directly:

```python
from main import ImageGenerator

# Initialize
generator = ImageGenerator(device="cpu")

# Load model
if generator.load_model():
    # Generate
    images, metadata = generator.generate_image(
        prompt="a majestic dragon in mountains",
        negative_prompt="blurry, low quality",
        num_inference_steps=25,
        guidance_scale=7.5,
        seed=42
    )
    
    # Save
    filepath = generator.save_image_with_metadata(
        images[0],
        metadata
    )
    
    print(f"Image saved: {filepath}")
```

---

## Testing the Integration

### Test 1: Standalone Generation
```bash
python main.py
```

**Expected:**
- Loads model
- Generates test image
- Saves to `generated_images/`
- Creates PNG + JSON files

### Test 2: Streamlit Integration
```bash
streamlit run streamlit_app.py
```

**Expected:**
1. Create prompt
2. Load model via button
3. Generate image
4. See image in UI
5. Find files in `generated_images/`

---

## Error Handling

### Model Loading Errors:
```python
if not generator.load_model():
    print("Failed to load model")
    # Show error in UI
```

### Generation Errors:
```python
try:
    images, metadata = generator.generate_image(...)
except RuntimeError as e:
    st.error(f"Error: {e}")
```

### Common Issues:

**Issue:** Model won't load
- **Solution:** Check internet connection, model will download first time

**Issue:** Out of memory
- **Solution:** Use smaller image size, reduce batch size, use CPU instead of GPU

**Issue:** Slow generation
- **Solution:** Normal on CPU (30-60s per image), use GPU for faster generation

---

## Metadata Benefits

### 1. **Reproducibility**
- Exact seed saved
- All parameters recorded
- Can regenerate identical image

### 2. **Learning**
- See what prompts created good images
- Track parameter combinations
- Build prompt library

### 3. **Organization**
- Timestamp for chronological sorting
- Subject name for quick identification
- Searchable JSON files

### 4. **Sharing**
- PNG metadata embedded
- Others can see your prompts
- Professional workflow

---

## Advanced Features

### Multiple Images:
```python
images, metadata = generator.generate_image(
    ...,
    num_images=4  # Generate 4 variations
)

# Each gets unique filename with index
```

### Custom Filenames:
```python
filepath = generator.save_image_with_metadata(
    image,
    metadata,
    custom_filename="my_special_dragon"
)
# Saves as: my_special_dragon.png
```

### Different Image Sizes:
```python
images, metadata = generator.generate_image(
    ...,
    width=768,
    height=512  # Landscape orientation
)
```

---

## Output Directory Structure

```
generated_images/
├── 20241009_120000_dragon_mountains.png
├── 20241009_120000_dragon_mountains.json
├── 20241009_120145_portrait_woman.png
├── 20241009_120145_portrait_woman.json
├── 20241009_120230_fantasy_landscape.png
└── 20241009_120230_fantasy_landscape.json
```

**Format:**
- `YYYYMMDD_HHMMSS_subject.png` - Image with embedded metadata
- `YYYYMMDD_HHMMSS_subject.json` - Metadata sidecar

---

## Performance Notes

### CPU Generation:
- Time: 30-60 seconds per image
- Memory: ~2-4 GB RAM
- Works on any machine

### GPU Generation (CUDA):
- Time: 3-5 seconds per image
- Memory: 4-6 GB VRAM
- Requires NVIDIA GPU

### Model Loading:
- First time: Downloads ~4GB model
- Subsequent: Loads from cache (~30 seconds)
- Stays loaded in memory during session

---

## Future Enhancements

Potential additions:
- 🔮 Image history gallery
- 🔮 Compare multiple generations
- 🔮 Batch generation queue
- 🔮 Different model support
- 🔮 Inpainting/outpainting
- 🔮 Image-to-image generation
- 🔮 ControlNet integration

---

## Code Changes Summary

### `main.py`:
- ✅ Created `ImageGenerator` class
- ✅ Added metadata support
- ✅ Implemented file naming logic
- ✅ Embedded PNG metadata
- ✅ JSON sidecar files
- ✅ Commented out original code

### `streamlit_app.py`:
- ✅ Imported `ImageGenerator`
- ✅ Added model loading UI
- ✅ Integrated generation workflow
- ✅ Display generated images
- ✅ Show metadata
- ✅ Session state management

### `.gitignore`:
- ✅ Added `generated_images/` directory

---

## Summary

### What You Can Do Now:
1. ✅ Create prompts in UI
2. ✅ Load Stable Diffusion model
3. ✅ Generate images with one click
4. ✅ View images in browser
5. ✅ Access saved files with metadata
6. ✅ See all generation parameters
7. ✅ Reproduce any generation
8. ✅ Build image library

### Benefits:
- 🎯 Professional workflow
- 🎯 Complete metadata tracking
- 🎯 Reproducible results
- 🎯 Organized output
- 🎯 Easy sharing

---

**🎉 Full Image Generation Integration Complete!**

You now have a professional AI art generation workflow with complete metadata tracking and file organization!

