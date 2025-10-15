# ⚡ Object Extraction - Quick Start

## What This Does

**Extract objects from photos → Generate new images in different scenes!**

---

## 🚀 Quick Example

### Input:
- Photo of a person

### Process:
1. Extract the person
2. Describe: "a young woman with long hair"
3. Generate in new scene: "magical forest"

### Output:
- New AI image of that person in a magical forest!

---

## 📝 Simple Usage

### Step 1: Prepare Input Image

Copy an image to the project folder:
```
input_image.jpg  ← Your photo
```

### Step 2: Run the Program

```bash
uv run python object_extraction_generator.py
```

### Step 3: View Results

Check the `extracted_generations/` folder:
```
segmented_person.png           ← Extracted object
generated_person_new_scene.png ← New image!
```

---

## 🎨 Customize It

### Edit the Main Section (Bottom of file):

```python
# Line ~360 in object_extraction_generator.py

results = extractor.extract_and_generate(
    input_image_path="input_image.jpg",
    object_to_extract="person",  # ← Change: "dog", "cat", "car"
    new_scene_description="a futuristic cyberpunk city",  # ← Your scene
    style="digital art, highly detailed"  # ← Your style
)
```

---

## 💡 Object Types You Can Extract

**People:**
- "person", "man", "woman", "child", "face"

**Animals:**
- "dog", "cat", "bird", "horse", "fish"

**Objects:**
- "car", "building", "tree", "flower", "chair"

**Body Parts:**
- "face", "hand", "hair", "eyes"

---

## 🎯 Scene Ideas

**Fantasy:**
- "a magical forest with glowing mushrooms"
- "floating islands in the sky"
- "ancient castle at sunset"

**Sci-Fi:**
- "a futuristic cyberpunk city with neon lights"
- "a space station orbiting Earth"
- "holographic virtual reality world"

**Realistic:**
- "a professional photography studio"
- "a modern office with large windows"
- "a beach at golden hour"

**Artistic:**
- "an impressionist painting style garden"
- "a watercolor landscape"
- "abstract geometric background"

---

## 🔧 Workflow

```
1. Input: photo.jpg
   ↓
2. Extract: "person" → segmented_person.png
   ↓
3. Describe: AI generates → "a young woman wearing glasses"
   ↓
4. Generate: New image → person in magical forest
   ↓
5. Output: generated_person_new_scene.png
```

---

## 📊 Requirements

### Models Downloaded (First Run):
- CLIPSeg: ~350MB
- BLIP: ~1GB  
- Stable Diffusion: ~4GB

**Total:** ~5.5GB (one-time download)

### Time:
- Model loading: 3-5 minutes (first time)
- Extraction: 5-10 seconds
- Generation: 30-60 seconds (CPU)

---

## 🎨 Examples

### Extract Person → Fantasy Scene:
```python
object_to_extract="person"
new_scene_description="a magical enchanted forest"
style="fantasy art, detailed, mystical"
```

### Extract Dog → Beach Scene:
```python
object_to_extract="dog"
new_scene_description="a tropical beach at sunset"
style="photorealistic, golden hour lighting"
```

### Extract Car → Futuristic City:
```python
object_to_extract="car"
new_scene_description="a cyberpunk city street with neon signs"
style="digital art, cinematic, sci-fi"
```

---

## 📁 Files Created

### New File:
- `object_extraction_generator.py` - Main program

### Output Folder:
- `extracted_generations/` - Results stored here

### Dependencies:
- Updated `pyproject.toml` with `sentencepiece`

---

## 🚀 Quick Commands

### Run with Default Settings:
```bash
uv run python object_extraction_generator.py
```

### Just Extract Object:
```python
from object_extraction_generator import extract_object_only

extract_object_only("photo.jpg", "person", "person_only.png")
```

### Just Get Description:
```python
from object_extraction_generator import describe_image

desc = describe_image("photo.jpg")
print(desc)
```

---

## 💡 Pro Tips

1. **Use clear photos** - Better extraction
2. **Be specific** - "person" better than "human"
3. **Detailed scenes** - More context = better results
4. **Try different styles** - Photorealistic, artistic, etc.
5. **Save good results** - Metadata helps recreate

---

## 🎯 Next Steps

1. **Place input image** in project folder
2. **Run:** `uv run python object_extraction_generator.py`
3. **Check:** `extracted_generations/` for results
4. **Customize:** Edit script for your needs

---

**🎨 Start Extracting Objects and Creating New Scenes!** ✨

