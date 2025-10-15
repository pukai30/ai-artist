# 🔧 Force Reinstall - Fix Locked Files

## Issue

**Error:** `The process cannot access the file because it is being used by another process. (os error 32)`

**Cause:** Python process still running, locking the files

---

## ✅ Complete Solution

### Step 1: Close EVERYTHING

**Close these:**
- ✅ All terminal windows
- ✅ VSCode (completely close, not just the file)
- ✅ Any Python processes
- ✅ Task Manager → End any `python.exe` or `streamlit.exe`

**Windows Task Manager:**
```
1. Press Ctrl+Shift+Esc
2. Find any "python.exe" or "streamlit.exe" processes
3. Right-click → End Task
4. Make sure all are closed
```

---

### Step 2: Delete and Recreate Environment

**Open NEW PowerShell as Administrator:**

```powershell
cd F:\Projects\AI\ProjectsForDemo\ai-artist

# Remove the virtual environment
Remove-Item -Recurse -Force .venv

# Sync again (creates new environment)
uv sync

# Should complete successfully now
```

---

### Step 3: Test Model Loading

```bash
uv run python img_gen.py
```

---

## 🚀 Quick Alternative: Use pip in New Environment

If UV keeps having issues:

```bash
# Create venv with Python
python -m venv .venv

# Activate
.venv\Scripts\activate

# Install manually with compatible versions
pip install torch torchvision torchaudio
pip install "diffusers[torch]>=0.35.1"
pip install "transformers>=4.21.0,<4.48.0"
pip install "accelerate>=1.10.1,<2.0.0"
pip install streamlit pillow

# Test
python img_gen.py

# Run app
streamlit run streamlit_app.py
```

---

## 🎯 Recommended Steps (In Order)

### Option 1: Kill Processes + Clean Reinstall

```powershell
# 1. Close VSCode completely

# 2. Open Task Manager (Ctrl+Shift+Esc)
#    End all python.exe and streamlit.exe processes

# 3. Open new PowerShell
cd F:\Projects\AI\ProjectsForDemo\ai-artist

# 4. Delete .venv
Remove-Item -Recurse -Force .venv

# 5. Sync
uv sync

# 6. Test
uv run python img_gen.py
```

### Option 2: Restart Computer

Sometimes easiest:
```
1. Save your work
2. Restart computer
3. Open PowerShell
4. cd to project
5. uv sync
6. uv run python img_gen.py
```

---

## 📝 Files to Check

After successful `uv sync`, verify:

```bash
# Check transformers version
uv run python -c "import transformers; print(transformers.__version__)"

# Should show: 4.47.x or similar (NOT 4.48.x or higher)

# Check accelerate version  
uv run python -c "import accelerate; print(accelerate.__version__)"

# Should show: 1.x.x (NOT 2.x.x)
```

---

## 🎨 After Success

Once `uv sync` completes and versions are correct:

```bash
# Test model loading
uv run python img_gen.py

# If that works, run Streamlit
uv run streamlit run streamlit_app.py
```

---

## 💡 Why This Happens

**The `offload_state_dict` Error:**
- New `transformers` 4.48+ changed internal APIs
- Old `accelerate` 1.x or new `diffusers` not updated yet
- Incompatible → crash

**The Fix:**
- Pin `transformers` to < 4.48.0
- Pin `accelerate` to < 2.0.0
- Compatible versions work together

---

## ✅ Summary

**To fix:**
1. Close ALL Python processes (check Task Manager)
2. Delete `.venv` folder
3. Run `uv sync`
4. Test with `img_gen.py`
5. Run Streamlit app

**The version constraints are already set in `pyproject.toml`** - you just need to reinstall cleanly.

---

**Close everything, delete `.venv`, and run `uv sync` in a fresh terminal!** 🔧✨

