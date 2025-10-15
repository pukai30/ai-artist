# 📋 Metadata System - Complete Guide

## Overview

The AI Artist now has a **comprehensive metadata system** that tracks all template inputs, generation parameters, and user selections for every generated image.

---

## What's Included in Metadata

### 1. **Generation Parameters**
```json
{
  "prompt": "Full generated prompt...",
  "negative_prompt": "Full negative prompt...",
  "num_inference_steps": 25,
  "guidance_scale": 7.5,
  "seed": 42,
  "width": 512,
  "height": 512,
  "num_images": 1,
  "generation_time": 45.23,
  "model": "runwayml/stable-diffusion-v1-5",
  "device": "cpu",
  "timestamp": "2024-10-09T12:34:56.789123"
}
```

### 2. **Template Information** (NEW!)
```json
{
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
    "camera_details": "50mm lens, f/1.8, shallow depth of field",
    "negative_prompt_type": "artistic"
  }
}
```

---

## Metadata Structure Breakdown

### Template Info Fields:

| Field | Description | Example |
|-------|-------------|---------|
| `category` | Template category selected | "Character", "Animal", "Landscape" |
| `template` | Actual template string | "a {style} portrait of {subject}" |
| `template_index` | Which template variation (0-4) | 2 |
| `inputs` | User-provided field values | `{"subject": "warrior", "pose": "heroic"}` |
| `style` | Style configuration | "digital art, concept art, detailed" |
| `lighting` | Lighting configuration | "dramatic side lighting" |
| `mood` | Mood/atmosphere | "epic and mysterious" |
| `camera_details` | Camera specs (if used) | "85mm lens, f/2.8" or null |
| `negative_prompt_type` | Type of negative prompt | "general", "portrait", etc. |

---

## File Storage

### Files Created for Each Image:

1. **PNG File** (with embedded metadata)
   ```
   20241009_123456_warrior_princess.png
   ```
   - Contains the actual image
   - PNG metadata embedded in file
   - Can be shared with metadata intact

2. **JSON Sidecar File** (complete metadata)
   ```
   20241009_123456_warrior_princess.json
   ```
   - Complete metadata in JSON format
   - Easy to read and parse
   - Used for loading image previews

---

## Example Metadata Files

### Character Template Example:

**File:** `20241009_123456_warrior_princess.json`

```json
{
  "prompt": "a anime style, cel shaded, vibrant colors character design of warrior princess, dynamic action pose, ornate armor with flowing cape, fantasy castle ruins, detailed, vibrant colors, 4k",
  "negative_prompt": "photograph, photo, realistic, photorealistic, blurry, low quality, bad quality, watermark, signature, username, text, ugly, distorted, bad composition, messy",
  "num_inference_steps": 30,
  "guidance_scale": 7.5,
  "seed": 42,
  "width": 512,
  "height": 512,
  "num_images": 1,
  "generation_time": 45.67,
  "model": "runwayml/stable-diffusion-v1-5",
  "device": "cpu",
  "timestamp": "2024-10-09T12:34:56.123456",
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

### Animal Template Example:

**File:** `20241009_140512_tiger_jungle.json`

```json
{
  "prompt": "majestic tiger with piercing eyes and powerful build, dense jungle, dramatic side lighting, wildlife photography, 8k, highly detailed",
  "negative_prompt": "cartoon, anime, drawing, painting, sketch, low quality, worst quality, blurry, watermark, text, logo, signature, username, artificial, bad anatomy, distorted, oversaturated",
  "num_inference_steps": 25,
  "guidance_scale": 7.5,
  "seed": 100,
  "width": 768,
  "height": 512,
  "num_images": 1,
  "generation_time": 52.34,
  "model": "runwayml/stable-diffusion-v1-5",
  "device": "cpu",
  "timestamp": "2024-10-09T14:05:12.456789",
  "template_info": {
    "category": "Animal",
    "template": "majestic {animal} with {features}, {habitat}, {lighting}, {quality}",
    "template_index": 2,
    "inputs": {
      "animal": "tiger",
      "features": "piercing eyes and powerful build",
      "habitat": "dense jungle",
      "quality": "wildlife photography, 8k, highly detailed"
    },
    "style": "hyperrealistic, photorealistic, highly detailed",
    "lighting": "dramatic side lighting",
    "mood": "intense",
    "camera_details": "200mm lens, f/5.6, telephoto",
    "negative_prompt_type": "realistic"
  }
}
```

---

## New Methods in ImageGenerator

### 1. `load_image_with_metadata(filepath)`

**Purpose:** Load a saved image with its complete metadata

**Usage:**
```python
from main import ImageGenerator

image, metadata = ImageGenerator.load_image_with_metadata(
    "generated_images/20241009_123456_warrior.png"
)

if image and metadata:
    print(f"Loaded: {metadata['prompt']}")
    print(f"Template: {metadata['template_info']['category']}")
    print(f"Inputs: {metadata['template_info']['inputs']}")
```

**Returns:**
- `image`: PIL Image object
- `metadata`: Complete metadata dict

**Features:**
- ✅ Tries JSON sidecar first (most complete)
- ✅ Falls back to PNG embedded metadata
- ✅ Returns None if file not found
- ✅ Error handling built-in

---

### 2. `get_all_generated_images(output_dir)`

**Purpose:** Get all generated images with metadata

**Usage:**
```python
from main import ImageGenerator

all_images = ImageGenerator.get_all_generated_images()

for img_info in all_images:
    print(f"File: {img_info['filepath']}")
    print(f"Category: {img_info['template_category']}")
    print(f"Inputs: {img_info['template_inputs']}")
    print(f"Image: {img_info['image']}")
```

**Returns:**
List of dicts with:
- `filepath`: Path to image file
- `image`: PIL Image object
- `metadata`: Complete metadata
- `timestamp`: Generation timestamp
- `template_category`: Template category used
- `template_inputs`: User input values

**Features:**
- ✅ Sorted by newest first
- ✅ Only returns valid images
- ✅ Extracts template info
- ✅ Ready for gallery/preview features

---

## Benefits of Template Input Tracking

### 1. **Reproducibility**
```json
"inputs": {
  "character": "warrior princess",
  "pose": "dynamic action pose",
  "outfit": "ornate armor"
}
```
- Know exactly what inputs created this image
- Recreate similar images
- Share successful combinations

### 2. **Learning & Improvement**
- See which inputs produce best results
- Build library of successful combinations
- Learn what works for each category

### 3. **Sample Image Previews** (Future)
- Filter by template category
- Show examples for each template
- Help users choose templates
- Display similar images

### 4. **Batch Processing** (Future)
- Regenerate with variations
- Apply same inputs to different templates
- Create series of images

---

## In Streamlit UI

### Metadata Display:

When you generate an image and click "View Full Metadata":

```
┌─────────────────────────────────────────────┐
│ 📋 View Full Metadata                      │
├─────────────────────────────────────────────┤
│ 🎯 Template Information                    │
│ Category: Character                        │
│ Template: a {style} character design...    │
│                                            │
│ 📝 User Inputs                             │
│ Character: warrior princess                │
│ Pose: dynamic action pose                  │
│ Outfit: ornate armor with flowing cape     │
│ Background: fantasy castle ruins           │
│ Quality: detailed, vibrant colors, 4k      │
│                                            │
│ 🎨 Style Configuration                     │
│ Style: anime style, cel shaded...          │
│ Lighting: dramatic side lighting           │
│ Mood: epic                                 │
│ Camera: 50mm lens, f/1.8...                │
│ Negative Type: artistic                    │
│                                            │
│ ⚙️ Complete Metadata                       │
│ [Full JSON display]                        │
└─────────────────────────────────────────────┘
```

---

## Use Cases

### Use Case 1: Recreate Similar Image
1. Load metadata from successful image
2. Copy template inputs
3. Change one parameter (e.g., different character)
4. Generate new variant

### Use Case 2: Build Template Library
1. Generate images from different templates
2. Review metadata to see which templates work best
3. Create collection of favorite combinations
4. Share templates with inputs

### Use Case 3: Sample Previews (Future Feature)
1. Filter images by template category
2. Show 3-5 examples for each template
3. Display inputs used
4. Help users choose templates

### Use Case 4: Batch Variations
1. Load successful image metadata
2. Keep all inputs except one
3. Generate variations (e.g., different poses)
4. Create image series

---

## API Examples

### Save with Template Info:

```python
from main import ImageGenerator

generator = ImageGenerator()
generator.load_model()

template_info = {
    "category": "Animal",
    "template": "majestic {animal} with {features}",
    "inputs": {
        "animal": "tiger",
        "features": "piercing eyes"
    },
    "style": "realistic",
    "lighting": "natural",
    "mood": "intense",
    "camera_details": None,
    "negative_prompt_type": "realistic"
}

images, metadata = generator.generate_image(
    prompt="majestic tiger with piercing eyes",
    template_info=template_info  # ← Include template info
)

filepath = generator.save_image_with_metadata(images[0], metadata)
```

### Load and Inspect:

```python
from main import ImageGenerator

# Load specific image
image, metadata = ImageGenerator.load_image_with_metadata(
    "generated_images/20241009_123456_tiger.png"
)

# Access template info
template_info = metadata['template_info']
print(f"Category: {template_info['category']}")
print(f"Inputs used:")
for key, value in template_info['inputs'].items():
    print(f"  {key}: {value}")
```

### Load All Images:

```python
from main import ImageGenerator

all_images = ImageGenerator.get_all_generated_images()

# Filter by category
animal_images = [
    img for img in all_images 
    if img['template_category'] == 'Animal'
]

print(f"Found {len(animal_images)} animal images")

# Display inputs from first animal image
if animal_images:
    inputs = animal_images[0]['template_inputs']
    print(f"Example inputs: {inputs}")
```

---

## Testing

### Test Metadata System:

```bash
python test_metadata.py
```

**Output:**
```
📁 Checking for generated images...
   Found 3 PNG files
   Found 3 JSON files

📋 Loading metadata from most recent image...
   ✅ Successfully loaded!
   
   🎯 Template Information:
      Category: Character
      Template: a {style} character design...
      
   📝 User Inputs:
      Character: warrior princess
      Pose: dynamic action pose
      Outfit: ornate armor
      
   🎨 Style Configuration:
      Style: anime style...
      Lighting: dramatic side lighting
      Mood: epic
```

---

## Future Features Enabled

With template input metadata, you can now build:

### 1. **Image Gallery with Filters**
```python
# Show all Character images
character_images = [img for img in all_images 
                   if img['template_category'] == 'Character']

# Show all images with specific input
warrior_images = [img for img in all_images
                 if 'warrior' in str(img['template_inputs'].get('character', ''))]
```

### 2. **Template Previews**
```python
# Get examples for each template
def get_template_examples(category, template_idx):
    return [img for img in all_images
           if img['metadata']['template_info']['category'] == category
           and img['metadata']['template_info']['template_index'] == template_idx]
```

### 3. **Input Suggestions**
```python
# Find popular inputs for a field
def get_popular_inputs(category, field_name):
    inputs = [img['template_inputs'].get(field_name)
             for img in all_images
             if img['template_category'] == category]
    return list(set(inputs))  # Unique values used
```

### 4. **Prompt Analytics**
```python
# Which templates generate fastest?
# Which inputs produce best results?
# What parameter combinations work well?
```

---

## Benefits Summary

### ✅ Complete Tracking
- Every parameter saved
- Template inputs preserved
- Style configurations recorded
- Generation settings stored

### ✅ Reproducibility
- Exact inputs available
- Can recreate any image
- Share successful formulas
- Build on what works

### ✅ Learning & Improvement
- See what inputs work best
- Analyze successful generations
- Build expertise over time
- Share knowledge

### ✅ Future-Ready
- Foundation for gallery
- Enables filtering/searching
- Template preview system
- Advanced analytics

---

## Metadata in UI

### In Streamlit App:

After generating an image, click **"View Full Metadata"**:

**Section 1: Template Information**
- Shows category and template used

**Section 2: User Inputs**
- All field values you entered
- Displayed in 2-column layout
- Easy to read and copy

**Section 3: Style Configuration**
- Style, Lighting, Mood selections
- Camera details if used
- Negative prompt type

**Section 4: Complete Metadata**
- Full JSON for advanced users
- Everything in one place

---

## Example Workflow

### Creating and Using Metadata:

1. **Create Image in UI**
   - Select "Character" template
   - Fill inputs: character="mage", pose="casting spell"
   - Generate image

2. **Image Saved With:**
   ```
   generated_images/
   ├── 20241009_143022_mage.png     ← Image + PNG metadata
   └── 20241009_143022_mage.json    ← Complete metadata
   ```

3. **Load Later:**
   ```python
   image, meta = ImageGenerator.load_image_with_metadata(
       "generated_images/20241009_143022_mage.png"
   )
   
   # See what inputs created this
   inputs = meta['template_info']['inputs']
   print(f"Character was: {inputs['character']}")
   print(f"Pose was: {inputs['pose']}")
   ```

4. **Create Variation:**
   - Use same inputs but change pose
   - Generate new image in same style
   - Build character set

---

## Code Reference

### Files Modified:

| File | Changes |
|------|---------|
| `main.py` | Added `template_info` parameter to `generate_image()` |
| `main.py` | Added `load_image_with_metadata()` method |
| `main.py` | Added `get_all_generated_images()` method |
| `streamlit_app.py` | Collect and pass template_info during generation |
| `streamlit_app.py` | Display template inputs in metadata viewer |

---

## Summary

### What You Can Do:

✅ **Track Everything**
- All inputs saved
- Complete reproduction possible
- Nothing lost

✅ **Load Any Image**
- With full metadata
- See exact inputs used
- Understand generation

✅ **Build Library**
- Filter by category
- Search by inputs
- Analyze results

✅ **Enable Future Features**
- Gallery with previews
- Template examples
- Input suggestions
- Analytics dashboard

---

**🎉 Complete Metadata System Active!**

Every generated image now contains comprehensive metadata including all template inputs, making it easy to reproduce, learn from, and build upon your successful generations!

