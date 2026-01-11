# 🌌 Innerverse: Backend Engineering & Logic Documentation

Innerverse is a smart journaling ecosystem that bridges the gap between creative writing and clinical mental health awareness. This document tracks the full architectural development of the **Backend** system.

---

## 🛠️ The Architecture (The `backend/` Folder)

We structured the backend into two distinct sections to separate **Logic** from **Experience**.

### 1. `backend/core/` (The Brain)

- **`engine.py`**: The central nervous system. It processes raw text, calculates polarity, and translates numbers into atmospheric weather states.
- **`security.py`**: The "Guardian" module. It intercepts high-risk keywords before they even reach the engine to ensure immediate safety.
- **`assessments.py`**: The clinical vault. It contains standardized medical screening tools (GAD-7 and PHQ-9).

### 2. `backend/utils/` (The Nervous System)

- **`interface.py`**: Handles the human-computer interaction, using the `Rich` library to turn boring code into a beautiful, color-coded terminal experience.

---

## 🧠 Logic Milestones (What We Built)

### **Phase 1: Sentiment & Translation**

We built a "State-Logic Table" to map human emotions to weather.

- **Tool used:** `TextBlob` for Natural Language Processing.
- **Innovation:** Added an **Intensity Booster** that multiplies the sentiment score by $1.5$ if the user uses ALL CAPS or excessive punctuation (`!!!`), acknowledging that "shouting" signals higher emotional energy.

### **Phase 2: The Safety Guardian**

We implemented a mandatory security check that runs _before_ any analysis.

- **Logic:** If a "Crisis Keyword" is detected, the engine halts and provides immediate help.
- **Clinical Integration:** We added the **988 Suicide & Crisis Lifeline** as a hard-coded safety override.

### **Phase 3: Clinical Assessments (GAD-7 & PHQ-9)**

We added evidence-based tools to move beyond "vibe checks" into clinical data.

- **GAD-7:** Screens for Generalized Anxiety Disorder.
- **PHQ-9:** Screens for Depression.
- **Smart Logic:** If a user answers "Yes" to the self-harm question (Q9), or scores above a 10 (Moderate), the app automatically provides a clickable link to 988 resources.

### **Phase 4: Trend Awareness**

We built a logic gate that monitors `mood_history`.

- **Condition:** If the last 3 entries are `STEADY RAIN` or `THUNDERSTORM`, the app realizes the user is in a "rut" and suggests an assessment.

### **Phase 5: The Mindful UI**

We replaced standard `print()` and `input()` with custom-built functions.

- **`slow_input`**: Solved the `NoneType` attribute error by ensuring input is returned while maintaining a typewriter effect.
- **`Rich Panels`**: Created color-coded boxes (Yellow for joy, Red for distress) to provide instant visual validation.

---

## 🔗 Research & Learning Resources

Throughout this build, we utilized the following documentation and tutorials to ensure professional-grade code:

- **Sentiment Analysis:** [TextBlob Quickstart](https://textblob.readthedocs.io/en/dev/quickstart.html) - Understanding polarity and subjectivity.
- **UI Design:** [Rich Library Documentation](https://rich.readthedocs.io/en/latest/introduction.html) - How to style terminals.
- **Clinical Standards:** [PHQ-9 & GAD-7 Scoring Guide](https://www.apa.org/depression-guideline/patient-health-questionnaire.pdf) - Mapping scores to clinical severity.
- **Python Logic:** [Conditional Branching and Functions](https://docs.python.org/3/tutorial/controlflow.html) - Building the "Main Gate" and logic loops.

---

## 📝 Commit History Recap

1.  **Engine Initialized:** Text-to-Weather mapping.
2.  **Safety Guard:** Keyword interception added.
3.  **Clinical Milestone:** GAD-7 and PHQ-9 modules created.
4.  **Integration Milestone:** Linking history trends to clinical triggers.
5.  **UI Milestone:** `Rich` library and `slow_input` integration.
