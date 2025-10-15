# 🚀 How to Run AI Artist - Dependency Guide

## The Issue

When running `streamlit run streamlit_app.py` directly, you might get:
```
ModuleNotFoundError: No module named 'diffusers'
```

This happens because Streamlit runs in your global Python environment, not the project's virtual environment.

---

## ✅ Solution: Use UV to Run

### Correct Command:
```bash
uv run streamlit run streamlit_app.py
```

**Why this works:**
- `uv run` ensures the command runs in the project's virtual environment
- All dependencies from `pyproject.toml` are available
- No manual activation needed

---

## 🔧 Alternative Solutions

### Option 1: Use UV (Recommended)
```bash
# Sync dependencies first (if not done)
uv sync

# Run the app
uv run streamlit run streamlit_app.py
```

### Option 2: Manual Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate

# Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -e .

# Run the app
streamlit run streamlit_app.py
```

### Option 3: Install Globally (Not Recommended)
```bash
pip install -e .
streamlit run streamlit_app.py
```

---

## 📝 Updated Launcher Scripts

I'll update the launcher scripts to use `uv run`:

### Windows (`run_streamlit.bat`):
```batch
@echo off
echo Starting AI Artist with UV...
uv run streamlit run streamlit_app.py
```

### Mac/Linux (`run_streamlit.sh`):
```bash
#!/bin/bash
echo "Starting AI Artist with UV..."
uv run streamlit run streamlit_app.py
```

---

## ✅ Quick Commands

### Start the App:
```bash
uv run streamlit run streamlit_app.py
```

### Test Components:
```bash
# Test templates
uv run python prompt_temp.py

# Test image generation
uv run python main.py

# Test metadata
uv run python test_metadata.py
```

---

## 🎯 The App is Now Running!

The app should now be accessible at:
- **http://localhost:8501** (or next available port)

Check your terminal for the exact URL.

---

## 💡 Pro Tips

1. **Always use `uv run`** for this project
2. **Dependencies are managed** by UV automatically
3. **No manual activation** needed
4. **Consistent environment** guaranteed

---

## 🆘 Troubleshooting

### If you still get import errors:
```bash
# Re-sync dependencies
uv sync

# Check UV is installed
uv --version

# If UV not installed:
pip install uv
```

### If app won't start:
```bash
# Check if streamlit is in dependencies
cat pyproject.toml | grep streamlit

# Should see: "streamlit>=1.28.0"
```

---

**🎉 The app is running with all dependencies available!**

Access it in your browser and start creating AI art!

