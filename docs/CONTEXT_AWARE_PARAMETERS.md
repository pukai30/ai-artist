# 🎯 Context-Aware Template Parameters

## Major Update - Smart Dropdown Values

The template parameters now provide **context-specific dropdown options** based on the selected template category. No more generic suggestions!

---

## What Changed?

### ✅ Before (Generic):
```
Animal Template selected
Parameters show:
- Animal: [text input - type anything]
- Habitat: [text input - type anything]
- Behavior: [generic action list]
```

### ✅ After (Context-Aware):
```
Animal Template selected
Parameters show:
- Animal: [tiger, lion, eagle, wolf, elephant, dolphin...]
- Habitat: [dense jungle, african savanna, arctic tundra...]
- Behavior: [hunting prey, resting peacefully, playing...]
```

---

## Template-Specific Options

### 1. Portrait Templates

**Optimized for:** Human portraits, character close-ups

**Context-Specific Fields:**
- **Subject:** a young woman, a young man, elderly person, child, warrior, artist, scientist
- **Expression:** smiling warmly, serious, contemplative, joyful, mysterious, confident
- **Background:** blurred bokeh, studio backdrop, urban environment, natural setting
- **Features:** expressive eyes, strong jawline, gentle features, professional attire

**Example:** 
```
Template: "a {style} portrait of {subject}, {expression}, {background}"
Dropdown suggestions tailored for portraits!
```

---

### 2. Landscape Templates

**Optimized for:** Nature scenes, scenic views

**Context-Specific Fields:**
- **Location:** mountain range, ocean coastline, forest clearing, desert dunes, alpine meadow
- **Season:** spring bloom, summer sunshine, autumn colors, winter snow
- **Time of Day:** sunrise, morning light, midday sun, afternoon glow, sunset, golden hour
- **Weather:** clear skies, dramatic storm clouds, misty fog, light rain, snow falling
- **Elements:** flowing water, wildflowers, ancient trees, rock formations, winding path

---

### 3. Fantasy Templates

**Optimized for:** Magical scenes, mythical creatures

**Context-Specific Fields:**
- **Creature:** majestic dragon, ethereal phoenix, mystical unicorn, wise wizard, elven warrior
- **Setting:** enchanted forest, floating castle, crystal caverns, misty mountains, ancient ruins
- **Action:** flying through, casting spells in, guarding, emerging from, battling in
- **Elements:** glowing runes, magical particles, swirling mists, floating crystals, mystical aura

---

### 4. Sci-Fi Templates

**Optimized for:** Futuristic scenes, technology

**Context-Specific Fields:**
- **Subject:** cyborg warrior, space explorer, AI android, alien creature, hacker, pilot
- **Setting:** neon-lit megacity, space station, alien planet, cyberpunk alley, virtual reality
- **Technology:** holographic displays, neural implants, advanced weapons, flying drones
- **Action:** hacking into, fighting in, exploring, piloting through, escaping from

---

### 5. Animal Templates

**Optimized for:** Wildlife, creatures

**Context-Specific Fields:**
- **Animal:** tiger, lion, eagle, wolf, elephant, dolphin, bear, fox, owl, leopard, panda
- **Habitat:** dense jungle, african savanna, arctic tundra, coral reef, mountain forest
- **Behavior:** hunting prey, resting peacefully, playing, caring for young, stalking
- **Features:** piercing eyes, powerful build, graceful movement, majestic presence
- **Action:** prowling through, leaping across, swimming in, soaring over

---

### 6. Architecture Templates

**Optimized for:** Buildings, structures

**Context-Specific Fields:**
- **Building:** modern skyscraper, gothic cathedral, ancient temple, futuristic complex
- **Features:** glass facade, ornate columns, geometric patterns, curved lines, marble details
- **Environment:** urban skyline, historic district, waterfront, mountain setting
- **Atmosphere:** bustling and vibrant, serene and peaceful, dramatic and imposing

---

### 7. Abstract Templates

**Optimized for:** Non-representational art

**Context-Specific Fields:**
- **Concept:** consciousness, time, energy, emotion, nature, technology, dreams, harmony
- **Elements:** flowing lines, geometric shapes, particle effects, light beams, fractals
- **Colors:** vibrant rainbow, cool blue tones, warm sunset hues, neon colors, metallic sheen

---

### 8. Food Templates

**Optimized for:** Culinary photography

**Context-Specific Fields:**
- **Dish:** gourmet pasta, artisan pizza, sushi platter, dessert cake, grilled steak
- **Presentation:** rustic wooden board, elegant white plate, marble surface, slate platter
- **Garnish:** fresh herbs, edible flowers, microgreens, lemon wedge, sauce drizzle
- **Ingredients:** fresh vegetables, premium meats, artisan cheese, exotic spices
- **Setting:** restaurant table, kitchen counter, outdoor picnic, cafe setting

---

### 9. Character Templates

**Optimized for:** Full-body character designs

**Context-Specific Fields:**
- **Character:** warrior, mage, rogue, knight, samurai, ninja, archer, barbarian, paladin
- **Pose:** heroic stance, dynamic action, combat ready, walking forward, casting spell
- **Outfit:** ornate armor, flowing robes, leather outfit, battle gear, royal attire
- **Features:** battle scars, glowing eyes, magical aura, weapon in hand, distinctive tattoos

---

### 10. Product Templates

**Optimized for:** Product photography

**Context-Specific Fields:**
- **Product:** luxury watch, smartphone, perfume bottle, designer shoes, headphones, camera
- **Angle:** front view, side profile, three-quarter view, top-down, detail close-up
- **Surface:** reflective glass, marble stone, wooden surface, metallic platform
- **Details:** brand label visible, premium materials, sleek design, luxury finish

---

## How It Works

### Technical Flow:

1. **User selects template category** → "Animal"
2. **System extracts required fields** → {animal}, {habitat}, {behavior}
3. **System checks for context-specific options** → Found in TEMPLATE_SPECIFIC_OPTIONS["Animal"]
4. **Dropdowns populated with relevant values** → Animal-specific choices
5. **User selects from contextual options** → Much easier!

### Code Implementation:

```python
# In prompt_temp.py
TEMPLATE_SPECIFIC_OPTIONS = {
    "Animal": {
        "animal": ["tiger", "lion", "eagle"...],
        "habitat": ["dense jungle", "savanna"...],
        "behavior": ["hunting", "resting"...]
    },
    # ... other categories
}

# In streamlit_app.py
def get_placeholder_suggestions(placeholder, category):
    # First check category-specific options
    if category in TEMPLATE_SPECIFIC_OPTIONS:
        if placeholder in TEMPLATE_SPECIFIC_OPTIONS[category]:
            return TEMPLATE_SPECIFIC_OPTIONS[category][placeholder]
    
    # Fallback to defaults
    return DEFAULT_FIELD_OPTIONS.get(placeholder, [])
```

---

## User Experience Improvements

### ✅ Faster Input
- No typing needed
- Select from relevant options
- Fewer errors

### ✅ Better Results
- Suggestions proven to work well
- Category-optimized choices
- Professional quality

### ✅ Learning Tool
- See what works for each category
- Discover new ideas
- Build expertise

### ✅ Consistency
- Standardized terminology
- Best practices built-in
- Professional standards

---

## Example Workflows

### Example 1: Creating Animal Portrait

1. **Select Category:** Animal
2. **Select Template:** Template 3 (majestic {animal} with {features})
3. **See Context-Aware Dropdowns:**
   - Animal: [Select from 15 animals] → Choose "snow leopard"
   - Features: [Select from 8 feature options] → Choose "piercing eyes and thick spotted fur"
4. **Result:** Professional, coherent prompt!

### Example 2: Creating Landscape

1. **Select Category:** Landscape  
2. **Select Template:** Template 1 (a {style} landscape of {location})
3. **See Context-Aware Dropdowns:**
   - Location: [Select from 9 locations] → Choose "alpine meadow"
   - Season: [Select from 6 seasons] → Choose "spring bloom"
   - Weather: [Select from 7 weather options] → Choose "partly cloudy"
4. **Result:** Beautiful, specific prompt!

### Example 3: Creating Sci-Fi Scene

1. **Select Category:** Sci-Fi
2. **Select Template:** Template 1 (a {style} depiction of {subject} in {setting})
3. **See Context-Aware Dropdowns:**
   - Subject: [Select from 9 sci-fi subjects] → Choose "AI android"
   - Setting: [Select from 8 futuristic settings] → Choose "neon-lit megacity"
   - Technology: [Select from 8 tech options] → Choose "holographic displays"
4. **Result:** Cohesive sci-fi prompt!

---

## Benefits

### For Beginners:
- ✅ No need to know terminology
- ✅ Learn by seeing options
- ✅ Guaranteed good results
- ✅ Fast prompt creation

### For Advanced Users:
- ✅ Quick selection of proven combinations
- ✅ Consistent quality
- ✅ Time-saving
- ✅ Still can use custom option

### For All Users:
- ✅ Better image quality
- ✅ More professional prompts
- ✅ Less trial and error
- ✅ Enjoyable experience

---

## Visual Indicator

When using context-aware parameters, you'll see:

```
📝 Template-Specific Fields
💡 Dropdown values are tailored for Animal templates

[Animal dropdown with animal-specific options]
[Habitat dropdown with habitat-specific options]
```

This indicator confirms you're getting category-optimized suggestions!

---

## Fallback Behavior

If a field doesn't have category-specific options:
1. System checks DEFAULT_FIELD_OPTIONS
2. If not found, provides generic suggestions
3. Always has custom input option as fallback

**You're never stuck!**

---

## Custom Input Still Available

Don't like the suggestions? You can still:
- ✅ Check "Custom" checkbox
- ✅ Type your own value
- ✅ Complete creative freedom

**Best of both worlds!**

---

## Statistics

### Total Context-Specific Options Added:

- **Portrait:** 4 fields, ~30 options
- **Landscape:** 5 fields, ~40 options  
- **Fantasy:** 4 fields, ~30 options
- **Sci-Fi:** 4 fields, ~30 options
- **Animal:** 5 fields, ~40 options
- **Architecture:** 4 fields, ~30 options
- **Abstract:** 3 fields, ~25 options
- **Food:** 5 fields, ~40 options
- **Character:** 4 fields, ~35 options
- **Product:** 4 fields, ~30 options

**Total: ~330 context-specific options across 10 categories!**

---

## Testing

### How to Test:

1. **Run the app**
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Test Animal Category:**
   - Select "Animal" category
   - Select Template 3
   - Check "Animal" dropdown → See animal-specific options
   - Check "Habitat" dropdown → See habitat-specific options
   - Verify options make sense for animals

3. **Test Landscape Category:**
   - Select "Landscape" category
   - Select Template 1
   - Check "Location" dropdown → See landscape locations
   - Check "Season" dropdown → See season-specific options

4. **Test Each Category:**
   - Repeat for all 10 categories
   - Verify dropdowns show relevant options
   - Test custom input still works

---

## Future Enhancements

Potential additions:
- 🔮 AI-powered suggestions based on previous selections
- 🔮 Favorite combinations saved
- 🔮 Community-contributed options
- 🔮 More granular subcategories
- 🔮 Dynamic option filtering

---

## Summary

### What You Get:
- ✅ 330+ context-specific dropdown options
- ✅ 10 fully optimized template categories
- ✅ Smart, relevant suggestions
- ✅ Faster prompt creation
- ✅ Better results

### How It Helps:
- 🎯 No more guessing
- 🎯 Professional quality built-in
- 🎯 Learn as you go
- 🎯 Save time
- 🎯 Better images

---

**🎉 Context-Aware Parameters Active!**

Your template parameters now intelligently adapt to provide the most relevant options for each category!

