"""
Image Generation Module for AI Artist
Handles Stable Diffusion pipeline and image generation with metadata
"""

import sys
import torch
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, Tuple
from PIL import Image
from PIL.PngImagePlugin import PngInfo
from diffusers import StableDiffusionPipeline
import json
import re
import io

# Fix Windows console encoding issues
if sys.platform == 'win32':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    except:
        pass


class ImageGenerator:
    """Handles Stable Diffusion image generation with metadata support."""
    
    def __init__(self, model_name: str = "runwayml/stable-diffusion-v1-5", device: str = "cpu"):
        """
        Initialize the image generator.
        
        Args:
            model_name: HuggingFace model identifier
            device: Device to run on ("cpu", "cuda", or "mps")
        """
        self.model_name = model_name
        self.device = device
        self.pipe = None
        self.is_loaded = False
        
    def load_model(self) -> bool:
        """
        Load the Stable Diffusion model.
        
        Returns:
            bool: True if loaded successfully, False otherwise
        """
        print(f"torch version: {torch.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")
        print(f"Loading Stable Diffusion pipeline from {self.model_name}...")
        print("Note: First-time loading will download ~4GB model (may take several minutes)")

        try:
            # Load with safetensors for better compatibility
            self.pipe = StableDiffusionPipeline.from_pretrained(
                "runwayml/stable-diffusion-v1-5",
                torch_dtype=torch.float32,
                safety_checker=None,
                requires_safety_checker=False,
                low_cpu_mem_usage=False  # Disable to avoid accelerate issues
            )
            print("Model downloaded/loaded, moving to device...")
            self.pipe = self.pipe.to(self.device)
            self.is_loaded = True
            print(f"[SUCCESS] Pipeline loaded successfully on {self.device}!")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to load pipeline: {e}")
            print(f"Error type: {type(e).__name__}")
            import traceback
            print(f"Traceback:\n{traceback.format_exc()}")
            self.is_loaded = False
            return False
    
    def generate_image(
        self,
        prompt: str,
        negative_prompt: str = "",
        num_inference_steps: int = 25,
        guidance_scale: float = 7.5,
        seed: Optional[int] = None,
        width: int = 512,
        height: int = 512,
        num_images: int = 1,
        template_info: Optional[Dict] = None
    ) -> Tuple[list, Dict]:
        """
        Generate image(s) from prompt.
        
        Args:
            prompt: Main generation prompt
            negative_prompt: Negative prompt (what to avoid)
            num_inference_steps: Number of denoising steps
            guidance_scale: How closely to follow the prompt
            seed: Random seed for reproducibility
            width: Image width
            height: Image height
            num_images: Number of images to generate
            template_info: Dict containing template metadata (category, template, inputs)
            
        Returns:
            Tuple of (list of PIL Images, metadata dict)
        """
        if not self.is_loaded:
            raise RuntimeError("Model not loaded. Call load_model() first.")
        
        generator = None
        if seed is not None:
            generator = torch.Generator(device=self.device).manual_seed(seed)
        
        start_time = time.perf_counter()
        
        print(f"Generating {num_images} image(s)...")
        result = self.pipe(
            prompt=prompt,
            negative_prompt=negative_prompt if negative_prompt else None,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            generator=generator,
            width=width,
            height=height,
            num_images_per_prompt=num_images
        )
        
        generation_time = time.perf_counter() - start_time
        
        metadata = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "num_inference_steps": num_inference_steps,
            "guidance_scale": guidance_scale,
            "seed": seed,
            "width": width,
            "height": height,
            "num_images": num_images,
            "generation_time": round(generation_time, 2),
            "model": self.model_name,
            "device": self.device,
            "timestamp": datetime.now().isoformat()
        }
        
        if template_info:
            metadata["template_info"] = template_info
        
        print(f"Generation completed in {generation_time:.2f} seconds")
        
        return result.images, metadata
    
    @staticmethod
    def extract_subject_from_prompt(prompt: str, max_words: int = 3) -> str:
        """Extract a subject name from the prompt for filename."""
        prefixes = [
            r"^a\s+", r"^an\s+", r"^the\s+", 
            r"^.*?\s+of\s+", r"^.*?\s+portrait\s+of\s+",
            r"^.*?\s+image\s+of\s+", r"^.*?\s+photo\s+of\s+"
        ]
        
        cleaned = prompt.lower()
        for prefix in prefixes:
            cleaned = re.sub(prefix, "", cleaned)
        
        words = cleaned.split()
        
        skip_words = {
            'style', 'art', 'painting', 'digital', 'realistic', 
            'detailed', 'high', 'quality', 'masterpiece', '8k', '4k',
            'ultra', 'professional', 'stunning', 'beautiful'
        }
        
        subject_words = [w for w in words if w not in skip_words][:max_words]
        
        if not subject_words:
            subject_words = words[:max_words]
        
        subject = "_".join(subject_words)
        subject = re.sub(r'[^a-z0-9_]', '', subject)
        
        return subject[:30]
    
    @staticmethod
    def save_image_with_metadata(
        image: Image.Image,
        metadata: Dict,
        output_dir: str = "generated_images",
        custom_filename: Optional[str] = None
    ) -> str:
        """Save image with metadata embedded."""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        if custom_filename:
            filename = custom_filename
        else:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            subject = ImageGenerator.extract_subject_from_prompt(metadata.get("prompt", "image"))
            filename = f"{timestamp}_{subject}"
        
        if not filename.endswith('.png'):
            filename += '.png'
        
        filepath = output_path / filename
        
        png_info = PngInfo()
        png_info.add_text("prompt", metadata.get("prompt", ""))
        png_info.add_text("negative_prompt", metadata.get("negative_prompt", ""))
        png_info.add_text("parameters", json.dumps({
            k: v for k, v in metadata.items() 
            if k not in ["prompt", "negative_prompt"]
        }))
        
        image.save(filepath, "PNG", pnginfo=png_info)
        
        json_path = filepath.with_suffix('.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        print(f"Image saved: {filepath}")
        print(f"Metadata saved: {json_path}")
        
        return str(filepath)
    
    @staticmethod
    def load_image_with_metadata(filepath: str) -> Tuple[Optional[Image.Image], Optional[Dict]]:
        """Load an image and its metadata from file."""
        try:
            img_path = Path(filepath)
            if not img_path.exists():
                print(f"Image file not found: {filepath}")
                return None, None
            
            image = Image.open(img_path)
            
            json_path = img_path.with_suffix('.json')
            if json_path.exists():
                with open(json_path, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
                print(f"Loaded metadata from: {json_path}")
            else:
                metadata = {}
                if hasattr(image, 'text'):
                    if 'prompt' in image.text:
                        metadata['prompt'] = image.text['prompt']
                    if 'negative_prompt' in image.text:
                        metadata['negative_prompt'] = image.text['negative_prompt']
                    if 'parameters' in image.text:
                        try:
                            params = json.loads(image.text['parameters'])
                            metadata.update(params)
                        except json.JSONDecodeError:
                            pass
                print(f"Loaded metadata from PNG: {filepath}")
            
            return image, metadata
            
        except Exception as e:
            print(f"Error loading image: {e}")
            return None, None
    
    @staticmethod
    def get_all_generated_images(output_dir: str = "generated_images") -> list:
        """Get list of all generated images with their metadata."""
        output_path = Path(output_dir)
        if not output_path.exists():
            return []
        
        images_info = []
        
        for png_file in sorted(output_path.glob("*.png"), reverse=True):
            image, metadata = ImageGenerator.load_image_with_metadata(str(png_file))
            
            if image and metadata:
                images_info.append({
                    'filepath': str(png_file),
                    'image': image,
                    #'metadata': metadata,
                    'timestamp': metadata.get('timestamp', ''),
                    'template_category': metadata.get('template_info', {}).get('category', 'Unknown'),
                    'template_inputs': metadata.get('template_info', {}).get('inputs', {})
                })
        
        return images_info


# ============================================================================
# ORIGINAL CODE (COMMENTED OUT FOR REFERENCE)
# ============================================================================

# import sys
# import torch,time
# import torchvision
# import torchaudio
# import transformers
# import gradio
# import diffusers
# import datasets
# import peft
# import accelerate
# import tqdm
# import scipy
# from PIL import Image
# from diffusers import StableDiffusionPipeline
#
# print(f"torch version: {torch.__version__}")
# print(f"CUDA available: {torch.cuda.is_available()}")
#
# # Try a simpler approach with CPU-only generation for now
# print("Loading Stable Diffusion pipeline...")
# try:
#     pipe = StableDiffusionPipeline.from_pretrained(
#         "runwayml/stable-diffusion-v1-5",
#         torch_dtype=torch.float32,  # Use float32 for better compatibility
#         safety_checker=None,
#         requires_safety_checker=False
#     )
#     pipe = pipe.to("cpu")  # Use CPU to avoid memory issues
#     print("Pipeline loaded successfully!")
# except Exception as e:
#     print(f"Error loading pipeline: {e}")
#     print("Falling back to a simple test...")
#     # Create a simple test instead
#     import numpy as np
#     test_image = np.random.randint(0, 255, (512, 512, 3), dtype=np.uint8)
#     from PIL import Image
#     img = Image.fromarray(test_image)
#     img.save("output.png")
#     print("Generated test image instead")
#     exit()
#
# # Skip torch.compile as it requires C++ compiler
# # if hasattr(torch, "compile"):
# #     pipe.unet = torch.compile(pipe.unet, mode="reduce-overhead")
#
# stng = "surreal landscape, pastel colors, low-poly"
#
# prompt = "a watercolor of a child riding a horse in a misty forest"
# #  prompt = stng
# start=time.perf_counter()
# seed= 123
# image = pipe(prompt, num_inference_steps=16, guidance_scale=8.0, seed=seed).images[0]
# latency = time.perf_counter() - start
# print(f"Time taken: {latency} seconds")
# image.save("output1.png")


# ============================================================================
# EXAMPLE USAGE (for testing)
# ============================================================================

if __name__ == "__main__":
    generator = ImageGenerator(device="cpu")
    
    if generator.load_model():
        prompt = "a watercolor of a child riding a horse in a misty forest"
        negative = "blurry, low quality, bad anatomy"
        
        template_info = {
            "category": "Portrait",
            "template": "a {style} portrait of {subject}, {lighting}, {quality}",
            "template_index": 0,
            "inputs": {
                "subject": "child riding a horse",
                "quality": "masterpiece, detailed"
            },
            "style": "watercolor",
            "lighting": "soft natural light",
            "mood": "peaceful",
            "camera_details": None,
            "negative_prompt_type": "general"
        }
        
        images, metadata = generator.generate_image(
            prompt=prompt,
            negative_prompt=negative,
            num_inference_steps=16,
            guidance_scale=8.0,
            seed=123,
            template_info=template_info
        )
        
        filepath = generator.save_image_with_metadata(
            images[0],
            metadata,
            output_dir="generated_images"
        )
        
        print(f"\nTest image generated successfully: {filepath}")
        print("\nMetadata includes template inputs!")
    else:
        print("Failed to load model")

