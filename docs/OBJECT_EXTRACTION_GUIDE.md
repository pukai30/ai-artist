# 🎨 Object Extraction and Image Generation Guide

## Overview

A new feature that **extracts objects from existing images** and **generates new images** with those objects in different scenes using AI!

---

## 🎯 What It Does

### Complete Pipeline:

```
Input Image
    ↓
1. Extract Object (e.g., person, dog, car)
    ↓
2. Generate Description of Object
    ↓
3. Create New Scene with Object
    ↓
New Generated Image
```

### Example:

**Input:** Photo of a person  
**Extract:** The person  
**Describe:** "a young woman with long hair"  
**Generate:** That person in a fantasy forest  
**Output:** New AI-generated image!

---

## 📋 Features

### 1. **Object Segmentation (CLIPSeg)**
- Extract specific objects using text prompts
- "person", "dog", "car", "building", etc.
- Background removal
- Transparent PNG output

### 2. **Image Captioning (BLIP)**
- Automatically describe extracted objects
- Generate detailed descriptions
- Use for new prompts

### 3. **Image Generation (Stable Diffusion)**
- Create new scenes with extracted objects
- Apply different styles
- Custom backgrounds and contexts

---

## 🚀 Installation

### Install Additional Dependencies:

```bash
uv sync
```

This installs the new dependency: `sentencepiece` (required for BLIP)

---

## 📝 Usage Examples

### Example 1: Extract Person, New Scene

```python
from object_extraction_generator import ObjectExtractorAndGenerator

# Initialize
extractor = ObjectExtractorAndGenerator(device="cpu")

# Load models
extractor.load_all_models()

# Extract and generate
results = extractor.extract_and_generate(
    input_image_path="photo.jpg",
    object_to_extract="person",
    new_scene_description="a magical forest with glowing mushrooms",
    style="fantasy art, detailed, vibrant colors"
)

# Check results
if results['success']:
    print(f"Generated: {results['paths']['generated']}")
```

**Output:**
- `segmented_person.png` - Extracted person
- `generated_person_new_scene.png` - New image!
- `generated_person_new_scene.json` - Metadata

---

### Example 2: Extract Animal, Artistic Style

```python
results = extractor.extract_and_generate(
    input_image_path="dog_photo.jpg",
    object_to_extract="dog",
    new_scene_description="a serene beach at sunset",
    style="watercolor painting, soft colors, artistic"
)
```

**Result:** Your dog painted in watercolor on a beach!

---

### Example 3: Just Extract Object

```python
from object_extraction_generator import extract_object_only

# Just segment, no generation
segmented = extract_object_only(
    image_path="photo.jpg",
    object_name="person",
    output_path="person_only.png"
)
```

**Result:** Transparent PNG with just the person

---

### Example 4: Just Describe Image

```python
from object_extraction_generator import describe_image

description = describe_image("photo.jpg")
print(f"Image contains: {description}")
```

**Result:** AI-generated description of the image

---

## 🎨 Use Cases

### Use Case 1: Character in Different Settings
```
Extract: Person from vacation photo
Generate: Same person in...
  - Fantasy landscape
  - Sci-fi city
  - Historical setting
  - Artistic style
```

### Use Case 2: Product Placement
```
Extract: Product from catalog
Generate: Same product in...
  - Lifestyle setting
  - Different background
  - Artistic render
  - Different lighting
```

### Use Case 3: Pet in New Scenes
```
Extract: Your pet
Generate: Your pet in...
  - Different location
  - Artistic style
  - Fantasy scene
  - Professional portrait
```

### Use Case 4: Object Reimagining
```
Extract: Any object
Generate: That object...
  - Different art style
  - New environment
  - Enhanced details
  - Creative variations
```

---

## 🔧 API Reference

### Class: `ObjectExtractorAndGenerator`

#### Initialize:
```python
extractor = ObjectExtractorAndGenerator(device="cpu")
```

#### Load Models:
```python
extractor.load_all_models()
# Or load individually:
extractor.load_segmentation_model()
extractor.load_caption_model()
extractor.load_stable_diffusion()
```

#### Segment Object:
```python
segmented = extractor.segment_object(
    image=pil_image,
    object_prompt="person",
    threshold=0.4  # Segmentation sensitivity
)
```

#### Caption Image:
```python
description = extractor.caption_image(pil_image)
```

#### Generate from Description:
```python
generated, metadata = extractor.generate_from_description(
    description="a young woman",
    negative_prompt="blurry, low quality",
    style_modifier="fantasy art, detailed",
    num_inference_steps=25,
    guidance_scale=7.5,
    seed=42
)
```

#### Complete Pipeline:
```python
results = extractor.extract_and_generate(
    input_image_path="photo.jpg",
    object_to_extract="person",
    new_scene_description="magical forest",
    style="fantasy art",
    output_dir="extracted_generations",
    save_intermediate=True
)
```

---

## 📁 Output Structure

```
extracted_generations/
├── segmented_person.png           # Extracted object (transparent)
├── generated_person_new_scene.png # New generated image
└── generated_person_new_scene.json # Complete metadata
```

### Metadata Example:
```json
{
  "prompt": "fantasy art a young woman in a magical forest",
  "base_description": "a young woman",
  "style_modifier": "fantasy art",
  "object_extracted": "person",
  "new_scene": "a magical forest",
  "original_image": "photo.jpg",
  "generation_time": 45.67,
  ...
}
```

---

## 🎯 Standalone Functions

### Quick Extract:
```python
from object_extraction_generator import extract_object_only

segmented = extract_object_only(
    "photo.jpg", 
    "person", 
    "person_extracted.png"
)
```

### Quick Describe:
```python
from object_extraction_generator import describe_image

description = describe_image("photo.jpg")
```

### Quick Generate from Segmented:
```python
from object_extraction_generator import generate_from_extracted_object

generated = generate_from_extracted_object(
    "segmented_person.png",
    "a cyberpunk city",
    "digital art, neon"
)
```

---

## 💡 Tips & Best Practices

### For Best Segmentation:
- ✅ Clear, high-contrast objects
- ✅ Simple backgrounds
- ✅ Good lighting
- ✅ Use specific prompts ("person" better than "human figure")

### Object Prompts That Work Well:
- "person", "man", "woman", "child"
- "dog", "cat", "bird", "horse"
- "car", "building", "tree", "flower"
- "face", "hand", "hair"

### For Best Generation:
- ✅ Detailed scene descriptions
- ✅ Specific style modifiers
- ✅ Appropriate negative prompts
- ✅ Higher inference steps (25-30)

---

## 🧪 Testing

### Test the Feature:

```bash
# 1. Prepare an input image
# Copy any image to the project folder as "input_image.jpg"

# 2. Run the program
uv run python object_extraction_generator.py

# 3. Check output
# Look in extracted_generations/ folder
```

---

## 🎨 Creative Examples

### Example 1: Historical Figure in Modern Times
```python
results = extractor.extract_and_generate(
    input_image_path="old_photo.jpg",
    object_to_extract="person",
    new_scene_description="a modern coffee shop with laptop",
    style="photorealistic, modern photography"
)
```

### Example 2: Pet as Superhero
```python
results = extractor.extract_and_generate(
    input_image_path="pet.jpg",
    object_to_extract="dog",
    new_scene_description="flying over a city wearing a cape",
    style="comic book art, dynamic, heroic"
)
```

### Example 3: Product in Luxury Setting
```python
results = extractor.extract_and_generate(
    input_image_path="product.jpg",
    object_to_extract="watch",
    new_scene_description="on a marble pedestal with dramatic lighting",
    style="professional product photography, luxury"
)
```

---

## 🔮 Future Integration with Streamlit

Potential features to add to the UI:
- Upload image button
- Object selection dropdown
- Scene description field
- Style selector
- Before/after comparison
- Gallery of extracted generations

---

## 📊 Models Used

| Model | Purpose | Size |
|-------|---------|------|
| CLIPSeg | Object segmentation | ~350MB |
| BLIP | Image captioning | ~1GB |
| Stable Diffusion | Image generation | ~4GB |

**Total:** ~5.5GB models (downloaded on first use)

---

## Summary

### What You Get:
- ✅ Extract objects from images
- ✅ Automatic object description
- ✅ Generate new scenes with object
- ✅ Complete metadata tracking
- ✅ Flexible API
- ✅ Standalone functions

### Use Cases:
- 🎭 Character in different scenes
- 🐕 Pets in new environments
- 📦 Products in different contexts
- 🎨 Artistic reimagining
- 🔄 Style transfer with context

---

**🎉 New Feature Created: Object Extraction + Image Generation!**

Extract any object from an image and place it in entirely new scenes with AI!

