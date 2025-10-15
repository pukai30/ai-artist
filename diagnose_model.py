"""
Diagnostic script to test Stable Diffusion model loading
Run this to identify the specific issue preventing model loading
"""

import sys
import io

# Fix Windows console encoding
if sys.platform == 'win32':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    except:
        pass

import torch

print("="*80)
print("STABLE DIFFUSION MODEL LOADING DIAGNOSTIC")
print("="*80)
print()

# Test 1: Check Python version
print("✓ Test 1: Python Version")
print(f"   Python: {sys.version}")
print()

# Test 2: Check PyTorch
print("✓ Test 2: PyTorch Installation")
try:
    print(f"   Torch version: {torch.__version__}")
    print(f"   CUDA available: {torch.cuda.is_available()}")
    print(f"   CUDA version: {torch.version.cuda if torch.cuda.is_available() else 'N/A'}")
except Exception as e:
    print(f"   ❌ Error: {e}")
print()

# Test 3: Check Diffusers
print("✓ Test 3: Diffusers Library")
try:
    import diffusers
    print(f"   Diffusers version: {diffusers.__version__}")
except Exception as e:
    print(f"   ❌ Error: {e}")
    print("   Solution: uv pip install diffusers")
print()

# Test 4: Check Transformers
print("✓ Test 4: Transformers Library")
try:
    import transformers
    print(f"   Transformers version: {transformers.__version__}")
except Exception as e:
    print(f"   ❌ Error: {e}")
    print("   Solution: uv pip install transformers")
print()

# Test 5: Check disk space (cache location)
print("✓ Test 5: Model Cache Directory")
from pathlib import Path
import os

cache_dir = Path.home() / ".cache" / "huggingface"
print(f"   Cache location: {cache_dir}")
print(f"   Exists: {cache_dir.exists()}")

if cache_dir.exists():
    # Try to get size
    try:
        total_size = sum(f.stat().st_size for f in cache_dir.rglob('*') if f.is_file())
        print(f"   Cache size: {total_size / (1024**3):.2f} GB")
    except:
        print(f"   Cache size: Unable to calculate")
print()

# Test 6: Try loading the model
print("✓ Test 6: Attempting to Load Stable Diffusion Model")
print("   This may take several minutes on first run...")
print()

try:
    from diffusers import StableDiffusionPipeline
    
    print("   Step 1/3: Importing StableDiffusionPipeline - OK")
    
    print("   Step 2/3: Downloading/loading model (this may take a while)...")
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        dtype=torch.float32,
        safety_checker=None,
        requires_safety_checker=False
    )
    print("   Step 2/3: Model loaded - OK")
    
    print("   Step 3/3: Moving to CPU...")
    pipe = pipe.to("cpu")
    print("   Step 3/3: Moved to CPU - OK")
    
    print()
    print("="*80)
    print("✅ SUCCESS! Model loaded successfully!")
    print("="*80)
    print()
    print("The model is working. You can now:")
    print("1. Close this test")
    print("2. Restart the Streamlit app")
    print("3. Try loading the model in the UI")
    print()
    
except Exception as e:
    print()
    print("="*80)
    print("❌ FAILED TO LOAD MODEL")
    print("="*80)
    print()
    print(f"Error: {e}")
    print(f"Error type: {type(e).__name__}")
    print()
    print("Full traceback:")
    import traceback
    traceback.print_exc()
    print()
    print("="*80)
    print("SOLUTIONS:")
    print("="*80)
    print()
    
    error_str = str(e).lower()
    
    if "connection" in error_str or "timeout" in error_str:
        print("Network Issue Detected:")
        print("  - Check your internet connection")
        print("  - Try again (download will resume)")
        print("  - Use VPN if region-blocked")
        print()
    
    elif "memory" in error_str or "ram" in error_str:
        print("Memory Issue Detected:")
        print("  - Close other applications")
        print("  - Try smaller image size (512x512)")
        print("  - Restart computer to free RAM")
        print()
    
    elif "disk" in error_str or "space" in error_str:
        print("Disk Space Issue Detected:")
        print("  - Free up at least 5GB disk space")
        print("  - Clear huggingface cache if needed")
        print()
    
    else:
        print("Unknown Issue:")
        print("  - Share the error above for help")
        print("  - Try: uv sync")
        print("  - Try restarting the app")
        print()

print("="*80)

