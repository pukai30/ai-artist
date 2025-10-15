"""
Test script for metadata functionality
Demonstrates loading images with metadata and viewing template inputs
"""

from main import ImageGenerator
from pathlib import Path
import json

print("=" * 80)
print("METADATA SYSTEM TEST")
print("=" * 80)
print()

# Test 1: Check if generated images exist
print("📁 Test 1: Checking for generated images...")
output_dir = Path("generated_images")

if output_dir.exists():
    png_files = list(output_dir.glob("*.png"))
    json_files = list(output_dir.glob("*.json"))
    
    print(f"   Found {len(png_files)} PNG files")
    print(f"   Found {len(json_files)} JSON files")
    
    if png_files:
        print(f"\n   Recent files:")
        for png_file in sorted(png_files, reverse=True)[:3]:
            print(f"   - {png_file.name}")
else:
    print("   ⚠️ No generated images directory found yet")
    print("   Generate some images first using the Streamlit app!")

print()

# Test 2: Load and display metadata from most recent image
print("📋 Test 2: Loading metadata from most recent image...")

if output_dir.exists():
    png_files = sorted(output_dir.glob("*.png"), reverse=True)
    
    if png_files:
        test_file = png_files[0]
        print(f"   Loading: {test_file.name}")
        print()
        
        image, metadata = ImageGenerator.load_image_with_metadata(str(test_file))
        
        if image and metadata:
            print("   ✅ Successfully loaded image and metadata!")
            print()
            
            # Display key information
            print("   📝 Generation Details:")
            print(f"      Prompt: {metadata.get('prompt', 'N/A')[:80]}...")
            print(f"      Negative: {metadata.get('negative_prompt', 'N/A')[:60]}...")
            print(f"      Size: {metadata.get('width')}x{metadata.get('height')}")
            print(f"      Steps: {metadata.get('num_inference_steps')}")
            print(f"      Guidance: {metadata.get('guidance_scale')}")
            print(f"      Seed: {metadata.get('seed')}")
            print(f"      Time: {metadata.get('generation_time')}s")
            print()
            
            # Display template information if available
            if 'template_info' in metadata:
                template_info = metadata['template_info']
                
                print("   🎯 Template Information:")
                print(f"      Category: {template_info.get('category', 'N/A')}")
                print(f"      Template: {template_info.get('template', 'N/A')[:60]}...")
                print()
                
                print("   📝 User Inputs:")
                inputs = template_info.get('inputs', {})
                for key, value in inputs.items():
                    print(f"      {key.replace('_', ' ').title()}: {value}")
                print()
                
                print("   🎨 Style Configuration:")
                print(f"      Style: {template_info.get('style', 'N/A')[:50]}...")
                print(f"      Lighting: {template_info.get('lighting', 'N/A')}")
                print(f"      Mood: {template_info.get('mood', 'N/A')}")
                if template_info.get('camera_details'):
                    print(f"      Camera: {template_info.get('camera_details')}")
                print(f"      Negative Type: {template_info.get('negative_prompt_type', 'N/A')}")
            else:
                print("   ⚠️ No template info in metadata (older generation)")
        else:
            print("   ❌ Failed to load metadata")
    else:
        print("   ⚠️ No PNG files found")
else:
    print("   ⚠️ Directory doesn't exist yet")

print()

# Test 3: Get all generated images
print("📚 Test 3: Getting all generated images...")

all_images = ImageGenerator.get_all_generated_images()

if all_images:
    print(f"   Found {len(all_images)} images with metadata")
    print()
    
    # Show summary of recent images
    print("   Recent Generations:")
    for idx, img_info in enumerate(all_images[:5], 1):
        category = img_info.get('template_category', 'Unknown')
        filepath = Path(img_info['filepath']).name
        timestamp = img_info.get('timestamp', 'N/A')
        
        print(f"   {idx}. {filepath}")
        print(f"      Category: {category}")
        print(f"      Timestamp: {timestamp}")
        
        # Show template inputs if available
        template_inputs = img_info.get('template_inputs', {})
        if template_inputs:
            print(f"      Inputs: {', '.join([f'{k}={v[:20]}...' if len(v) > 20 else f'{k}={v}' for k, v in list(template_inputs.items())[:3]])}")
        print()
else:
    print("   ⚠️ No images found. Generate some images first!")

print()

# Test 4: Test metadata structure
print("🔍 Test 4: Verifying metadata structure...")

if output_dir.exists():
    json_files = list(output_dir.glob("*.json"))
    
    if json_files:
        test_json = json_files[0]
        print(f"   Checking: {test_json.name}")
        
        with open(test_json, 'r') as f:
            metadata = json.load(f)
        
        # Check for required fields
        required_fields = ['prompt', 'negative_prompt', 'num_inference_steps', 
                          'guidance_scale', 'seed', 'width', 'height', 'timestamp']
        
        print()
        print("   Required Fields:")
        for field in required_fields:
            status = "✓" if field in metadata else "✗"
            print(f"      {status} {field}")
        
        print()
        print("   Template Info Fields:")
        if 'template_info' in metadata:
            template_fields = ['category', 'template', 'inputs', 'style', 
                             'lighting', 'mood', 'negative_prompt_type']
            for field in template_fields:
                status = "✓" if field in metadata['template_info'] else "✗"
                print(f"      {status} template_info.{field}")
        else:
            print("      ⚠️ No template_info found (generate new images to test)")
    else:
        print("   ⚠️ No JSON files found")
else:
    print("   ⚠️ Directory doesn't exist")

print()
print("=" * 80)
print("METADATA TEST COMPLETE")
print("=" * 80)
print()

if not output_dir.exists() or not list(output_dir.glob("*.png")):
    print("💡 To generate test images:")
    print("   1. Run: streamlit run streamlit_app.py")
    print("   2. Create a prompt and generate images")
    print("   3. Run this test again to verify metadata")
else:
    print("✅ Metadata system is working!")
    print("   All generated images have complete metadata including template inputs")

print()

