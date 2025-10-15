"""
Prompt Templates for Diffusion Model Image Generation
Includes various templates with placeholders for customization
"""

# ============================================================================
# PROMPT TEMPLATES
# ============================================================================

PORTRAIT_TEMPLATES = [
    "a {style} portrait of {subject}, {lighting}, {quality}, {camera_details}",
    "{subject} portrait in {style} style, {mood} atmosphere, {quality}",
    "professional headshot of {subject}, {lighting}, {background}, {quality}",
    "close-up portrait of {subject}, {expression}, {style} art style, {quality}",
    "{subject} with {features}, {style} painting, {mood} lighting, {quality}",
]

LANDSCAPE_TEMPLATES = [
    "a {style} landscape of {location}, {time_of_day}, {weather}, {quality}",
    "{location} scenery, {style} art style, {season}, {mood} atmosphere, {quality}",
    "panoramic view of {location}, {weather} conditions, {lighting}, {quality}",
    "{style} painting of {location}, {time_of_day}, {elements}, {quality}",
    "vast {location} with {elements}, {mood} atmosphere, {style} style, {quality}",
]

FANTASY_TEMPLATES = [
    "a {style} illustration of {creature} in {setting}, {mood} atmosphere, {quality}",
    "{creature} {action} in {setting}, {style} art, {lighting}, {quality}",
    "magical {setting} with {creature}, {elements}, {style} style, {quality}",
    "{creature} surrounded by {elements}, {mood} ambiance, {style} painting, {quality}",
    "fantasy scene of {creature} {action}, {setting}, {lighting}, {quality}",
]

SCI_FI_TEMPLATES = [
    "a {style} depiction of {subject} in {setting}, {mood} atmosphere, {technology}, {quality}",
    "futuristic {subject} {action}, {setting}, {lighting}, {technology}, {quality}",
    "{setting} with {subject}, {style} sci-fi art, {technology}, {quality}",
    "cyberpunk {subject} in {setting}, neon {lighting}, {mood} atmosphere, {quality}",
    "{subject} against {setting} backdrop, {technology}, {style} style, {quality}",
]

ANIMAL_TEMPLATES = [
    "a {style} image of {animal} in {habitat}, {behavior}, {lighting}, {quality}",
    "{animal} {action} in {habitat}, {style} photography, {mood} mood, {quality}",
    "majestic {animal} with {features}, {habitat}, {lighting}, {quality}",
    "{style} artwork of {animal}, {habitat} background, {mood} atmosphere, {quality}",
    "close-up of {animal} {action}, {features}, {lighting}, {quality}",
]

ARCHITECTURE_TEMPLATES = [
    "a {style} view of {building} architecture, {time_of_day}, {atmosphere}, {quality}",
    "{building} with {features}, {style} architecture, {lighting}, {quality}",
    "{style} rendering of {building}, {environment}, {mood} atmosphere, {quality}",
    "interior of {building}, {features}, {lighting}, {style} design, {quality}",
    "{building} facade, {style} architecture, {time_of_day}, {weather}, {quality}",
]

ABSTRACT_TEMPLATES = [
    "{style} abstract art with {elements}, {colors}, {mood} mood, {quality}",
    "abstract {concept} representation, {style} style, {elements}, {quality}",
    "{colors} abstract composition, {elements}, {mood} atmosphere, {quality}",
    "{style} digital art of {concept}, {elements}, {colors}, {quality}",
    "minimalist {concept} with {elements}, {colors}, {style} aesthetics, {quality}",
]

FOOD_TEMPLATES = [
    "a {style} photograph of {dish}, {presentation}, {lighting}, {quality}",
    "{dish} on {surface}, {style} food photography, {garnish}, {lighting}, {quality}",
    "gourmet {dish} with {ingredients}, {presentation}, {mood} lighting, {quality}",
    "{style} image of {dish}, {setting} background, {garnish}, {quality}",
    "close-up of {dish}, {details}, {lighting}, {style} photography, {quality}",
]

CHARACTER_TEMPLATES = [
    "a {style} character design of {character}, {pose}, {outfit}, {background}, {quality}",
    "{character} wearing {outfit}, {pose}, {mood} atmosphere, {style} art, {quality}",
    "full body illustration of {character}, {features}, {style} style, {quality}",
    "{character} in {pose}, {background} setting, {lighting}, {quality}",
    "{style} concept art of {character}, {outfit}, {features}, {quality}",
]

PRODUCT_TEMPLATES = [
    "a {style} product shot of {product}, {background}, {lighting}, {quality}",
    "{product} on {surface}, {style} photography, {mood} atmosphere, {quality}",
    "minimalist {product} showcase, {background}, {lighting}, {quality}",
    "{style} render of {product}, {angle} angle, {environment}, {quality}",
    "{product} with {details}, {lighting}, {background}, {quality}",
]

# ============================================================================
# NEGATIVE PROMPTS
# ============================================================================

NEGATIVE_PROMPTS = {
    "general": (
        "blurry, low quality, bad quality, poorly drawn, ugly, deformed, "
        "distorted, disfigured, bad anatomy, extra limbs, missing limbs, "
        "watermark, signature, text, logo, username, bad proportions"
    ),
    
    "portrait": (
        "blurry, ugly face, bad anatomy, bad hands, missing fingers, extra fingers, "
        "mutated hands, poorly drawn hands, poorly drawn face, deformed, "
        "bad proportions, extra limbs, disfigured, long neck, cross-eyed, "
        "watermark, signature, low quality, worst quality"
    ),
    
    "realistic": (
        "cartoon, anime, drawing, painting, sketch, low quality, worst quality, "
        "blurry, watermark, text, logo, signature, username, artificial, "
        "bad anatomy, distorted, oversaturated"
    ),
    
    "artistic": (
        "photograph, photo, realistic, photorealistic, blurry, low quality, "
        "bad quality, watermark, signature, username, text, ugly, distorted, "
        "bad composition, messy"
    ),
    
    "fantasy": (
        "realistic, photorealistic, modern, contemporary, blurry, low quality, "
        "bad anatomy, deformed, ugly, watermark, signature, text, "
        "poorly drawn, bad proportions"
    ),
    
    "minimal": (
        "cluttered, busy, complex, noisy, chaotic, watermark, signature, "
        "low quality, blurry, distorted, bad composition"
    ),
    
    "product": (
        "blurry, low quality, bad lighting, cluttered, messy background, "
        "watermark, text, logo, distorted, poor composition, noisy, "
        "grainy, unprofessional"
    ),
    
    "landscape": (
        "people, human, person, text, watermark, signature, blurry, "
        "low quality, bad quality, distorted, ugly, oversaturated, "
        "bad composition, cluttered"
    ),
    
    "clean": (
        "nsfw, nude, violence, gore, text, watermark, signature, "
        "low quality, blurry, distorted, ugly"
    ),
}

# ============================================================================
# STYLE PRESETS
# ============================================================================

STYLES = {
    "realistic": "hyperrealistic, photorealistic, highly detailed",
    "cinematic": "cinematic lighting, dramatic, film grain, depth of field",
    "anime": "anime style, manga, cel shaded, vibrant colors",
    "oil_painting": "oil painting, classical art, brush strokes, canvas texture",
    "watercolor": "watercolor painting, soft colors, fluid, artistic",
    "digital_art": "digital art, concept art, detailed, vibrant",
    "sketch": "pencil sketch, hand drawn, artistic, monochrome",
    "3d_render": "3D render, octane render, unreal engine, ray tracing",
    "pixel_art": "pixel art, 8-bit, retro gaming style",
    "impressionist": "impressionist painting, loose brush strokes, light focused",
    "noir": "film noir, black and white, high contrast, dramatic shadows",
    "steampunk": "steampunk aesthetic, Victorian era, brass and copper",
    "minimalist": "minimalist, clean, simple, elegant",
    "psychedelic": "psychedelic art, vibrant colors, surreal, trippy",
}

QUALITY_MODIFIERS = [
    "masterpiece, best quality, ultra detailed, 8k, sharp focus",
    "highly detailed, professional, award winning, 4k resolution",
    "stunning, beautiful, intricate details, high resolution",
    "premium quality, ultra high definition, crystal clear",
    "professional quality, detailed, sharp, vivid colors",
]

LIGHTING_OPTIONS = [
    "soft diffused lighting",
    "dramatic side lighting",
    "golden hour lighting",
    "studio lighting",
    "natural lighting",
    "neon lighting",
    "backlit",
    "rim lighting",
    "volumetric lighting",
    "cinematic lighting",
]

# ============================================================================
# CONTEXT-SPECIFIC PARAMETER OPTIONS
# ============================================================================

TEMPLATE_SPECIFIC_OPTIONS = {
    "Portrait": {
        "subject": ["a young woman", "a young man", "an elderly person", "a child", "a teenager", 
                   "a professional", "a warrior", "an artist", "a scientist"],
        "expression": ["smiling warmly", "serious and focused", "contemplative", "joyful laughter",
                      "mysterious smile", "confident gaze", "peaceful", "surprised"],
        "background": ["blurred bokeh", "studio backdrop", "urban environment", "natural setting",
                      "indoor setting", "dramatic clouds", "sunset sky", "abstract patterns"],
        "features": ["expressive eyes", "strong jawline", "gentle features", "distinctive style",
                    "professional attire", "casual clothing", "elegant outfit"],
    },
    
    "Landscape": {
        "location": ["mountain range", "ocean coastline", "forest clearing", "desert dunes",
                    "alpine meadow", "tropical beach", "canyon valley", "rolling hills", "lakeside"],
        "season": ["spring bloom", "summer sunshine", "autumn colors", "winter snow",
                  "rainy season", "harvest time"],
        "time_of_day": ["sunrise", "morning light", "midday sun", "afternoon glow", 
                       "sunset", "golden hour", "blue hour", "twilight", "night"],
        "weather": ["clear skies", "partly cloudy", "dramatic storm clouds", "misty fog",
                   "light rain", "snow falling", "rainbow after rain"],
        "elements": ["flowing water", "wildflowers", "ancient trees", "rock formations",
                    "distant mountains", "clouds reflecting in water", "winding path"],
    },
    
    "Fantasy": {
        "creature": ["majestic dragon", "ethereal phoenix", "mystical unicorn", "wise wizard",
                    "elven warrior", "fairy queen", "ancient griffin", "magical cat", "demon lord"],
        "setting": ["enchanted forest", "floating castle", "crystal caverns", "misty mountains",
                   "magical library", "ancient ruins", "fairy glen", "dark tower", "mystical realm"],
        "action": ["flying through", "casting spells in", "guarding", "emerging from",
                  "battling in", "resting in", "discovering"],
        "elements": ["glowing runes", "magical particles", "swirling mists", "floating crystals",
                    "enchanted weapons", "mystical aura", "ancient symbols", "magical flames"],
    },
    
    "Sci-Fi": {
        "subject": ["cyborg warrior", "space explorer", "AI android", "alien creature",
                   "hacker", "pilot", "scientist", "rebel fighter", "mutant"],
        "setting": ["neon-lit megacity", "space station", "alien planet", "cyberpunk alley",
                   "futuristic laboratory", "abandoned facility", "flying vehicle", "virtual reality"],
        "technology": ["holographic displays", "neural implants", "advanced weapons", "force fields",
                      "flying drones", "energy shields", "quantum computers", "teleportation device"],
        "action": ["hacking into", "fighting in", "exploring", "piloting through",
                  "escaping from", "discovering in"],
    },
    
    "Animal": {
        "animal": ["tiger", "lion", "eagle", "wolf", "elephant", "dolphin", "bear", "fox",
                  "owl", "deer", "leopard", "hawk", "whale", "snow leopard", "panda"],
        "habitat": ["dense jungle", "african savanna", "arctic tundra", "coral reef",
                   "mountain forest", "desert oasis", "rainforest canopy", "rocky mountains",
                   "open plains", "deep ocean"],
        "behavior": ["hunting prey", "resting peacefully", "playing", "drinking water",
                    "caring for young", "stalking", "flying", "swimming", "climbing"],
        "features": ["piercing eyes", "powerful build", "graceful movement", "majestic presence",
                    "sharp claws", "beautiful fur pattern", "impressive antlers", "sleek body"],
        "action": ["prowling through", "leaping across", "swimming in", "soaring over",
                  "running through", "resting in"],
    },
    
    "Architecture": {
        "building": ["modern skyscraper", "gothic cathedral", "ancient temple", "futuristic complex",
                    "art deco building", "minimalist structure", "classical palace", "brutalist tower"],
        "features": ["glass facade", "ornate columns", "geometric patterns", "curved lines",
                    "pointed arches", "steel beams", "marble details", "reflective surfaces"],
        "environment": ["urban skyline", "historic district", "waterfront", "mountain setting",
                       "desert landscape", "forest clearing", "city center"],
        "atmosphere": ["bustling and vibrant", "serene and peaceful", "dramatic and imposing",
                      "elegant and refined", "modern and sleek", "ancient and mystical"],
    },
    
    "Abstract": {
        "concept": ["consciousness", "time", "energy", "emotion", "nature", "technology",
                   "dreams", "music", "chaos", "harmony"],
        "elements": ["flowing lines", "geometric shapes", "particle effects", "light beams",
                    "color gradients", "fractal patterns", "swirling forms", "crystalline structures"],
        "colors": ["vibrant rainbow", "cool blue tones", "warm sunset hues", "monochrome",
                  "neon colors", "pastel palette", "earth tones", "metallic sheen"],
    },
    
    "Food": {
        "dish": ["gourmet pasta", "artisan pizza", "sushi platter", "dessert cake",
                "fresh salad", "grilled steak", "seafood platter", "breakfast spread",
                "exotic fruits", "handcrafted burger"],
        "presentation": ["rustic wooden board", "elegant white plate", "marble surface",
                        "slate platter", "colorful bowl", "minimalist setting", "vintage tray"],
        "garnish": ["fresh herbs", "edible flowers", "microgreens", "lemon wedge",
                   "sauce drizzle", "powdered sugar", "sesame seeds"],
        "ingredients": ["fresh vegetables", "premium meats", "artisan cheese", "exotic spices",
                       "seasonal produce", "seafood", "organic ingredients"],
        "setting": ["restaurant table", "kitchen counter", "outdoor picnic", "cafe setting",
                   "home dining", "food studio"],
    },
    
    "Character": {
        "character": ["warrior", "mage", "rogue", "knight", "samurai", "ninja", "archer",
                     "barbarian", "paladin", "necromancer", "druid", "monk"],
        "pose": ["heroic stance", "dynamic action", "combat ready", "sitting meditation",
                "walking forward", "casting spell", "drawing weapon", "defensive posture"],
        "outfit": ["ornate armor", "flowing robes", "leather outfit", "battle gear",
                  "casual clothes", "royal attire", "tribal costume", "modern tactical"],
        "features": ["battle scars", "glowing eyes", "magical aura", "weapon in hand",
                    "distinctive tattoos", "unique hairstyle", "facial markings"],
    },
    
    "Product": {
        "product": ["luxury watch", "smartphone", "perfume bottle", "designer shoes",
                   "headphones", "camera", "jewelry", "sunglasses", "laptop", "handbag"],
        "angle": ["front view", "side profile", "three-quarter view", "top-down",
                 "detail close-up", "angled perspective"],
        "surface": ["reflective glass", "marble stone", "wooden surface", "fabric backdrop",
                   "metallic platform", "gradient background"],
        "details": ["brand label visible", "premium materials", "sleek design", "intricate details",
                   "modern aesthetics", "luxury finish"],
    },
}

# Default options for fields not in specific categories
DEFAULT_FIELD_OPTIONS = {
    "subject": ["person", "warrior", "artist", "scientist", "child", "elder"],
    "location": ["outdoor setting", "indoor space", "natural environment", "urban area"],
    "setting": ["natural environment", "urban setting", "indoor space", "mystical realm"],
    "background": ["blurred background", "detailed environment", "solid color", "natural setting"],
}

# ============================================================================
# EXAMPLE USAGE
# ============================================================================

def format_prompt(template, **kwargs):
    """
    Format a template with provided keyword arguments.
    
    Args:
        template: A prompt template string with placeholders
        **kwargs: Keyword arguments to substitute into the template
        
    Returns:
        Formatted prompt string
    """
    try:
        return template.format(**kwargs)
    except KeyError as e:
        print(f"Warning: Missing placeholder {e}")
        return template

def get_random_prompt(template_list):
    """Get a random prompt template from a list."""
    import random
    return random.choice(template_list)

# ============================================================================
# EXAMPLE PROMPTS
# ============================================================================

EXAMPLE_PROMPTS = [
    {
        "name": "Fantasy Dragon Portrait",
        "template": FANTASY_TEMPLATES[0],
        "params": {
            "style": "digital art",
            "creature": "majestic dragon",
            "setting": "misty mountain peak",
            "mood": "epic and mysterious",
            "quality": "masterpiece, best quality, ultra detailed, 8k"
        },
        "negative": NEGATIVE_PROMPTS["fantasy"]
    },
    
    {
        "name": "Cyberpunk City",
        "template": SCI_FI_TEMPLATES[3],
        "params": {
            "subject": "flying cars",
            "setting": "neon-lit megacity",
            "lighting": "lights",
            "mood": "dystopian",
            "quality": "highly detailed, professional, 4k resolution"
        },
        "negative": NEGATIVE_PROMPTS["general"]
    },
    
    {
        "name": "Portrait Photography",
        "template": PORTRAIT_TEMPLATES[2],
        "params": {
            "subject": "a young woman with long flowing hair",
            "lighting": "soft diffused studio lighting",
            "background": "blurred bokeh background",
            "quality": "professional quality, sharp, 8k, detailed"
        },
        "negative": NEGATIVE_PROMPTS["portrait"]
    },
    
    {
        "name": "Mountain Landscape",
        "template": LANDSCAPE_TEMPLATES[0],
        "params": {
            "style": "oil painting",
            "location": "snow-capped mountain range",
            "time_of_day": "sunset",
            "weather": "clear sky with dramatic clouds",
            "quality": "masterpiece, intricate details, vibrant colors"
        },
        "negative": NEGATIVE_PROMPTS["landscape"]
    },
    
    {
        "name": "Gourmet Dish",
        "template": FOOD_TEMPLATES[0],
        "params": {
            "style": "professional",
            "dish": "artisan pizza with fresh ingredients",
            "presentation": "rustic wooden board",
            "lighting": "natural window light",
            "quality": "ultra detailed, 8k, sharp focus"
        },
        "negative": NEGATIVE_PROMPTS["product"]
    },
    
    {
        "name": "Wildlife Photography",
        "template": ANIMAL_TEMPLATES[2],
        "params": {
            "animal": "tiger",
            "features": "piercing amber eyes",
            "habitat": "dense jungle",
            "lighting": "dappled sunlight through trees",
            "quality": "wildlife photography, 8k, highly detailed"
        },
        "negative": NEGATIVE_PROMPTS["realistic"]
    },
    
    {
        "name": "Abstract Concept",
        "template": ABSTRACT_TEMPLATES[0],
        "params": {
            "style": "modern",
            "elements": "flowing geometric shapes",
            "colors": "vibrant blue and orange gradient",
            "mood": "energetic",
            "quality": "digital art, 4k, crisp"
        },
        "negative": NEGATIVE_PROMPTS["artistic"]
    },
    
    {
        "name": "Modern Architecture",
        "template": ARCHITECTURE_TEMPLATES[0],
        "params": {
            "style": "wide-angle",
            "building": "contemporary glass skyscraper",
            "time_of_day": "blue hour",
            "atmosphere": "dramatic and sleek",
            "quality": "architectural photography, 8k, professional"
        },
        "negative": NEGATIVE_PROMPTS["realistic"]
    },
    
    {
        "name": "Character Design",
        "template": CHARACTER_TEMPLATES[0],
        "params": {
            "style": "anime",
            "character": "warrior princess",
            "pose": "dynamic action pose",
            "outfit": "ornate armor with flowing cape",
            "background": "fantasy castle ruins",
            "quality": "detailed, vibrant colors, 4k"
        },
        "negative": NEGATIVE_PROMPTS["artistic"]
    },
    
    {
        "name": "Product Showcase",
        "template": PRODUCT_TEMPLATES[0],
        "params": {
            "style": "minimalist",
            "product": "luxury watch",
            "background": "gradient backdrop",
            "lighting": "dramatic key lighting",
            "quality": "commercial photography, ultra detailed, 8k"
        },
        "negative": NEGATIVE_PROMPTS["product"]
    },
]

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def print_example_prompts():
    """Print all example prompts with their formatted outputs."""
    print("=" * 80)
    print("EXAMPLE PROMPTS FOR IMAGE GENERATION")
    print("=" * 80)
    print()
    
    for i, example in enumerate(EXAMPLE_PROMPTS, 1):
        prompt = format_prompt(example["template"], **example["params"])
        print(f"Example {i}: {example['name']}")
        print("-" * 80)
        print(f"Template: {example['template']}")
        print()
        print(f"Formatted Prompt:")
        print(f"  {prompt}")
        print()
        print(f"Negative Prompt:")
        print(f"  {example['negative']}")
        print()
        print("=" * 80)
        print()

def create_custom_prompt(template_category, **kwargs):
    """
    Create a custom prompt from a template category.
    
    Args:
        template_category: Name of template list (e.g., 'PORTRAIT_TEMPLATES')
        **kwargs: Parameters to fill into the template
        
    Returns:
        Formatted prompt string
    """
    templates = globals().get(template_category.upper())
    if templates:
        template = get_random_prompt(templates)
        return format_prompt(template, **kwargs)
    else:
        raise ValueError(f"Unknown template category: {template_category}")

# ============================================================================
# MAIN (for testing)
# ============================================================================

if __name__ == "__main__":
    print_example_prompts()
    
    # Example of creating a custom prompt
    print("\nCUSTOM PROMPT EXAMPLE:")
    print("-" * 80)
    custom = create_custom_prompt(
        "portrait_templates",
        style="watercolor",
        subject="a wise old wizard",
        lighting="soft moonlight",
        quality="masterpiece, detailed, ethereal",
        camera_details="50mm lens, f/2.8",
        mood="mystical",
        expression="contemplative gaze",
        features="long white beard",
        background="starry night sky"
    )
    print(f"Generated: {custom}")
    print()
    print(f"Suggested Negative: {NEGATIVE_PROMPTS['artistic']}")

