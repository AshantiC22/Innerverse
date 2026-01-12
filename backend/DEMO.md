# 🛸 Innerverse: System Demo & Logic Documentation

This document serves as the technical manual and proof-of-work for the Innerverse "Brain" (v1.5).

## 🧠 Core System Architecture

### 1. The Engine (`engine.py`)

The central orchestrator that manages the flow from user input to emotional output.

- **Intent Detection:** Uses NLP pattern matching to identify specific emotions like ANGER or GRATITUDE.
- **Intensity Multiplier:** Scans for modifiers (e.g., "totally", "extremely") to amplify the emotional "volume".
- **Sentiment Fallback:** Uses TextBlob polarity math when no specific intent pattern is recognized.

### 2. The Safety Firewall (Crisis Intercept)

A prioritized guardrail designed to protect the user in high-risk moments.

- **Logic:** If a crisis keyword is detected, the program triggers an immediate "Safety Path".
- **Result:** Displays 988 Lifeline resources and **blocks** all secondary logic (journaling, weather, and clinical assessments) to ensure user safety.

### 3. Avatar Skills & Interventions (`avatar.py`)

The digital companion module providing real-time support based on detected emotional states.

- **Guided Breathing:** Triggered by `OVERWHELMED`. Uses timed `time.sleep` intervals for a 4-4-4-4 box breathing cycle.
- **Interactive Grounding (5-4-3-2-1):** Triggered by `ANXIETY` or `FOGGY MIST`. This skill uses a **nested loop** to prompt the user for individual sensory inputs one-by-one, forcing a slow, meditative focus.

### 4. Persistence & History (`view_history.py`)

- **Storage:** Saves every entry locally to `journal.json`.
- **Visualization:** A utility that renders a summary table of weather trends and provides health insights.

---

## 🧪 Verified Demo Test Cases

| Test Case       | User Input Pattern             | Expected Weather | Avatar Action              | Safety Gate              |
| :-------------- | :----------------------------- | :--------------- | :------------------------- | :----------------------- |
| **Crisis**      | "i want to end it all"         | N/A              | **988 Support Info**       | **LOCKED** (Stops PHQ-9) |
| **Overwhelmed** | "it's too much on my plate!!!" | THUNDERSTORM     | **Guided Breathing**       | Open                     |
| **Anxiety**     | "i'm really worried about..."  | FOGGY MIST       | **Step-by-Step Grounding** | Open                     |
| **Gratitude**   | "i'm so grateful for today"    | RADIANT SUN      | Validation/Positive        | Open                     |

---

_Documentation updated on 2026-01-12_
