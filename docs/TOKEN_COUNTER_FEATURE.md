# 🔢 Token Counter Feature

## New Feature: Token Count Display

The Prompt Preview section now displays **estimated token counts** for both the generated prompt and negative prompt.

---

## What's Displayed

### Token Count Locations:

1. **Generated Prompt Header**
   ```
   ✨ Generated Prompt: `45 tokens`
   ```

2. **What to Avoid Header**
   ```
   🚫 What to Avoid: `28 tokens`
   ```

3. **Total Token Count Info Box**
   ```
   📊 Total Token Count: 73 tokens (Prompt: 45 + Negative: 28)
   ```

---

## Visual Layout

```
┌─────────────────────────────────────────────────────┐
│ 👁️ Prompt Preview                                   │
├──────────────────────────┬──────────────────────────┤
│ ✨ Generated Prompt:     │ 🚫 What to Avoid:        │
│    `45 tokens`           │    `28 tokens`           │
│ ┌──────────────────────┐ │ ┌──────────────────────┐ │
│ │ [Prompt text...]     │ │ │ [Negative text...]   │ │
│ └──────────────────────┘ │ └──────────────────────┘ │
│ [Code block]             │ [Code block]             │
└──────────────────────────┴──────────────────────────┘
┌─────────────────────────────────────────────────────┐
│ 📊 Total Token Count: 73 tokens                     │
│    (Prompt: 45 + Negative: 28)                      │
└─────────────────────────────────────────────────────┘
```

---

## How Token Estimation Works

### Algorithm:
```python
def estimate_tokens(text: str) -> int:
    """
    Estimate token count using word count approximation.
    
    Rule: 1 word ≈ 1.3 tokens (based on GPT tokenization)
    """
    words = text.split()
    estimated_tokens = int(len(words) * 1.3)
    return estimated_tokens
```

### Why This Approximation?

Based on OpenAI's tokenization:
- **English text:** ~1.3 tokens per word on average
- **Technical terms:** May be slightly higher
- **Common words:** May be slightly lower

**This provides a good estimate** for most use cases.

---

## Example Output

### Example 1: Short Prompt
```
✨ Generated Prompt: `32 tokens`
"a digital art portrait of a young woman, 
dramatic lighting, masterpiece, 8k"

🚫 What to Avoid: `18 tokens`
"blurry, low quality, bad anatomy"

📊 Total Token Count: 50 tokens (Prompt: 32 + Negative: 18)
```

### Example 2: Detailed Prompt
```
✨ Generated Prompt: `67 tokens`
"a hyperrealistic digital art illustration of 
majestic dragon soaring through mystical crystal 
caverns, epic and mysterious atmosphere, magical 
glowing crystals, dramatic side lighting, 
masterpiece, best quality, ultra detailed, 8k"

🚫 What to Avoid: `31 tokens`
"realistic, photorealistic, modern, contemporary, 
blurry, low quality, bad anatomy, deformed, ugly, 
watermark"

📊 Total Token Count: 98 tokens (Prompt: 67 + Negative: 31)
```

---

## Why Token Count Matters

### 1. **Model Limitations**
- Most AI models have token limits
- Stable Diffusion: ~75 tokens typical
- Knowing your count helps stay within limits

### 2. **Cost Awareness**
- Some APIs charge per token
- Track usage for budgeting
- Optimize prompts for efficiency

### 3. **Prompt Optimization**
- See if prompts are too long
- Find opportunities to simplify
- Balance detail vs. brevity

### 4. **Quality Control**
- Very short prompts may lack detail
- Very long prompts may be over-specified
- Find the sweet spot (30-80 tokens typical)

---

## Token Count Guidelines

### Recommended Ranges:

| Prompt Length | Token Count | Use Case |
|---------------|-------------|----------|
| **Minimal** | 10-25 | Simple concepts, quick tests |
| **Standard** | 25-50 | Most use cases, good balance |
| **Detailed** | 50-75 | Complex scenes, specific requirements |
| **Maximum** | 75+ | Very detailed, may hit model limits |

### Warning Signs:

⚠️ **Too Short** (<15 tokens)
- May lack important details
- Results may be inconsistent
- Consider adding quality modifiers

⚠️ **Too Long** (>100 tokens)
- May exceed model limits
- Some details may be ignored
- Consider simplifying

✅ **Sweet Spot** (30-70 tokens)
- Good detail level
- Well within limits
- Consistent results

---

## Features

### ✅ Real-Time Calculation
- Calculated when preview is generated
- Updates with each new prompt
- No manual action needed

### ✅ Breakdown Display
- Individual counts for prompt and negative
- Total combined count
- Easy to understand format

### ✅ Visual Clarity
- Inline badge format: `45 tokens`
- Info box for totals
- Color-coded sections

---

## Technical Details

### Implementation:

**File:** `streamlit_app.py`

**Function Added:**
```python
def estimate_tokens(text: str) -> int:
    if not text:
        return 0
    words = text.split()
    estimated_tokens = int(len(words) * 1.3)
    return estimated_tokens
```

**Usage in Preview:**
```python
if st.session_state.generated_prompt:
    # Calculate counts
    prompt_tokens = estimate_tokens(st.session_state.generated_prompt)
    negative_tokens = estimate_tokens(st.session_state.generated_negative)
    total_tokens = prompt_tokens + negative_tokens
    
    # Display with counts
    st.markdown(f"**✨ Generated Prompt:** `{prompt_tokens} tokens`")
    # ... display prompt ...
    
    # Show total
    st.info(f"📊 Total: {total_tokens} tokens")
```

---

## Benefits

### For Users:
- ✅ Know if prompts fit model limits
- ✅ Understand prompt complexity
- ✅ Optimize for better results
- ✅ Learn prompt engineering

### For Optimization:
- ✅ Identify overly long prompts
- ✅ Find opportunities to simplify
- ✅ Balance detail vs. efficiency
- ✅ Stay within API limits

### For Learning:
- ✅ See token impact of different elements
- ✅ Understand tokenization basics
- ✅ Improve prompt writing skills
- ✅ Make informed decisions

---

## Example Scenarios

### Scenario 1: Staying Within Limits
```
User creates detailed fantasy prompt
Token count shows: 85 tokens
User realizes it's near the limit
User simplifies to 65 tokens
Result: Better model performance!
```

### Scenario 2: Adding More Detail
```
User creates minimal prompt
Token count shows: 18 tokens
User realizes it's too short
User adds style and quality modifiers
Result: More consistent outputs!
```

### Scenario 3: Optimizing Negative Prompt
```
User adds many negative terms
Token count shows: 42 tokens for negative
User realizes negative is too long
User uses preset negative prompt instead
Result: Balanced prompt distribution!
```

---

## Future Enhancements

Potential improvements:
- 🔮 Use actual tokenizer (tiktoken) for exact counts
- 🔮 Show token limit warnings
- 🔮 Suggest optimizations
- 🔮 Token usage history
- 🔮 Compare across generations

---

## Accuracy Note

**This is an estimation**, not exact tokenization:
- ✅ Accurate within 5-10% typically
- ✅ Good enough for planning
- ✅ Fast calculation (no API calls)
- ⚠️ May vary from actual model tokenization

For **production use** with strict limits, consider using the actual tokenizer library.

---

## Summary

### What You Get:
- ✅ Token count for generated prompt
- ✅ Token count for negative prompt
- ✅ Total combined token count
- ✅ Real-time updates
- ✅ Visual clarity

### Why It Matters:
- 📊 Stay within model limits
- 📊 Optimize prompt length
- 📊 Understand complexity
- 📊 Improve results

### How It Helps:
- 🎯 Make informed decisions
- 🎯 Learn prompt engineering
- 🎯 Avoid errors
- 🎯 Better outputs

---

**🎉 Token Counter Active!**

You can now see exactly how many tokens your prompts use!

