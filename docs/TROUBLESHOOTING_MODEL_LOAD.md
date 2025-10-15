# 🔧 Troubleshooting: Model Loading Issues

## Issue: "Failed to load model"

If you're seeing this error, here are solutions:

---

## ✅ Quick Fixes (Try These First)

### 1. Check Terminal/Console for Details
The error details are printed in the terminal where you ran the app.

Look for:
```
❌ Error loading pipeline: [detailed error message]
Error type: [error type]
Traceback: [full traceback]
```

### 2. Common Issues & Solutions

#### Issue: `torch_dtype` deprecation
**Error:** `'torch_dtype' is deprecated! Use 'dtype' instead!`

**✅ FIXED:** Already updated to use `dtype` instead

**Action:** Restart the app to use the fixed code

---

#### Issue: Network/Download Error
**Error:** Connection timeout, download failed

**Solutions:**
- Check internet connection
- Try again (download resumes)
- Use VPN if region-blocked
- Wait for better network

---

#### Issue: Out of Memory
**Error:** CUDA out of memory, CPU RAM insufficient

**Solutions:**
```python
# Try smaller model (not recommended)
# Or reduce image size in UI to 512x512
```

**System Requirements:**
- RAM: 8GB+ recommended
- Disk Space: 5GB+ for model cache
- Internet: For first-time download

---

#### Issue: Missing Dependencies
**Error:** No module named 'transformers', 'accelerate', etc.

**Solution:**
```bash
# Re-sync dependencies
uv sync

# Or manually install
uv pip install diffusers transformers accelerate
```

---

## 🧪 Diagnostic Steps

### Step 1: Check Python & Torch
```bash
uv run python -c "import torch; print(f'Torch: {torch.__version__}')"
```

Expected output:
```
Torch: 2.8.0+cpu
```

### Step 2: Check Diffusers
```bash
uv run python -c "import diffusers; print(f'Diffusers: {diffusers.__version__}')"
```

Expected output:
```
Diffusers: 0.35.1
```

### Step 3: Test Model Loading Directly
```bash
uv run python main.py
```

This will:
- Show detailed error messages
- Display full traceback
- Test model loading in isolation

### Step 4: Check Disk Space
```bash
# Windows
dir %USERPROFILE%\.cache\huggingface

# Mac/Linux
ls -lh ~/.cache/huggingface
```

Model cache needs ~4-5GB free space.

---

## 🔄 Alternative: Use Lighter Model

If the main model won't load, try a smaller one:

**Update `streamlit_app.py` line 588:**
```python
# Instead of default model, try:
st.session_state.generator = ImageGenerator(
    model_name="CompVis/stable-diffusion-v1-4",  # Slightly smaller
    device="cpu"
)
```

Or even smaller test model:
```python
st.session_state.generator = ImageGenerator(
    model_name="hf-internal-testing/tiny-stable-diffusion-torch",  # Tiny test model
    device="cpu"
)
```

---

## 🐛 Debug Mode

Add debug output to see exactly where it fails:

**Create `test_load.py`:**
```python
import torch
from diffusers import StableDiffusionPipeline

print("Step 1: Importing libraries - OK")
print(f"Torch version: {torch.__version__}")

print("\nStep 2: Attempting to load model...")
try:
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        dtype=torch.float32,
        safety_checker=None,
        requires_safety_checker=False
    )
    print("Step 3: Model downloaded/loaded - OK")
    
    pipe = pipe.to("cpu")
    print("Step 4: Model moved to CPU - OK")
    
    print("\n✅ SUCCESS! Model loaded.")
    
except Exception as e:
    print(f"\n❌ FAILED at some step")
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
```

**Run:**
```bash
uv run python test_load.py
```

---

## 💾 Check Model Cache

### View cached models:
```bash
# Windows
dir %USERPROFILE%\.cache\huggingface\hub

# Mac/Linux  
ls ~/.cache/huggingface/hub
```

### Clear cache and retry:
```bash
# Windows
rmdir /s %USERPROFILE%\.cache\huggingface

# Mac/Linux
rm -rf ~/.cache/huggingface
```

Then try loading again (will re-download).

---

## 🔍 Check Error in Terminal

**Look at your terminal output** where you ran `uv run streamlit run streamlit_app.py`

You should see detailed error messages like:
```
❌ Error loading pipeline: [specific error]
Error type: RuntimeError
Traceback: [full stack trace]
```

**Common Error Messages:**

### Error: "No space left on device"
**Solution:** Free up disk space (need 5GB+)

### Error: "Connection timeout"
**Solution:** Check internet, try again

### Error: "OSError: Can't load tokenizer"
**Solution:** Install transformers: `uv pip install transformers`

### Error: "CUDA out of memory"
**Solution:** Already using CPU, reduce image size

---

## 🆘 Emergency Fallback

If nothing works, use a mock generator for testing UI:

**Create `mock_generator.py`:**
```python
from PIL import Image
import numpy as np
import time

class MockImageGenerator:
    def __init__(self, *args, **kwargs):
        self.is_loaded = False
    
    def load_model(self):
        time.sleep(1)  # Simulate loading
        self.is_loaded = True
        return True
    
    def generate_image(self, prompt, **kwargs):
        # Create random test image
        img_array = np.random.randint(0, 255, (512, 512, 3), dtype=np.uint8)
        image = Image.fromarray(img_array)
        
        metadata = {
            "prompt": prompt,
            "test_mode": True,
            **kwargs
        }
        
        return [image], metadata
```

**Update streamlit_app.py temporarily:**
```python
# Line 10
from mock_generator import MockImageGenerator as ImageGenerator
```

This lets you test the UI while debugging the real model.

---

## 📝 What to Share for Help

If you need further assistance, share:

1. **Error message from terminal** (full traceback)
2. **System info:**
   ```bash
   uv run python -c "import torch; import sys; print(f'Python: {sys.version}'); print(f'Torch: {torch.__version__}')"
   ```
3. **Disk space:**
   ```bash
   # Windows: Check C: drive
   # Mac/Linux: df -h
   ```
4. **Internet status:** Can you download from huggingface.co?

---

## 🎯 Next Steps

1. **Check terminal output** for detailed error
2. **Try diagnostic steps** above
3. **Share error details** if you need help
4. **Consider lighter model** as temporary solution

---

**The app is updated with better error handling. Try loading the model again and check the terminal for specific error details!** 🔧

