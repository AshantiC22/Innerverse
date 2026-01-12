# 🛸 Innerverse: The Avatar's House

**Empathetic AI Journaling & Mood-Responsive Environments**

Innerverse is a web-based wellness application that translates human emotion into dynamic "Atmospheric Weather." By combining NLP-driven sentiment analysis with clinical grounding techniques, it provides users a safe space to reflect, breathe, and ground themselves.

## 🔬 The Research: Making it Reality

Our development is guided by three core pillars of research:

### 1. The Color-Mood Connection (Chromotherapy)

We are researching how UI color shifts impact emotional regulation.

- **Radiant Sun:** Uses warm yellows (#FFD700) to stimulate dopamine during positive reflection.
- **Foggy Mist:** Uses soft greys and low-contrast UI to reduce visual overstimulation during high-anxiety states.
- **Steady Rain:** Uses calming blues to encourage introspection and "releasing weight".

### 2. Digital Clinical Safety

Research into the "Safety Firewall" ensures that high-risk inputs are never ignored in favor of AI features.

- **Crisis Intercept:** Logic that prioritizes 988 resources over all other app functions.
- **Assessment Pacing:** PHQ-9/GAD-7 triggers are designed to appear only after a 3-day "Heavy Weather" threshold to avoid "Assessment Fatigue".

### 3. Interactive Grounding Logic

We’ve moved from passive reading to **active participation**.

- **The 5-4-3-2-1 Nested Loop:** Research suggests that forcing individual sensory inputs (one-by-one) effectively halts the "rumination loop" common in anxiety.

---

## 🛠 Tech Stack

- **Backend:** Python / Flask
- **Sentiment Engine:** TextBlob & Custom NLP Intent Patterns
- **Frontend:** HTML5, CSS3 (Mood-Responsive), JavaScript (Fetch API)
- **Storage:** JSON Persistence

---

## 🚀 How it Works (Phase 2 Flow)

1. **The Input:** User submits thoughts via a web form.
2. **The Analysis:** Flask processes the text through `engine.py`.
3. **The Response:** The server returns a "Weather Package" (CSS color, Emoji, Avatar Skill).
4. **The Transition:** The webpage background changes in real-time to match the user's emotional state.
