# 🚀 Quick Start Guide

## Start the App in 3 Steps

### 1️⃣ Install Dependencies
```bash
uv sync
```

### 2️⃣ Run the App
```bash
uv run streamlit run streamlit_app.py
```

**Or use the launcher (recommended):**
- Windows: Double-click `run_streamlit.bat`
- Mac/Linux: `./run_streamlit.sh`

**Note:** Always use `uv run` to ensure dependencies are available!

### 3️⃣ Create Your First Prompt

**In the Streamlit app:**
1. **Select** a template category (e.g., "Portrait")
2. **Choose** a style preset (e.g., "Cinematic")
3. **Fill** the required fields
4. **Click** "Generate Preview"
5. **Copy** your prompt!

---

## 📁 File Overview

| File | Purpose |
|------|---------|
| `streamlit_app.py` | Main Streamlit UI application |
| `prompt_temp.py` | 50+ templates, styles, presets |
| `test_streamlit_integration.py` | Test everything works |
| `demo_prompts.py` | See example outputs |
| `STREAMLIT_README.md` | Full documentation |

---

## 🎨 Quick Examples

### Run Tests
```bash
python test_streamlit_integration.py
```

### See Demo Prompts
```bash
python demo_prompts.py
```

### View All Templates
```bash
python prompt_temp.py
```

---

## 🎯 Template Categories

1. **Portrait** - Character portraits
2. **Landscape** - Scenic views
3. **Fantasy** - Magical scenes
4. **Sci-Fi** - Futuristic imagery
5. **Animal** - Wildlife photos
6. **Architecture** - Buildings
7. **Abstract** - Abstract art
8. **Food** - Food photography
9. **Character** - Character designs
10. **Product** - Product shots

**Each category has 5 template variations!**

---

## ⚙️ Generation Parameters

| Parameter | Range | Recommended |
|-----------|-------|-------------|
| Inference Steps | 10-100 | 25-30 |
| Guidance Scale | 1.0-20.0 | 7.0-8.0 |
| Image Size | Various | 512x512 |

---

## 💡 Pro Tips

✅ **DO:**
- Use style presets for consistency
- Combine lighting with time of day
- Add quality modifiers
- Use negative prompts

❌ **AVOID:**
- Too many conflicting styles
- Vague descriptions
- Contradictory terms

---

## 🆘 Help

**App won't start?**
```bash
pip install --upgrade streamlit
streamlit --version
```

**Import errors?**
```bash
python -c "import prompt_temp; print('OK')"
```

**Need help?**
- Read `STREAMLIT_README.md`
- Check `STREAMLIT_GUIDE.md`

---

## 🎨 Next Steps

After creating prompts:
1. ✅ Preview your prompt
2. ⚙️ Adjust parameters
3. 🎬 Generate images (coming soon)
4. 💾 Save favorites

---

**Ready to create amazing AI art! 🚀**

