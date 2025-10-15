# 🎨 AI Artist - Stable Diffusion Image Generation

A professional AI image generation system with an intuitive Streamlit UI, 50+ prompt templates, context-aware parameters, and complete metadata tracking.

---

## ⚡ Quick Start

### 1. Install Dependencies
```bash
uv sync
```

### 2. Run the Application
```bash
uv run streamlit run streamlit_app.py
```

### 3. Create Amazing AI Art!
- Model loads automatically on startup
- Select templates and configure parameters
- Generate images with complete metadata
- All results saved in `generated_images/`

---

## ✨ Key Features

### 🎯 **50+ Professional Templates**
- 10 categories: Portrait, Landscape, Fantasy, Sci-Fi, Animal, Architecture, Abstract, Food, Character, Product
- 5 variations per category
- Context-aware dropdown suggestions (330+ options)

### 🎨 **Smart Parameter System**
- 14 style presets (Cinematic, Anime, Oil Painting, etc.)
- 10 lighting options (Dramatic, Natural, Neon, etc.)
- 10 mood options (Epic, Peaceful, Mysterious, etc.)
- 8 camera presets (Optional professional specs)

### 📊 **Complete Metadata Tracking**
- All template inputs saved
- Generation parameters preserved
- PNG embedded metadata + JSON sidecar
- Full reproducibility

### 🖼️ **Image Generation**
- Stable Diffusion integration
- Multiple image sizes (512x512 to 768x768)
- Batch generation (1-4 images)
- Real-time token counter

### 🔍 **Object Extraction (NEW!)**
- Extract objects from existing images
- AI-powered object description
- Generate new scenes with extracted objects
- Complete pipeline automation

---

## 📁 Project Structure

```
ai-artist/
├── streamlit_app.py              # Main Streamlit UI
├── main.py                        # ImageGenerator class
├── prompt_temp.py                 # Template library (50+ templates)
├── object_extraction_generator.py # Object extraction feature
├── img_gen.py                     # Simple test script
├── generated_images/              # Output directory
├── extracted_generations/         # Object extraction output
├── docs/                          # 📚 All documentation (37 guides)
│   ├── README.md                  # Documentation index
│   ├── QUICK_START.md             # Get started guide
│   ├── STREAMLIT_README.md        # Complete UI guide
│   ├── OBJECT_EXTRACTION_GUIDE.md # Object extraction guide
│   └── ... (33 more guides)
├── pyproject.toml                 # Dependencies
└── README.md                      # This file
```

---

## 📚 Documentation

**All documentation has been organized in the [`docs/`](docs/) folder.**

### Essential Guides:
- 🚀 **[Quick Start](docs/QUICK_START.md)** - Get started in 3 steps
- 📖 **[Streamlit Guide](docs/STREAMLIT_README.md)** - Complete UI documentation
- 🔧 **[Troubleshooting](docs/TROUBLESHOOTING_MODEL_LOAD.md)** - Fix common issues
- 🎯 **[Object Extraction](docs/OBJECT_EXTRACTION_QUICKSTART.md)** - Extract & regenerate objects

### Browse All Documentation:
See **[`docs/README.md`](docs/README.md)** for complete documentation index with 37 guides organized by topic.

---

## 🎯 Usage Examples

### Generate Image from Template:
```bash
# Start the app
uv run streamlit run streamlit_app.py

# In browser:
# 1. Wait for model to load (automatic)
# 2. Select template (e.g., "Fantasy")
# 3. Fill parameters with smart dropdowns
# 4. Generate preview (see token count)
# 5. Generate image
# 6. View results with complete metadata
```

### Extract Object and Regenerate:
```bash
# Run object extraction
uv run python object_extraction_generator.py

# Or use programmatically
```

---

## 🔧 Requirements

- **Python:** 3.12+
- **RAM:** 8GB+ recommended
- **Disk Space:** 6GB (for models)
- **Internet:** For first-time model downloads

---

## 💡 Features Highlight

- ✅ 50 prompt templates with placeholders
- ✅ 330+ context-aware dropdown options
- ✅ Automatic model loading on startup
- ✅ Real-time token counter
- ✅ Complete metadata system
- ✅ Smart file naming (timestamp + subject)
- ✅ Object extraction from images
- ✅ Professional UI (no sidebar, clean layout)
- ✅ User-friendly terminology
- ✅ Educational tooltips

---

## 🆘 Support

### Having Issues?
- Check [docs/TROUBLESHOOTING_MODEL_LOAD.md](docs/TROUBLESHOOTING_MODEL_LOAD.md)
- Run diagnostic: `uv run python diagnose_model.py`
- See [docs/WINDOWS_ENCODING_FIX.md](docs/WINDOWS_ENCODING_FIX.md) for encoding issues

### Want to Learn More?
- Browse all docs: [docs/README.md](docs/README.md)
- See complete features: [docs/FINAL_IMPLEMENTATION_SUMMARY.md](docs/FINAL_IMPLEMENTATION_SUMMARY.md)

---

## 🎨 What You Can Create

- 🎭 Character portraits in various styles
- 🏞️ Stunning landscapes
- 🐉 Fantasy scenes with creatures
- 🚀 Sci-fi and cyberpunk imagery
- 🦁 Wildlife photography
- 🏛️ Architectural visualizations
- 🎨 Abstract art
- 🍕 Food photography
- 👤 Character designs
- 📦 Product shots
- 🔄 Object extraction and scene transfer

---

## 🚀 Commands Cheat Sheet

```bash
# Start the app
uv run streamlit run streamlit_app.py

# Test image generation
uv run python img_gen.py

# Extract objects and generate
uv run python object_extraction_generator.py

# View templates
uv run python prompt_temp.py

# Test metadata
uv run python test_metadata.py

# Diagnose issues
uv run python diagnose_model.py
```

---

## 📊 Project Stats

- **Templates:** 50
- **Context-Aware Options:** 330+
- **Style Presets:** 14
- **Documentation Files:** 37
- **Lines of Code:** 3,500+
- **AI Models:** 4 (Stable Diffusion, CLIPSeg, BLIP, + components)

---

## 🎉 Credits

Built with:
- **Streamlit** - Web UI framework
- **Stable Diffusion** - Image generation
- **CLIPSeg** - Object segmentation
- **BLIP** - Image captioning
- **PyTorch** - Deep learning framework
- **HuggingFace** - Model hub

---

## 📝 License

Part of the AI Artist project.

---

**🎨 Start Creating Amazing AI Art!**

Run `uv run streamlit run streamlit_app.py` and let your creativity flow! ✨

