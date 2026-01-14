"""
FILE: avatar.py (utils/avatar.py)
PURPOSE: The "voice" of the Innerverse - provides comfort and coping skills
FIXED ISSUES:
- Fixed emoji encoding
- Improved response variety
- Better exercise formatting
- Added error handling
"""

import time


def run_breathing_exercise():
    """
    A simple guided breathing timer using the 4-4-4-4 box breathing technique.
    Effective for anxiety and overwhelm.
    """
    print("\n" + "=" * 60)
    print("  🫁 GUIDED BREATHING EXERCISE")
    print("=" * 60)
    print("\nAvatar: Let's take a moment together...")
    print("Follow along with this simple breathing pattern.\n")
    time.sleep(2)
    
    steps = [
        ("Breathe IN slowly... (4 seconds)", 4),
        ("HOLD your breath... (4 seconds)", 4),
        ("Breathe OUT slowly... (4 seconds)", 4),
        ("REST and relax... (4 seconds)", 4)
    ]
    
    for step_text, duration in steps:
        print(f"  {step_text}")
        for i in range(duration):
            print("  .", end="", flush=True)
            time.sleep(1)
        print()  # New line after dots
    
    print("\n" + "-" * 60)
    print("Avatar: You're doing great. One step at a time.")
    print("=" * 60 + "\n")


def run_grounding_exercise():
    """
    Guided 5-4-3-2-1 Grounding technique.
    Helps bring someone back to the present moment when anxious or dissociating.
    """
    print("\n" + "=" * 60)
    print("  🧭 GROUNDING EXERCISE (5-4-3-2-1)")
    print("=" * 60)
    print("\nAvatar: The fog feels thick. Let's find our way back")
    print("        to the present moment together...\n")
    time.sleep(2)
    
    # Define the senses and how many items for each
    senses = [
        {"action": "SEE", "count": 5, "emoji": "👀", "prompt": "Name 5 things you can see around you:"},
        {"action": "TOUCH", "count": 4, "emoji": "🖐️", "prompt": "Name 4 things you can physically touch:"},
        {"action": "HEAR", "count": 3, "emoji": "👂", "prompt": "Name 3 things you can hear right now:"},
        {"action": "SMELL", "count": 2, "emoji": "👃", "prompt": "Name 2 things you can smell (or like to smell):"},
        {"action": "TASTE", "count": 1, "emoji": "👅", "prompt": "Name 1 thing you can taste (or recently tasted):"}
    ]
    
    for sense in senses:
        print(f"\n{sense['emoji']}  {sense['prompt']}")
        print("-" * 60)
        
        for i in range(1, sense['count'] + 1):
            # This forces the user to type one item and press Enter
            try:
                response = input(f"  {i}. ")
                if not response.strip():
                    print("     (It's okay, just noticing is enough)")
            except KeyboardInterrupt:
                print("\n\nExercise paused. That's okay - you tried.")
                return
        
        time.sleep(0.5)
    
    print("\n" + "=" * 60)
    print("Avatar: I can see you clearly now. You are right here,")
    print("        in this moment. You're safe.")
    print("=" * 60 + "\n")


def get_avatar_response(weather, intent):
    """
    Acts as the 'Voice' of the Innerverse, providing comfort based on the detected state.
    
    Args:
        weather: String weather state (e.g., "THUNDERSTORM")
        intent: String emotion intent (e.g., "ANGER") or None
    
    Returns:
        str: Avatar's empathetic response
    """
    
    # Intent-specific responses (prioritized)
    intent_responses = {
        "ANGER": [
            "I hear the fire in your words. Let's take a 5-second pause together. You're allowed to be frustrated.",
            "That anger is valid. It's telling you something matters to you. Let's sit with it for a moment."
        ],
        "OVERWHELMED": [
            "The world feels heavy right now. Focus only on this screen, and take one deep breath. We'll take it one step at a time.",
            "I see you're carrying a lot. Let's put some of it down together, just for now."
        ],
        "SADNESS": [
            "I'm standing here in the rain with you. It's okay to not be okay right now.",
            "Your sadness is heard. You don't have to carry it alone."
        ],
        "ANXIETY": [
            "The fog is thick, but you don't need to see the whole path. Just the next few inches.",
            "I can feel the worry in your words. Let's ground ourselves together."
        ],
        "GRATITUDE": [
            "Your light is making the Innerverse bloom! I'm glad you're sharing this moment with me.",
            "What a beautiful thing to notice. Thank you for bringing that warmth here."
        ],
        "CONFUSION": [
            "It's okay to feel 'in-between'. Clarity comes in its own time.",
            "Not knowing is part of the journey. You're exactly where you need to be."
        ],
        "JOY": [
            "Your joy is contagious! The whole house is brighter with you here.",
            "I love seeing you like this. Hold onto this feeling."
        ],
        "EXCITEMENT": [
            "I can feel your energy! Tell me more about what's sparking that excitement.",
            "Your enthusiasm is lighting up the whole space!"
        ]
    }
    
    # Weather-based fallback responses
    weather_responses = {
        "THUNDERSTORM": [
            "The storm is loud, but you are steady. I'm here until it passes.",
            "Thunder doesn't last forever. I'll stay right here with you."
        ],
        "RADIANT SUN": [
            "It's a beautiful day in here. Let's hold onto this feeling.",
            "The light you bring is illuminating everything. Stay in this warmth."
        ],
        "STEADY RAIN": [
            "Rain washes things clean. This too shall pass, and I'm here with you.",
            "Let the rain fall. Sometimes we need to release what we're holding."
        ],
        "FOGGY MIST": [
            "The fog will clear when it's ready. For now, I'm your guide.",
            "It's okay to not see clearly right now. Just stay present."
        ],
        "CLEAR SKIES": [
            "What a peaceful atmosphere. Just breathe it in.",
            "Balance feels good, doesn't it? You've found a calm place."
        ]
    }
    
    # Default response
    default_responses = [
        "I'm here, and I'm listening.",
        "You're not alone in this space. I'm with you.",
        "Whatever you're feeling right now, it's valid. I see you."
    ]
    
    # Select response based on intent first, then weather, then default
    import random
    
    if intent and intent in intent_responses:
        return random.choice(intent_responses[intent])
    elif weather and weather in weather_responses:
        return random.choice(weather_responses[weather])
    else:
        return random.choice(default_responses)


def offer_skill(intent, weather):
    """
    Suggests a coping skill based on the current emotional state.
    
    Args:
        intent: String emotion intent
        weather: String weather state
    
    Returns:
        bool: True if a skill was offered and executed
    """
    print("\n" + "=" * 60)
    print("  💡 COPING SKILL SUGGESTION")
    print("=" * 60)
    
    if intent == "OVERWHELMED":
        print("\nYou mentioned feeling overwhelmed.")
        print("Would you like to try a quick breathing exercise?")
        choice = input("\nType 'YES' to try it, or 'NO' to skip: ").upper()
        
        if choice == 'YES':
            run_breathing_exercise()
            return True
    
    elif intent == "ANXIETY" or weather == "FOGGY MIST":
        print("\nI notice you might be feeling anxious or unclear.")
        print("Would you like to try a grounding exercise?")
        choice = input("\nType 'YES' to try it, or 'NO' to skip: ").upper()
        
        if choice == 'YES':
            run_grounding_exercise()
            return True
    
    elif weather == "THUNDERSTORM":
        print("\nThe atmosphere is quite intense right now.")
        print("Would you like to try box breathing to calm the storm?")
        choice = input("\nType 'YES' to try it, or 'NO' to skip: ").upper()
        
        if choice == 'YES':
            run_breathing_exercise()
            return True
    
    print("That's okay. The option is always here if you need it.")
    print("=" * 60 + "\n")
    return False


# ============================================================
# TESTING INTERFACE
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("    AVATAR MODULE TEST")
    print("=" * 60)
    
    print("\nTesting avatar responses...")
    
    test_cases = [
        ("ANGER", "THUNDERSTORM"),
        ("JOY", "RADIANT SUN"),
        ("ANXIETY", "FOGGY MIST"),
        (None, "STEADY RAIN")
    ]
    
    for intent, weather in test_cases:
        response = get_avatar_response(weather, intent)
        print(f"\nIntent: {intent}, Weather: {weather}")
        print(f"Avatar: {response}")
    
    print("\n" + "=" * 60)
    print("Testing breathing exercise...")
    print("=" * 60)
    
    choice = input("\nWould you like to test the breathing exercise? (yes/no): ").lower()
    if choice == 'yes':
        run_breathing_exercise()
    
    print("\n" + "=" * 60)
    print("Testing grounding exercise...")
    print("=" * 60)
    
    choice = input("\nWould you like to test the grounding exercise? (yes/no): ").lower()
    if choice == 'yes':
        run_grounding_exercise()
    
    print("\nAvatar module test complete!")