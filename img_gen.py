import sys
import torch
import time
import torchvision
import torchaudio
import transformers
import gradio
import diffusers
import datasets
import peft
import accelerate
import tqdm
import scipy
from PIL import Image
from diffusers import StableDiffusionPipeline

print(f"torch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")

# Try a simpler approach with CPU-only generation for now
print("Loading Stable Diffusion pipeline...")
try:
    # Load with minimal options to avoid version conflicts
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float32,
        safety_checker=None,
        requires_safety_checker=False,
        low_cpu_mem_usage=False  # Disable to avoid accelerate issues
    )
    pipe = pipe.to("cpu")
    print("Pipeline loaded successfully!")
except Exception as e:
    print(f"Error loading pipeline: {e}")
    print("Falling back to a simple test...")
    # Create a simple test instead
    import numpy as np
    test_image = np.random.randint(0, 255, (512, 512, 3), dtype=np.uint8)
    from PIL import Image
    img = Image.fromarray(test_image)
    img.save("output.png")
    print("Generated test image instead")
    exit()

# Skip torch.compile as it requires C++ compiler
# if hasattr(torch, "compile"):
#     pipe.unet = torch.compile(pipe.unet, mode="reduce-overhead")

stng = "surreal landscape, pastel colors, low-poly"

prompt = "a watercolor of a child riding a horse in a misty forest"
#  prompt = stng
start = time.perf_counter()
seed = 123
image = pipe(prompt, num_inference_steps=16, guidance_scale=8.0, seed=seed).images[0]
latency = time.perf_counter() - start
print(f"Time taken: {latency} seconds")
image.save("output1.png")