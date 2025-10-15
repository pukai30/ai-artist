"""
Smoke-tests the generative-art stack:
1. Prints Python, PyTorch, and CUDA versions
2. Generates one 512 × 512 image with Stable Diffusion v1-5
3. Saves the PNG locally and reports inference latency
"""

import time
import platform
import torch
from diffusers import StableDiffusionPipeline

print("Python", platform.python_version())
print("PyTorch", torch.__version__, "| CUDA", torch.version.cuda)
print("GPU available:", torch.cuda.is_available())

# Load weights in bfloat16 for speed and VRAM savings
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.bfloat16
)
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Optional: compile UNet for extra speed (PyTorch ≥ 2.3)
if hasattr(torch, "compile"):
    pipe.unet = torch.compile(pipe.unet, mode="reduce-overhead")

prompt = "a watercolor fox in a misty forest, 4k illustration"

start = time.perf_counter()
image = pipe(prompt, num_inference_steps=25, guidance_scale=8.0).images[0]
latency = time.perf_counter() - start

out_path = "fox_forest.png"
image.save(out_path)
print(f"Saved {out_path} | Latency: {latency:.2f} s")