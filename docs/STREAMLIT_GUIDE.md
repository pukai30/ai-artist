# AI Artist - Streamlit UI Guide

## 🚀 Quick Start

### Installation

First, install the required dependencies:

```bash
# Using pip
pip install streamlit

# Or if using uv (already in pyproject.toml)
uv sync
```

### Running the App

```bash
streamlit run streamlit_app.py
```

The app will automatically open in your default browser at `http://localhost:8501`

## 🎨 Features

### 1. **Template Selection** (Sidebar)
- Choose from 10 template categories:
  - Portrait
  - Landscape
  - Fantasy
  - Sci-Fi
  - Animal
  - Architecture
  - Abstract
  - Food
  - Character
  - Product
- Each category has 5 different template variations

### 2. **Style Options** (Sidebar)
- Select from 14 predefined style presets:
  - Realistic
  - Cinematic
  - Anime
  - Oil Painting
  - Watercolor
  - Digital Art
  - Sketch
  - 3D Render
  - Pixel Art
  - Impressionist
  - Film Noir
  - Steampunk
  - Minimalist
  - Psychedelic
- Or enter a custom style

### 3. **Lighting Options** (Sidebar)
- Choose from 10 lighting presets:
  - Soft diffused lighting
  - Dramatic side lighting
  - Golden hour lighting
  - Studio lighting
  - Natural lighting
  - Neon lighting
  - Backlit
  - Rim lighting
  - Volumetric lighting
  - Cinematic lighting
- Or enter custom lighting

### 4. **Negative Prompts** (Sidebar)
- Select from 9 predefined negative prompt types:
  - General
  - Portrait
  - Realistic
  - Artistic
  - Fantasy
  - Minimal
  - Product
  - Landscape
  - Clean
- Add custom negative terms

### 5. **Dynamic Template Parameters** (Main Area)
- The app automatically detects placeholders in the selected template
- Provides intelligent input methods:
  - **Dropdowns** for common fields (style, lighting, mood, etc.)
  - **Text inputs** for custom descriptions
  - **Smart suggestions** based on placeholder type
- Fields automatically populated for style and lighting if presets are selected

### 6. **Prompt Preview** (Main Area)
- Real-time preview of the generated prompt
- Shows both positive and negative prompts
- Displays prompts in copyable code blocks
- Configure generation parameters:
  - Inference steps (10-100)
  - Guidance scale (1.0-20.0)
  - Random seed

### 7. **Image Generation Section**
- Select image size (512x512, 768x768, 512x768, 768x512)
- Choose number of images (1-4)
- Shows generation configuration in JSON format
- Placeholder for actual image generation (to be implemented)

## 📋 Usage Flow

1. **Select Template Category** → Choose the type of image (e.g., Portrait)
2. **Select Specific Template** → Pick a template variation
3. **Configure Style & Lighting** → Choose presets or enter custom values
4. **Select Negative Prompt** → Choose what to exclude
5. **Fill Template Parameters** → Complete all required fields
6. **Generate Preview** → Click to see formatted prompt
7. **Adjust Generation Parameters** → Set steps, guidance, seed
8. **Generate Image** → (Coming soon - integration phase)

## 🎯 Example Workflow

### Creating a Fantasy Dragon Portrait:

1. **Sidebar Settings:**
   - Template Category: `Fantasy`
   - Template: `Template 1`
   - Style Preset: `Digital Art`
   - Lighting Preset: `Dramatic side lighting`
   - Negative Prompt: `Fantasy`

2. **Template Parameters:**
   - Creature: `majestic dragon`
   - Setting: `misty mountain peak`
   - Mood: `epic and mysterious`
   - Quality: Select from dropdown

3. **Generate Preview** → View formatted prompt

4. **Generation Parameters:**
   - Steps: `30`
   - Guidance Scale: `7.5`
   - Seed: `42`

5. **Generate Image** → (Placeholder - will integrate later)

## 🔧 Integration with Image Generation

The UI is designed to be easily integrated with your existing `main.py`. The generation section collects all necessary parameters:

```python
{
    "prompt": "Generated positive prompt...",
    "negative_prompt": "Generated negative prompt...",
    "steps": 30,
    "guidance_scale": 7.5,
    "seed": 42,
    "size": "512x512",
    "num_images": 1
}
```

## 💡 Tips

- **Style Presets** automatically fill the `{style}` placeholder
- **Lighting Presets** automatically fill the `{lighting}` placeholder
- **Quality Modifiers** provide professional-grade quality descriptions
- Use **Custom options** for complete creative control
- Copy prompts directly from the code blocks for external use

## 🎨 Customization

You can extend the functionality by:
- Adding more templates to `prompt_temp.py`
- Creating new style presets
- Adding more negative prompt variations
- Customizing the UI layout and styling

## 📝 Notes

- All prompts are formatted using the templates from `prompt_temp.py`
- The app validates that all required fields are filled before generating preview
- Placeholder images are shown in the generation section until integration
- The app uses session state to maintain prompt data across interactions

