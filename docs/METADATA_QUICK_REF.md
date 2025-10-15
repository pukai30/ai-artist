# ⚡ Metadata System - Quick Reference

## What Changed?

### ✅ Metadata Now Includes Template Inputs!

**Before:**
```json
{
  "prompt": "Full prompt...",
  "negative_prompt": "...",
  "seed": 42
}
```

**After:**
```json
{
  "prompt": "Full prompt...",
  "negative_prompt": "...",
  "seed": 42,
  "template_info": {
    "category": "Character",
    "inputs": {
      "character": "warrior princess",
      "pose": "dynamic action",
      "outfit": "ornate armor"
    },
    "style": "anime style",
    "lighting": "dramatic",
    "mood": "epic"
  }
}
```

---

## 📝 Template Inputs in Metadata

### Example: Character Template

**User fills in UI:**
- Character: "warrior princess"
- Pose: "dynamic action pose"
- Outfit: "ornate armor"
- Background: "fantasy castle"

**Saved in metadata:**
```json
"template_info": {
  "inputs": {
    "character": "warrior princess",
    "pose": "dynamic action pose",
    "outfit": "ornate armor",
    "background": "fantasy castle"
  }
}
```

**Why this matters:**
✅ Know exactly what inputs created this image
✅ Reproduce with same inputs
✅ Create variations easily
✅ Build template library

---

## 🔧 New Methods

### 1. Load Image with Metadata
```python
from main import ImageGenerator

image, metadata = ImageGenerator.load_image_with_metadata(
    "generated_images/20241009_123456_warrior.png"
)

# Access template inputs
inputs = metadata['template_info']['inputs']
print(inputs['character'])  # "warrior princess"
```

### 2. Get All Generated Images
```python
all_images = ImageGenerator.get_all_generated_images()

for img_info in all_images:
    print(img_info['template_category'])    # "Character"
    print(img_info['template_inputs'])      # {"character": "..."}
```

---

## 📊 Metadata in UI

Click "View Full Metadata" to see:

```
🎯 Template Information
Category: Character
Template: a {style} character design...

📝 User Inputs
Character: warrior princess
Pose: dynamic action pose
Outfit: ornate armor
Background: fantasy castle

🎨 Style Configuration
Style: anime style
Lighting: dramatic
Mood: epic
Camera: None
```

---

## 💡 Use Cases

### Recreate Similar:
1. Load metadata from good image
2. See all inputs used
3. Change one input
4. Generate variation

### Learn What Works:
1. Generate many images
2. Review metadata of best ones
3. See which inputs work
4. Build knowledge base

### Template Previews (Future):
1. Show example images for each template
2. Display inputs that created them
3. Help users choose templates

---

## 📁 File Output

Each generation creates:

```
20241009_123456_warrior_princess.png    ← Image + PNG metadata
20241009_123456_warrior_princess.json   ← Full metadata JSON
```

**JSON Contains:**
- Prompts
- Parameters
- Template info ← NEW!
- User inputs ← NEW!
- Style config ← NEW!

---

## ✅ Benefits

**Complete Tracking:**
- Know what created each image
- Reproduce anytime
- Learn from successes

**Better Organization:**
- Filter by template category
- Search by inputs
- Build collections

**Future-Ready:**
- Gallery with previews
- Template examples
- Input analytics

---

**🎉 Every image now has complete metadata including all template inputs!**

