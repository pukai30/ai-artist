"""
Example Usage of Prompt Templates with Stable Diffusion
Demonstrates how to use prompt_temp.py with the diffusion model
"""

import torch
import time
from diffusers import StableDiffusionPipeline
from PIL import Image
import prompt_temp

# Load the pipeline (similar to main.py)
print("Loading Stable Diffusion pipeline...")
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float32,
    safety_checker=None,
    requires_safety_checker=False
)
pipe = pipe.to("cpu")
print("Pipeline loaded successfully!")

# ============================================================================
# Example 1: Using a pre-defined example
# ============================================================================
print("\n" + "="*80)
print("EXAMPLE 1: Using Pre-defined Example")
print("="*80)

example = prompt_temp.EXAMPLE_PROMPTS[0]  # Fantasy Dragon Portrait
prompt = prompt_temp.format_prompt(example["template"], **example["params"])
negative_prompt = example["negative"]

print(f"\nPrompt: {prompt}")
print(f"\nNegative Prompt: {negative_prompt[:100]}...")

start = time.perf_counter()
image = pipe(
    prompt=prompt,
    negative_prompt=negative_prompt,
    num_inference_steps=25,
    guidance_scale=7.5,
    generator=torch.Generator().manual_seed(42)
).images[0]
latency = time.perf_counter() - start

image.save("example_1_dragon.png")
print(f"\nGenerated image saved as 'example_1_dragon.png'")
print(f"Time taken: {latency:.2f} seconds")

# ============================================================================
# Example 2: Creating a custom portrait
# ============================================================================
print("\n" + "="*80)
print("EXAMPLE 2: Custom Portrait")
print("="*80)

portrait_template = prompt_temp.PORTRAIT_TEMPLATES[0]
custom_params = {
    "style": "cinematic",
    "subject": "an elderly man with weathered features",
    "lighting": "dramatic side lighting",
    "quality": "masterpiece, 8k, ultra detailed, sharp focus",
    "camera_details": "85mm lens, f/1.8, shallow depth of field"
}

prompt = prompt_temp.format_prompt(portrait_template, **custom_params)
negative_prompt = prompt_temp.NEGATIVE_PROMPTS["portrait"]

print(f"\nPrompt: {prompt}")

start = time.perf_counter()
image = pipe(
    prompt=prompt,
    negative_prompt=negative_prompt,
    num_inference_steps=25,
    guidance_scale=8.0,
    generator=torch.Generator().manual_seed(123)
).images[0]
latency = time.perf_counter() - start

image.save("example_2_portrait.png")
print(f"\nGenerated image saved as 'example_2_portrait.png'")
print(f"Time taken: {latency:.2f} seconds")

# ============================================================================
# Example 3: Random landscape with style preset
# ============================================================================
print("\n" + "="*80)
print("EXAMPLE 3: Landscape with Style Preset")
print("="*80)

landscape_template = prompt_temp.LANDSCAPE_TEMPLATES[1]
landscape_params = {
    "location": "alpine meadow with wildflowers",
    "style": prompt_temp.STYLES["oil_painting"],
    "season": "spring",
    "mood": "peaceful and serene",
    "quality": prompt_temp.QUALITY_MODIFIERS[0]
}

prompt = prompt_temp.format_prompt(landscape_template, **landscape_params)
negative_prompt = prompt_temp.NEGATIVE_PROMPTS["landscape"]

print(f"\nPrompt: {prompt}")

start = time.perf_counter()
image = pipe(
    prompt=prompt,
    negative_prompt=negative_prompt,
    num_inference_steps=30,
    guidance_scale=7.0,
    generator=torch.Generator().manual_seed(456)
).images[0]
latency = time.perf_counter() - start

image.save("example_3_landscape.png")
print(f"\nGenerated image saved as 'example_3_landscape.png'")
print(f"Time taken: {latency:.2f} seconds")

# ============================================================================
# Example 4: Batch generation with different parameters
# ============================================================================
print("\n" + "="*80)
print("EXAMPLE 4: Batch Generation with Variations")
print("="*80)

animals = ["tiger", "eagle", "wolf", "dolphin"]
template = prompt_temp.ANIMAL_TEMPLATES[2]

for i, animal in enumerate(animals):
    params = {
        "animal": animal,
        "features": "intense gaze",
        "habitat": "natural environment",
        "lighting": prompt_temp.LIGHTING_OPTIONS[4],  # natural lighting
        "quality": "wildlife photography, 8k, highly detailed"
    }
    
    prompt = prompt_temp.format_prompt(template, **params)
    print(f"\n{i+1}. Generating {animal}...")
    print(f"   Prompt: {prompt}")
    
    start = time.perf_counter()
    image = pipe(
        prompt=prompt,
        negative_prompt=prompt_temp.NEGATIVE_PROMPTS["realistic"],
        num_inference_steps=20,
        guidance_scale=7.5,
        generator=torch.Generator().manual_seed(100 + i)
    ).images[0]
    latency = time.perf_counter() - start
    
    filename = f"example_4_{animal}.png"
    image.save(filename)
    print(f"   Saved as '{filename}' ({latency:.2f}s)")

# ============================================================================
# Example 5: Using custom_prompt helper function
# ============================================================================
print("\n" + "="*80)
print("EXAMPLE 5: Using Helper Function")
print("="*80)

prompt = prompt_temp.create_custom_prompt(
    "sci_fi_templates",
    style="cyberpunk",
    subject="lone hacker",
    setting="dark alley with holographic advertisements",
    mood="gritty and atmospheric",
    technology="advanced neural interfaces",
    lighting="neon",
    action="working on a glowing terminal",
    quality="digital art, highly detailed, 4k"
)

negative_prompt = prompt_temp.NEGATIVE_PROMPTS["general"]

print(f"\nPrompt: {prompt}")

start = time.perf_counter()
image = pipe(
    prompt=prompt,
    negative_prompt=negative_prompt,
    num_inference_steps=25,
    guidance_scale=8.5,
    generator=torch.Generator().manual_seed(789)
).images[0]
latency = time.perf_counter() - start

image.save("example_5_cyberpunk.png")
print(f"\nGenerated image saved as 'example_5_cyberpunk.png'")
print(f"Time taken: {latency:.2f} seconds")

print("\n" + "="*80)
print("ALL EXAMPLES COMPLETED!")
print("="*80)

