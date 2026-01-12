import time

def run_breathing_exercise():
    """A simple guided breathing timer."""
    print("\n[bold cyan]Avatar: Let's take a moment together...[/bold cyan]")
    time.sleep(1)
    
    steps = [
        ("Inhale... (4s)", 4),
        ("Hold... (4s)", 4),
        ("Exhale... (4s)", 4),
        ("Rest... (4s)", 4)
    ]
    
    for text, duration in steps:
        print(text)
        time.sleep(duration)
        
    print("[bold green]Avatar: You're doing great. One step at a time.[/bold green]")

def get_avatar_response(weather, intent):
    """
    Acts as the 'Voice' of the Innerverse, providing comfort based on the detected state.
    """
    responses = {
        "ANGER": "Avatar: I hear the fire in your words. Let's take a 5-second pause together. You're allowed to be frustrated.",
        "OVERWHELMED": "Avatar: The world feels heavy right now. Focus only on this screen, and take one deep breath. We'll take it one step at a time.",
        "SADNESS": "Avatar: I'm standing here in the rain with you. It's okay to not be okay right now.",
        "ANXIETY": "Avatar: The fog is thick, but you don't need to see the whole path. Just the next few inches.",
        "GRATITUDE": "Avatar: Your light is making the Innerverse bloom! I'm glad you're sharing this moment with me.",
        "CONFUSION": "Avatar: It's okay to feel 'in-between'. Clarity comes in its own time."
    }

    # If we found a specific intent, use that. Otherwise, use a weather-based fallback.
    if intent in responses:
        return responses[intent]
    
    # Fallback logic
    if weather == "THUNDERSTORM":
        return "Avatar: The storm is loud, but you are steady. I'm here until it passes."
    elif weather == "RADIANT SUN":
        return "Avatar: It's a beautiful day in here. Let's hold onto this feeling."
    
    return "Avatar: I'm here, and I'm listening."