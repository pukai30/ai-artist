# ⚡ Simplified 2-Step Workflow

## Overview

The AI Artist app now has a **clear, simple 2-step process**:

```
Step 1: Load AI Model (one-time per session)
   ↓
Step 2: Generate Images (as many as you want)
```

---

## 🎯 Complete User Flow

### When You First Open the App:

```
┌──────────────────────────────────────────┐
│   🎨 AI Artist - Prompt Builder         │
├──────────────────────────────────────────┤
│                                          │
│   ⚡ Step 1: Load AI Model               │
│                                          │
│   ℹ️ Before generating images, we need  │
│   to load the Stable Diffusion model.   │
│                                          │
│   This is a one-time step per session.  │
│   First-time use will download ~4GB     │
│   model (takes 2-5 minutes).            │
│                                          │
│      [🚀 Load Stable Diffusion Model]   │
│                                          │
│   ─────────────────────────────────────  │
│   ⚠️ Please load the model first to     │
│   continue. The rest of the interface   │
│   will appear after the model is loaded.│
│                                          │
└──────────────────────────────────────────┘

[Nothing else shown until model loads]
```

---

### After Model Loads Successfully:

```
┌──────────────────────────────────────────┐
│   🎨 AI Artist - Prompt Builder         │
├──────────────────────────────────────────┤
│   ✅ Model Loaded - Ready to Generate!  │
│   ─────────────────────────────────────  │
│                                          │
│   🎯 Template Selection                 │
│   [Full interface appears here]         │
│                                          │
│   🚫 What to Avoid                      │
│   [...]                                  │
│                                          │
│   ⚙️ Template Parameters                │
│   [...]                                  │
│                                          │
│   👁️ Prompt Preview                     │
│   [...]                                  │
│                                          │
│   🖼️ Step 2: Generate Image             │
│   [🚀 Generate Image Now]               │
│                                          │
└──────────────────────────────────────────┘
```

---

## 📋 Step-by-Step Instructions

### STEP 1: Load the Model

1. **Open the app:**
   ```bash
   uv run streamlit run streamlit_app.py
   ```

2. **You'll see:**
   - Big blue button: "🚀 Load Stable Diffusion Model"
   - Info message explaining what it does
   - Nothing else (interface hidden until model loads)

3. **Click the button:**
   - Spinner shows: "⏳ Loading model..."
   - **Check terminal** to see loading progress
   - Wait 2-5 minutes (first time) or 30 seconds (cached)

4. **Model loads:**
   - See: "✅ Model loaded successfully!"
   - Page refreshes
   - Full interface appears

---

### STEP 2: Generate Images

**Now the full workflow is available:**

1. **Select Template** (e.g., "Character")
2. **Choose What to Avoid** (negative prompt type)
3. **Configure Style/Lighting/Mood**
4. **Fill Template Fields** (context-aware dropdowns)
5. **Generate Preview** (see prompt + token count)
6. **Adjust Parameters** (steps, guidance, seed)
7. **Generate Image** → Click "🚀 Generate Image Now"
8. **View Results** (image + metadata)

---

## 🎨 Visual Flow

```
START
  ↓
[Open App]
  ↓
╔════════════════════════════════╗
║  Step 1: Load AI Model         ║
║  [🚀 Load Model Button]        ║
╚════════════════════════════════╝
  ↓ (Click & Wait 2-5 min)
  ↓
✅ Model Loaded!
  ↓
╔════════════════════════════════╗
║  Full Interface Appears        ║
║                                ║
║  1. Select Template            ║
║  2. Configure Parameters       ║
║  3. Generate Preview           ║
║  4. Step 2: Generate Image     ║
║     [🚀 Generate Image Now]    ║
╚════════════════════════════════╝
  ↓ (Click & Wait 30-60 sec)
  ↓
🖼️ Image Generated!
  ↓
[View, Save, Create More]
```

---

## 💡 Key Improvements

### ✅ Clear Steps
- Step 1 labeled clearly
- Step 2 labeled clearly
- No confusion about order

### ✅ Progressive Disclosure
- Only show model loading first
- Hide rest of interface until ready
- Reduces overwhelm

### ✅ Better UX
- Can't try to generate without model
- Clear what to do first
- Smooth progression

### ✅ Error Handling
- Better error messages
- Detailed diagnostics in terminal
- Helpful suggestions

---

## 🔧 Troubleshooting

### If Model Loading Fails:

1. **Check terminal output** for detailed error
2. **Run diagnostic:**
   ```bash
   uv run python diagnose_model.py
   ```
3. **See:** `TROUBLESHOOTING_MODEL_LOAD.md`

### Common Issues:

| Issue | Solution |
|-------|----------|
| Network error | Check internet, retry |
| Out of memory | Close other apps, use 512x512 |
| Disk space | Free up 5GB+ |
| Missing deps | Run `uv sync` |

---

## 📝 What Changed

### Before:
```
- Load model button hidden in generation section
- Could navigate entire UI before loading
- Confusing when model wasn't loaded
- Generate button visibility issues
```

### After:
```
✅ Model loading is FIRST thing you see
✅ Can't proceed until model loads
✅ Clear 2-step process
✅ Better error handling
✅ Simplified workflow
```

---

## 🚀 Quick Start

### Complete Workflow:

```bash
# 1. Start app
uv run streamlit run streamlit_app.py

# 2. In browser - Click "Load Model"
# 3. Wait for loading (watch terminal)
# 4. Create prompts
# 5. Generate images
# 6. Enjoy!
```

---

## ✅ Benefits

### For New Users:
- Clear what to do first
- Can't skip important steps
- Less confusion

### For All Users:
- Faster workflow once model loaded
- No hunting for buttons
- Clear visual feedback

### For Troubleshooting:
- Better error messages
- Diagnostic script available
- Terminal shows details

---

**🎉 Simplified to 2 Clear Steps!**

1. **Load Model** (one-time)
2. **Generate Images** (unlimited)

Simple, clear, and easy to use!

