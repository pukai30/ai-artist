"""
Object Extraction and Image Generation
Extracts objects from an input image and generates new images using Stable Diffusion
"""

import torch
from PIL import Image
from transformers import (
    CLIPSegProcessor, 
    CLIPSegForImageSegmentation,
    BlipProcessor,
    BlipForConditionalGeneration
)
from diffusers import StableDiffusionPipeline
import numpy as np
from pathlib import Path
import time
from typing import List, Tuple, Optional
import io
import sys

# Fix Windows encoding
if sys.platform == 'win32':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    except:
        pass


class ObjectExtractorAndGenerator:
    """Extract objects from images and generate new images with Stable Diffusion."""
    
    def __init__(self, device: str = "cpu"):
        """
        Initialize the object extractor and image generator.
        
        Args:
            device: Device to use ("cpu" or "cuda")
        """
        self.device = device
        
        # Models (loaded on demand)
        self.segmentation_processor = None
        self.segmentation_model = None
        self.caption_processor = None
        self.caption_model = None
        self.sd_pipe = None
        
        self.models_loaded = {
            'segmentation': False,
            'caption': False,
            'stable_diffusion': False
        }
    
    def load_segmentation_model(self):
        """Load CLIPSeg for object segmentation."""
        print("Loading CLIPSeg segmentation model...")
        try:
            self.segmentation_processor = CLIPSegProcessor.from_pretrained(
                "CIDAS/clipseg-rd64-refined"
            )
            self.segmentation_model = CLIPSegForImageSegmentation.from_pretrained(
                "CIDAS/clipseg-rd64-refined"
            )
            self.segmentation_model.to(self.device)
            self.models_loaded['segmentation'] = True
            print("[SUCCESS] Segmentation model loaded")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to load segmentation model: {e}")
            return False
    
    def load_caption_model(self):
        """Load BLIP for image captioning."""
        print("Loading BLIP captioning model...")
        try:
            self.caption_processor = BlipProcessor.from_pretrained(
                "Salesforce/blip-image-captioning-base"
            )
            self.caption_model = BlipForConditionalGeneration.from_pretrained(
                "Salesforce/blip-image-captioning-base"
            )
            self.caption_model.to(self.device)
            self.models_loaded['caption'] = True
            print("[SUCCESS] Caption model loaded")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to load caption model: {e}")
            return False
    
    def load_stable_diffusion(self):
        """Load Stable Diffusion for image generation."""
        print("Loading Stable Diffusion pipeline...")
        try:
            self.sd_pipe = StableDiffusionPipeline.from_pretrained(
                "runwayml/stable-diffusion-v1-5",
                torch_dtype=torch.float32,
                safety_checker=None,
                requires_safety_checker=False,
                low_cpu_mem_usage=False
            )
            self.sd_pipe.to(self.device)
            self.models_loaded['stable_diffusion'] = True
            print("[SUCCESS] Stable Diffusion loaded")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to load Stable Diffusion: {e}")
            return False
    
    def load_all_models(self):
        """Load all required models."""
        print("\n" + "="*80)
        print("LOADING ALL MODELS")
        print("="*80 + "\n")
        
        success = True
        success &= self.load_caption_model()
        success &= self.load_segmentation_model()
        success &= self.load_stable_diffusion()
        
        print("\n" + "="*80)
        if success:
            print("All models loaded successfully!")
        else:
            print("Some models failed to load. Check errors above.")
        print("="*80 + "\n")
        
        return success
    
    def segment_object(
        self, 
        image: Image.Image, 
        object_prompt: str,
        threshold: float = 0.4
    ) -> Optional[Image.Image]:
        """
        Segment an object from the image using text prompt.
        
        Args:
            image: Input PIL Image
            object_prompt: Text description of object to segment (e.g., "person", "dog")
            threshold: Segmentation threshold (0-1)
            
        Returns:
            PIL Image with segmented object (background removed) or None
        """
        if not self.models_loaded['segmentation']:
            print("[ERROR] Segmentation model not loaded")
            return None
        
        print(f"Segmenting '{object_prompt}' from image...")
        
        # Prepare inputs
        inputs = self.segmentation_processor(
            text=[object_prompt],
            images=[image],
            return_tensors="pt"
        )
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        
        # Get segmentation mask
        with torch.no_grad():
            outputs = self.segmentation_model(**inputs)
        
        # Process mask
        mask = torch.sigmoid(outputs.logits).cpu().numpy()[0]
        
        # Apply threshold
        binary_mask = (mask > threshold).astype(np.uint8) * 255
        
        # Resize mask to match image size
        mask_image = Image.fromarray(binary_mask).resize(image.size, Image.Resampling.BILINEAR)
        
        # Create RGBA image with transparency
        image_rgba = image.convert("RGBA")
        mask_array = np.array(mask_image)
        
        # Apply mask as alpha channel
        image_array = np.array(image_rgba)
        image_array[:, :, 3] = mask_array
        
        result = Image.fromarray(image_array, 'RGBA')
        
        print(f"[SUCCESS] Object segmented")
        return result
    
    def caption_image(self, image: Image.Image) -> str:
        """
        Generate a caption for the image or extracted object.
        
        Args:
            image: Input PIL Image
            
        Returns:
            Generated caption string
        """
        if not self.models_loaded['caption']:
            print("[ERROR] Caption model not loaded")
            return ""
        
        print("Generating caption for image...")
        
        # Prepare inputs
        inputs = self.caption_processor(image, return_tensors="pt")
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        
        # Generate caption
        with torch.no_grad():
            outputs = self.caption_model.generate(**inputs, max_length=50)
        
        caption = self.caption_processor.decode(outputs[0], skip_special_tokens=True)
        
        print(f"[CAPTION] {caption}")
        return caption
    
    def generate_from_description(
        self,
        description: str,
        negative_prompt: str = "blurry, low quality, distorted",
        style_modifier: str = "",
        num_inference_steps: int = 25,
        guidance_scale: float = 7.5,
        seed: Optional[int] = None,
        width: int = 512,
        height: int = 512
    ) -> Tuple[Image.Image, dict]:
        """
        Generate a new image from description using Stable Diffusion.
        
        Args:
            description: Description of the object/scene to generate
            negative_prompt: What to avoid
            style_modifier: Additional style instructions
            num_inference_steps: Number of steps
            guidance_scale: How closely to follow prompt
            seed: Random seed
            width: Image width
            height: Image height
            
        Returns:
            Tuple of (generated image, metadata dict)
        """
        if not self.models_loaded['stable_diffusion']:
            print("[ERROR] Stable Diffusion not loaded")
            return None, {}
        
        # Build prompt
        if style_modifier:
            full_prompt = f"{style_modifier} {description}"
        else:
            full_prompt = description
        
        print(f"Generating image from: '{full_prompt}'")
        
        # Set up generator
        generator = None
        if seed is not None:
            generator = torch.Generator(device=self.device).manual_seed(seed)
        
        # Generate
        start_time = time.perf_counter()
        result = self.sd_pipe(
            prompt=full_prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            generator=generator,
            width=width,
            height=height
        )
        generation_time = time.perf_counter() - start_time
        
        metadata = {
            "prompt": full_prompt,
            "base_description": description,
            "style_modifier": style_modifier,
            "negative_prompt": negative_prompt,
            "num_inference_steps": num_inference_steps,
            "guidance_scale": guidance_scale,
            "seed": seed,
            "width": width,
            "height": height,
            "generation_time": round(generation_time, 2)
        }
        
        print(f"[SUCCESS] Generated in {generation_time:.2f}s")
        
        return result.images[0], metadata
    
    def extract_and_generate(
        self,
        input_image_path: str,
        object_to_extract: str,
        new_scene_description: str,
        style: str = "photorealistic",
        output_dir: str = "extracted_generations",
        save_intermediate: bool = True
    ) -> dict:
        """
        Complete pipeline: Extract object from image and generate new image.
        
        Args:
            input_image_path: Path to input image
            object_to_extract: What object to extract (e.g., "person", "dog")
            new_scene_description: New scene/context for the object
            style: Style for new generation
            output_dir: Where to save outputs
            save_intermediate: Whether to save intermediate steps
            
        Returns:
            Dictionary with results and paths
        """
        print("\n" + "="*80)
        print("OBJECT EXTRACTION AND GENERATION PIPELINE")
        print("="*80 + "\n")
        
        # Create output directory
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        results = {
            'success': False,
            'original_image': None,
            'segmented_object': None,
            'object_description': None,
            'generated_image': None,
            'paths': {}
        }
        
        # Step 1: Load original image
        print(f"Step 1: Loading image from {input_image_path}")
        try:
            original_image = Image.open(input_image_path).convert("RGB")
            results['original_image'] = original_image
            print(f"[SUCCESS] Image loaded: {original_image.size}")
        except Exception as e:
            print(f"[ERROR] Failed to load image: {e}")
            return results
        
        # Step 2: Segment object
        print(f"\nStep 2: Segmenting '{object_to_extract}' from image")
        segmented = self.segment_object(original_image, object_to_extract)
        
        if segmented:
            results['segmented_object'] = segmented
            if save_intermediate:
                seg_path = output_path / f"segmented_{object_to_extract}.png"
                segmented.save(seg_path)
                results['paths']['segmented'] = str(seg_path)
                print(f"[SAVED] Segmented object: {seg_path}")
        else:
            print("[ERROR] Segmentation failed")
            return results
        
        # Step 3: Caption the extracted object
        print(f"\nStep 3: Generating description of extracted object")
        description = self.caption_image(segmented)
        results['object_description'] = description
        
        # Step 4: Build new prompt
        print(f"\nStep 4: Building generation prompt")
        new_prompt = f"{style} image of {description} in {new_scene_description}"
        print(f"[PROMPT] {new_prompt}")
        
        # Step 5: Generate new image
        print(f"\nStep 5: Generating new image with Stable Diffusion")
        generated, metadata = self.generate_from_description(
            description=f"{description} in {new_scene_description}",
            style_modifier=style,
            negative_prompt="blurry, low quality, distorted, bad anatomy",
            num_inference_steps=25,
            guidance_scale=7.5
        )
        
        if generated:
            results['generated_image'] = generated
            results['success'] = True
            
            # Save generated image
            gen_path = output_path / f"generated_{object_to_extract}_new_scene.png"
            generated.save(gen_path)
            results['paths']['generated'] = str(gen_path)
            print(f"[SAVED] Generated image: {gen_path}")
            
            # Save metadata
            metadata['object_extracted'] = object_to_extract
            metadata['new_scene'] = new_scene_description
            metadata['original_image'] = input_image_path
            
            import json
            meta_path = gen_path.with_suffix('.json')
            with open(meta_path, 'w') as f:
                json.dump(metadata, f, indent=2)
            results['paths']['metadata'] = str(meta_path)
        
        print("\n" + "="*80)
        print("PIPELINE COMPLETE")
        print("="*80 + "\n")
        
        return results


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

def example_usage():
    """Example of using the object extraction and generation."""
    
    # Initialize
    extractor = ObjectExtractorAndGenerator(device="cpu")
    
    # Load all models
    print("Loading models (this will take a few minutes)...")
    if not extractor.load_all_models():
        print("[ERROR] Failed to load models. Exiting.")
        return
    
    # Example 1: Extract person and put in different scene
    print("\n" + "="*80)
    print("EXAMPLE 1: Extract person and place in fantasy landscape")
    print("="*80 + "\n")
    
    results = extractor.extract_and_generate(
        input_image_path="input_image.jpg",  # Replace with your image
        object_to_extract="person",
        new_scene_description="a magical forest with glowing mushrooms",
        style="fantasy art, detailed, vibrant colors"
    )
    
    if results['success']:
        print(f"\n[SUCCESS] Pipeline completed!")
        print(f"Original image: {results['original_image'].size}")
        print(f"Object description: {results['object_description']}")
        print(f"Generated image saved: {results['paths'].get('generated')}")
    
    # Example 2: Extract animal and create artistic version
    print("\n" + "="*80)
    print("EXAMPLE 2: Extract animal and create in different style")
    print("="*80 + "\n")
    
    results2 = extractor.extract_and_generate(
        input_image_path="input_image.jpg",
        object_to_extract="dog",
        new_scene_description="a serene beach at sunset",
        style="watercolor painting, soft colors, artistic"
    )


# ============================================================================
# STANDALONE FUNCTIONALITY
# ============================================================================

def extract_object_only(image_path: str, object_name: str, output_path: str = "segmented_object.png"):
    """
    Extract just the object without generating new image.
    
    Args:
        image_path: Path to input image
        object_name: Object to extract (e.g., "person", "dog", "car")
        output_path: Where to save segmented object
        
    Returns:
        PIL Image with extracted object
    """
    extractor = ObjectExtractorAndGenerator()
    
    if extractor.load_segmentation_model():
        image = Image.open(image_path).convert("RGB")
        segmented = extractor.segment_object(image, object_name)
        
        if segmented:
            segmented.save(output_path)
            print(f"[SAVED] Segmented object: {output_path}")
            return segmented
    
    return None


def describe_image(image_path: str) -> str:
    """
    Generate a description of an image.
    
    Args:
        image_path: Path to image
        
    Returns:
        Generated caption/description
    """
    extractor = ObjectExtractorAndGenerator()
    
    if extractor.load_caption_model():
        image = Image.open(image_path).convert("RGB")
        caption = extractor.caption_image(image)
        return caption
    
    return ""


def generate_from_extracted_object(
    segmented_object_path: str,
    new_scene: str,
    style: str = "photorealistic",
    output_path: str = "generated_new.png"
):
    """
    Generate new image from already segmented object.
    
    Args:
        segmented_object_path: Path to segmented object image
        new_scene: Description of new scene/context
        style: Style for generation
        output_path: Where to save result
        
    Returns:
        Generated PIL Image
    """
    extractor = ObjectExtractorAndGenerator()
    
    # Load caption and SD models
    extractor.load_caption_model()
    extractor.load_stable_diffusion()
    
    # Caption the object
    image = Image.open(segmented_object_path).convert("RGB")
    description = extractor.caption_image(image)
    
    # Generate new image
    generated, metadata = extractor.generate_from_description(
        description=f"{description} in {new_scene}",
        style_modifier=style
    )
    
    if generated:
        generated.save(output_path)
        print(f"[SAVED] Generated image: {output_path}")
        return generated
    
    return None


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*80)
    print("OBJECT EXTRACTION AND IMAGE GENERATION")
    print("="*80 + "\n")
    
    print("This program will:")
    print("1. Extract an object from an input image")
    print("2. Generate description of the object")
    print("3. Create new image with that object in a different scene")
    print()
    
    # Check if input image exists
    test_images = ["input_image.jpg", "input_image.png", "output1.png", "output.png"]
    input_image = None
    
    for img_path in test_images:
        if Path(img_path).exists():
            input_image = img_path
            print(f"Found input image: {img_path}")
            break
    
    if not input_image:
        print("[WARNING] No input image found. Creating a test...")
        print("Please provide an 'input_image.jpg' file to use this feature.")
        print()
        print("For testing, you can:")
        print("1. Copy any image to this folder as 'input_image.jpg'")
        print("2. Or use one of the generated images (output.png, output1.png)")
        print()
        exit()
    
    # Initialize extractor
    extractor = ObjectExtractorAndGenerator(device="cpu")
    
    # Load models
    if not extractor.load_all_models():
        print("[ERROR] Failed to load one or more models")
        exit()
    
    # Run the pipeline
    print("\n" + "="*80)
    print("RUNNING PIPELINE")
    print("="*80 + "\n")
    
    results = extractor.extract_and_generate(
        input_image_path=input_image,
        object_to_extract="person",  # Change to "dog", "cat", "car", etc.
        new_scene_description="walking a beachfront with clear blue sky",
        style="digital art, highly detailed, cinematic"
    )
    
    if results['success']:
        print("\n" + "="*80)
        print("SUCCESS!")
        print("="*80)
        print(f"\nObject extracted: {results['object_description']}")
        print(f"Segmented image: {results['paths'].get('segmented')}")
        print(f"Generated image: {results['paths'].get('generated')}")
        print(f"Metadata: {results['paths'].get('metadata')}")
        print("\nCheck the 'extracted_generations' folder for results!")
    else:
        print("\n[ERROR] Pipeline failed. Check errors above.")

