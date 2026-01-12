# 🧠 Innerverse: Advanced NLP & Emotion Intelligence

This module represents the "Option B" upgrade, moving the engine from basic sentiment analysis to **Intent-Based Emotion Classification**.

## 🚀 How it Works: The "Triple-Check" System

Instead of guessing based on a single polarity score, the engine now processes user input through three distinct layers:

### 1. Intent Detection (The "What")

The engine scans for **Sentence Starters** and patterns derived from clinical communication guides.

- **Purpose:** Identifies specific states like _Overwhelmed, Anxiety, or Gratitude_ that standard NLP often misreads.
- **Logic:** Uses the `INTENT_PATTERNS` dictionary to find explicit emotional declarations.

### 2. Intensity Multiplier (The "Volume")

The engine looks for "Adverbial Modifiers" to determine how loud the emotion is.

- **Low (0.5x):** "kinda", "a little", "sort of" → Softens the weather.
- **Medium (1.5x):** "really", "very", "so" → Heightens the weather.
- **High (2.0x):** "totally", "extremely", "pissed off" → Forces a **THUNDERSTORM**.

### 3. Sentiment Fallback (The "Math")

If no specific intent is found, the engine falls back to `TextBlob` polarity.

- **Innovation:** The Intensity Multiplier is still applied to the math, ensuring "I am so happy" gets a higher score than "I am happy."

---

## 📊 The Emotion Matrix

The weather is no longer just "Positive vs Negative." It is now mapped to specific emotional categories:

| Emotion         | Weather State | Trigger Example             |
| :-------------- | :------------ | :-------------------------- |
| **ANGER**       | THUNDERSTORM  | "I'm pissed off because..." |
| **OVERWHELMED** | THUNDERSTORM  | "Too much on my plate..."   |
| **ANXIETY**     | FOGGY MIST    | "I'm worried that..."       |
| **CONFUSION**   | FOGGY MIST    | "I don't get it..."         |
| **SADNESS**     | STEADY RAIN   | "I'm hurting right now..."  |
| **GRATITUDE**   | RADIANT SUN   | "I really appreciate..."    |

---

## 🛠️ Updated Functions in `engine.py`

- `detect_intent(user_text)`: Maps text to the Emotion Matrix.
- `get_intensity_multiplier(user_text)`: Calculates the "Emotional Volume."
- `translate_score_to_weather()`: The master logic gate that prioritizes Intent over Math.
