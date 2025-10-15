"""
Demo script showing various prompt combinations
Run this to see examples of what the Streamlit app can generate
"""

import prompt_temp
import sys
import io

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def print_demo_prompt(title, template, params, negative_key):
    """Print a formatted demo prompt."""
    print(f"\n{'='*80}")
    print(f"🎨 {title}")
    print(f"{'='*80}")
    print(f"\n📋 Template:")
    print(f"   {template}")
    print(f"\n⚙️  Parameters:")
    for key, value in params.items():
        print(f"   • {key}: {value}")
    
    formatted = prompt_temp.format_prompt(template, **params)
    negative = prompt_temp.NEGATIVE_PROMPTS[negative_key]
    
    print(f"\n✨ Generated Prompt:")
    print(f"   {formatted}")
    print(f"\n🚫 Negative Prompt:")
    print(f"   {negative}")
    print(f"\n{'='*80}\n")

# Main demo
print("\n" + "="*80)
print(" "*25 + "🎨 PROMPT BUILDER DEMO")
print("="*80)
print("\nShowing 6 diverse examples from different categories:\n")

# Demo 1: Portrait
print_demo_prompt(
    "Demo 1: Cinematic Portrait",
    prompt_temp.PORTRAIT_TEMPLATES[0],
    {
        "style": prompt_temp.STYLES["cinematic"],
        "subject": "a young astronaut with determined expression",
        "lighting": "dramatic rim lighting",
        "quality": prompt_temp.QUALITY_MODIFIERS[0],
        "camera_details": "85mm lens, f/1.4, shallow depth of field"
    },
    "portrait"
)

# Demo 2: Landscape
print_demo_prompt(
    "Demo 2: Watercolor Landscape",
    prompt_temp.LANDSCAPE_TEMPLATES[3],
    {
        "style": prompt_temp.STYLES["watercolor"],
        "location": "serene lake surrounded by autumn trees",
        "time_of_day": "golden hour",
        "elements": "gentle mist rising from water, distant mountains",
        "quality": prompt_temp.QUALITY_MODIFIERS[2]
    },
    "landscape"
)

# Demo 3: Fantasy
print_demo_prompt(
    "Demo 3: Fantasy Creature",
    prompt_temp.FANTASY_TEMPLATES[1],
    {
        "creature": "ethereal phoenix",
        "action": "soaring through",
        "setting": "mystical crystal caverns",
        "style": prompt_temp.STYLES["digital_art"],
        "lighting": "magical glowing crystals",
        "quality": prompt_temp.QUALITY_MODIFIERS[1]
    },
    "fantasy"
)

# Demo 4: Sci-Fi
print_demo_prompt(
    "Demo 4: Cyberpunk Scene",
    prompt_temp.SCI_FI_TEMPLATES[3],
    {
        "subject": "advanced AI android",
        "setting": "rain-soaked neon city streets",
        "lighting": "purple and cyan neon signs",
        "mood": "noir and atmospheric",
        "quality": prompt_temp.QUALITY_MODIFIERS[3]
    },
    "realistic"
)

# Demo 5: Animal
print_demo_prompt(
    "Demo 5: Wildlife Photography",
    prompt_temp.ANIMAL_TEMPLATES[2],
    {
        "animal": "snow leopard",
        "features": "intense blue eyes and thick spotted fur",
        "habitat": "rocky mountain cliff during snowfall",
        "lighting": "soft overcast natural light",
        "quality": "wildlife photography, national geographic style, 8k"
    },
    "realistic"
)

# Demo 6: Abstract
print_demo_prompt(
    "Demo 6: Abstract Digital Art",
    prompt_temp.ABSTRACT_TEMPLATES[1],
    {
        "concept": "human consciousness",
        "style": prompt_temp.STYLES["psychedelic"],
        "elements": "interconnected neural networks, flowing energy patterns",
        "quality": prompt_temp.QUALITY_MODIFIERS[4]
    },
    "artistic"
)

# Summary
print("\n" + "="*80)
print(" "*20 + "🎯 DEMO COMPLETE")
print("="*80)
print("\n📝 These examples demonstrate:")
print("   • Different template categories")
print("   • Style preset integration")
print("   • Lighting options")
print("   • Quality modifiers")
print("   • Negative prompt variations")
print("\n🚀 Try these combinations in the Streamlit app!")
print("   Run: streamlit run streamlit_app.py")
print("\n" + "="*80 + "\n")

