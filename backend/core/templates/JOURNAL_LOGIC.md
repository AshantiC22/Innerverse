# 📔 Innerverse: Journal Logic & UX Research

**Documenting the transition from Terminal to Web (Phase 2)**

## 🧪 UX Research: The Typewriter Effect

We implemented a controlled text-delivery system (30ms per character) to mirror human speech patterns.

- **Goal:** Prevent "Information Overload" where a user is hit with a wall of text instantly.
- **Impact:** Encourages slow reading and deliberate reflection.

## 🚦 Logic Flow: Asynchronous Emotional Processing

The web interface uses an **Asynchronous Request Cycle** to handle data:

1. **Safety Intercept:** `check_for_crisis` runs before any sentiment math to ensure immediate safety response.
2. **Intent Priority:** Specific patterns (ANXIETY, EXCITEMENT) override the TextBlob math to ensure accurate weather mapping.
3. **Skill Routing:** The backend identifies if a skill (Breathing/Grounding) is required and sends a `skill_needed` flag to the frontend.

## 🎨 Chromotherapy Mapping

We utilize specific hex codes to trigger biological mood responses:

- **#FFD700 (Gold):** Associated with warmth and optimism (Radiant Sun).
- **#4682B4 (SteelBlue):** Associated with stability and calm (Steady Rain).
- **#D3D3D3 (LightGrey):** Neutrality to reduce anxiety (Foggy Mist).

---

## 📐 Phase 3: Spatial Emotional Environments

- **Library:** Three.js (WebGL)
- **Concept:** "The Living Room" — A 3D space that physically morphs.
- **Visual Research:** - **Volumetric Lighting:** Using God-rays for RADIANT SUN.
  - **Particle Physics:** Real-time generated rain drops for STEADY RAIN.
  - **Shaders:** Post-processing "Blur" and "Grain" for FOGGY MIST to simulate visual occlusion.

# 🏛️ Phase 3.1: Architectural Emotional Regulation

**Researching the impact of 3D objects on User Safety**

## 🛋️ Object Manifestation

- **The Couch:** Represents a "Safe Base." By changing its material color to match the weather (e.g., deep blue during Rain), we provide a visual anchor that suggests the user has a "place to sit" within their emotions.
- **Fog Volumetrics:** Instead of just a grey background, we use `THREE.FogExp2`. This creates a literal sense of depth-loss, which helps externalize the feeling of "mental fog" common in anxiety.

## 📐 Camera Kinematics

The 100ms camera transition simulates the physical act of "walking." This triggers a **proprioceptive shift** in the user, helping them disconnect from the external world and commit to the journaling session.

# 🌋 Phase 3.4: Internal Environmentalism

**The Psychology of Embodied Metaphor**

## 🏗️ Emotional Architectures

We are researching **Metaphoric Congruence**. When a user types "I am upset," seeing the house shake (Earthquake) and the floor turn red (Lava) provides **Internal Validation**.

- **Earthquake Logic:** By vibrating the `camera.position` at 40-50Hz, we mimic the physical sensation of a "shaking heart" or "trembling hands."
- **Lava Floor:** Uses the `emissiveIntensity` property to create a "pulsing heat" sensation, which correlates with the physical warmth of anger.

## 🌫️ Atmospheric Occlusion

In "Confused/Anxious" states, the `THREE.FogExp2` is set to $0.15$. This physically prevents the user from seeing the edges of the room, mirroring the "tunnel vision" and "loss of perspective" found in high-anxiety clinical research.

# ✅ Phase 3.4 Integration Verification

**Testing the connection between Sentiment Analysis and 3D Rendering**

## 🧪 Test Results

1. **Priority Override:** Verified that "Angry" keywords trigger the `THUNDERSTORM` state even if the sentiment score is mathematically neutral.
2. **JSON Handshake:** Confirmed that `app.py` successfully sends a 3-part dictionary (`score`, `intent`, `weather`) to the frontend `fetch` call.
3. **Camera Kinematics:** Confirmed the Earthquake shake is tied to the `shakeIntensity` variable, which only activates when `intent == "ANGER"`.

_Technical Milestone: Phase 2 Web Architecture Complete - 2026-01-12_
