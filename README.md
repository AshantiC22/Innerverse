🌌 Innerverse: The Living House
Empathetic AI Journaling & Mood-Responsive Spatial Environments
Innerverse is a therapeutic full-stack application that translates human emotion into dynamic, 3D "Atmospheric Weather." By combining Natural Language Processing (NLP) with Three.js spatial computing, it provides users a visceral, visual "bio-feedback" loop for emotional processing and grounding.

🎯 Project Overview
Unlike traditional mood trackers that rely on static charts, Innerverse utilizes Internal Environmentalism. It transforms a virtual "Living House" in real-time based on the user's journal entries. If a user is joyful, the house expands with warm light; if they are anxious, the environment becomes claustrophobic and fog-filled.

What Makes It Special?
Video Game-Style Entrance: Immersive first-person perspective transitions through a virtual porch and cinematic door-opening sequences.

Real-Time Emotion Mapping: Leverages custom-tuned NLP to map unstructured text to environmental states.

Affective Architecture: Uses WebGL to physically alter the geometry of the room (ceiling height, wall thickness) as an emotional mirror.

Clinical Safety Guardrails: A prioritized "Security Firewall" that intercepts crisis language to provide immediate clinical resources.

🧠 Core System Architecture
1. The Emotion Engine (engine.py & README-NLP.md)
The "brain" of Innerverse uses a Triple-Check System to classify emotional states beyond basic polarity:

Intent Detection: Scans for clinical sentence starters to identify specific states like Overwhelmed, Anxiety, or Gratitude.

Intensity Multiplier: Detects "Adverbial Modifiers" (e.g., "totally," "extremely") to amplify the environmental response.

Sentiment Fallback: Uses TextBlob polarity math when no specific intent pattern is recognized.

2. The Living House (index.html & JOURNAL_LOGIC.md)
The frontend is built with Three.js and features dynamic environmental scaling:

Breathing Walls: Uses Sine-wave displacement to simulate biological rhythms, providing a visual anchor for breathing exercises.

Atmospheric Occlusion: High-anxiety states trigger FogExp2, mimicking the "tunnel vision" and loss of perspective associated with clinical anxiety.

Kinetic Visuals: Includes procedural rain particles, mist animation, and a camera "Earthquake" effect (40-50Hz vibration) for high-arousal emotions like anger.

3. Clinical Safety Firewall (security.py)
Safety is prioritized over all AI features through a specialized firewall:

Keyword Interception: Scans for "Red Flags" (suicidal ideation, self-harm) and "Warning Phrases".

Immediate Override: If a crisis is detected, the engine blocks all secondary logic and triggers an immediate display of 988 Lifeline resources.

🛠 Tech Stack & Engineering Fundamentals
Backend: Python 3.x, Flask (REST API).

Frontend: JavaScript (ES6+), Three.js (WebGL), GSAP Animations.

NLP: TextBlob, Custom Intent-Pattern Matching.

Clinical Standards: GAD-7 (Anxiety) and PHQ-9 (Depression) screening modules.

Storage: JSON-based state persistence and historical mood tracking.

🧪 Psychological Research Pillars
Innerverse is built on evidence-based concepts to ensure therapeutic value:

Chromotherapy: Maps specific hex codes (e.g., Gold #FFD700 for dopamine stimulation) to trigger biological mood responses.

Metaphoric Congruence: Validates user feelings by physically manifesting internal states in the environment (e.g., a "Lava Floor" for anger).

Active Grounding: Implements a 5-4-3-2-1 Sensory Loop within the UI to halt the "rumination loop" common in anxiety.

🚀 How to Run
Install Dependencies: pip install flask textblob rich.

Launch the Server: Run python app.py.

Access Innerverse: Navigate to localhost:5000 to enter the house.

Here is how each file can be demoed to prove the app's functionality:

engine.py (The Emotional Brain): You can run this file to see the core translation logic in action. It processes test phrases and demonstrates how it maps specific "intents" like JOY or ANGER to their corresponding weather states.

security.py (The Safety Firewall): This file contains an automated testing suite. Running it directly will process "Crisis Test Cases"—like "I want to end it all"—to prove that the system successfully intercepts dangerous language and triggers immediate clinical resources.

assessments.py (Clinical Tools): Running this allows you to test the standardized GAD-7 and PHQ-9 screenings. It demonstrates the interactive scoring system that tracks clinical-standard anxiety and depression levels.

avatar.py (Intervention Module): This file can be run to demo the "Avatar Skills". It specifically tests the 4-4-4-4 Box Breathing exercise with a timed, guided interface.

app.py (System Orchestrator): Running this launches the Flask server, proving that all the individual modules—security, engine, and assessments—are successfully integrated into a single, functional API.

📈 Future Enhancements
Spatial Audio: Integration of door creaks, rain, and thunder audio for total immersion.

Multi-Room Environments: Expanding to a Kitchen (nurturing), Bedroom (rest), and Study (focus).

Wearable Integration: Connecting real-time heart rate data to drive the "breathing" wall speeds.

Innerverse — Translating the unseen architecture of the mind into a living digital world.
