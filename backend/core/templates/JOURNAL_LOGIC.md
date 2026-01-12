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

_Technical Milestone: Phase 2 Web Architecture Complete - 2026-01-12_
