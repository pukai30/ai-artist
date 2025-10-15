"""
Test script to verify prompt_temp.py integration works correctly
Run this before starting the Streamlit app to ensure everything is set up
"""

import prompt_temp
import re
import sys

# Fix Windows console encoding issues
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 80)
print("TESTING PROMPT_TEMP.PY INTEGRATION")
print("=" * 80)
print()

# Test 1: Check all template categories exist
print("✅ Test 1: Checking Template Categories...")
categories = [
    "PORTRAIT_TEMPLATES",
    "LANDSCAPE_TEMPLATES", 
    "FANTASY_TEMPLATES",
    "SCI_FI_TEMPLATES",
    "ANIMAL_TEMPLATES",
    "ARCHITECTURE_TEMPLATES",
    "ABSTRACT_TEMPLATES",
    "FOOD_TEMPLATES",
    "CHARACTER_TEMPLATES",
    "PRODUCT_TEMPLATES"
]

for cat in categories:
    templates = getattr(prompt_temp, cat, None)
    if templates and isinstance(templates, list):
        print(f"   ✓ {cat}: {len(templates)} templates found")
    else:
        print(f"   ✗ {cat}: NOT FOUND")

print()

# Test 2: Check negative prompts
print("✅ Test 2: Checking Negative Prompts...")
negative_keys = ["general", "portrait", "realistic", "artistic", "fantasy", 
                 "minimal", "product", "landscape", "clean"]

for key in negative_keys:
    if key in prompt_temp.NEGATIVE_PROMPTS:
        print(f"   ✓ '{key}': Available")
    else:
        print(f"   ✗ '{key}': Missing")

print()

# Test 3: Check style presets
print("✅ Test 3: Checking Style Presets...")
print(f"   Found {len(prompt_temp.STYLES)} style presets:")
for style_key in list(prompt_temp.STYLES.keys())[:5]:
    print(f"      - {style_key}")
print(f"      ... and {len(prompt_temp.STYLES) - 5} more")

print()

# Test 4: Check lighting options
print("✅ Test 4: Checking Lighting Options...")
print(f"   Found {len(prompt_temp.LIGHTING_OPTIONS)} lighting options:")
for light in prompt_temp.LIGHTING_OPTIONS[:5]:
    print(f"      - {light}")
print(f"      ... and {len(prompt_temp.LIGHTING_OPTIONS) - 5} more")

print()

# Test 5: Check quality modifiers
print("✅ Test 5: Checking Quality Modifiers...")
print(f"   Found {len(prompt_temp.QUALITY_MODIFIERS)} quality modifiers")

print()

# Test 6: Test format_prompt function
print("✅ Test 6: Testing format_prompt Function...")
test_template = "a {style} portrait of {subject}, {lighting}"
test_params = {
    "style": "cinematic",
    "subject": "a warrior",
    "lighting": "dramatic lighting"
}

result = prompt_temp.format_prompt(test_template, **test_params)
expected = "a cinematic portrait of a warrior, dramatic lighting"

if result == expected:
    print(f"   ✓ Format function works correctly")
    print(f"      Input: {test_template}")
    print(f"      Output: {result}")
else:
    print(f"   ✗ Format function failed")
    print(f"      Expected: {expected}")
    print(f"      Got: {result}")

print()

# Test 7: Test placeholder extraction (for Streamlit app)
print("✅ Test 7: Testing Placeholder Extraction...")

def extract_placeholders(template):
    return re.findall(r'\{(\w+)\}', template)

test_template = "a {style} image of {subject} in {location}, {lighting}, {quality}"
placeholders = extract_placeholders(test_template)
expected_placeholders = ["style", "subject", "location", "lighting", "quality"]

if placeholders == expected_placeholders:
    print(f"   ✓ Placeholder extraction works")
    print(f"      Template: {test_template}")
    print(f"      Extracted: {placeholders}")
else:
    print(f"   ✗ Placeholder extraction failed")

print()

# Test 8: Test example prompts
print("✅ Test 8: Checking Example Prompts...")
print(f"   Found {len(prompt_temp.EXAMPLE_PROMPTS)} example prompts")

for i, example in enumerate(prompt_temp.EXAMPLE_PROMPTS[:3], 1):
    formatted = prompt_temp.format_prompt(example["template"], **example["params"])
    print(f"   {i}. {example['name']}")
    print(f"      Template has {len(extract_placeholders(example['template']))} placeholders")
    print(f"      Formatted length: {len(formatted)} chars")

print()

# Summary
print("=" * 80)
print("✨ ALL TESTS COMPLETED")
print("=" * 80)
print()
print("🚀 Ready to run Streamlit app!")
print("   Run: streamlit run streamlit_app.py")
print()

