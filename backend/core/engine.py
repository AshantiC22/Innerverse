"""
FILE: engine.py
PURPOSE: The core emotion analysis engine that translates text into atmosphere states.
FIXED ISSUES:
- Fixed emoji encoding issues
- Corrected function signatures to match app.py
- Improved intent detection logic
- Added better error handling
"""

from textblob import TextBlob
from security import check_for_crisis
from assessments import run_gad7, run_phq9

# Only import utils if running as standalone (not when used by Flask)
try:
    from utils.interface import slow_print, slow_input, display_report
    from utils.storage import load_history, save_entry
    from utils.avatar import get_avatar_response
    STANDALONE_MODE = True
except ImportError:
    STANDALONE_MODE = False


# ============================================================
# EMOTION LEXICON - Pattern matching for specific intents
# ============================================================

INTENT_PATTERNS = {
    "JOY": ["i'm so happy", "feeling great", "love this", "i'm excited", "amazing", "wonderful"],
    "ANGER": ["i'm frustrated", "i'm pissed", "felt disrespected", "i hate", "upset", "i'm upset", "angry", "furious"],
    "SADNESS": ["i'm really sad", "i'm hurting", "this is hard for me", "i feel lonely", "depressed", "crying"],
    "ANXIETY": ["i'm anxious", "i'm really anxious", "i'm worried", "my anxiety", "freaks me out", "nervous", "scared"],
    "OVERWHELMED": ["i'm totally overwhelmed", "too much on my plate", "can't handle all of this", "can't cope", "drowning"],
    "CONFUSION": ["i'm confused", "i don't get it", "need some clarity", "don't understand"],
    "GRATITUDE": ["i really appreciate", "thanks for", "i'm grateful", "thankful", "blessed"],
    "EXCITEMENT": ["i'm so pumped", "can't wait", "so excited", "hyped"]
}


def detect_intent(user_text):
    """
    Checks if the user's text matches specific emotion patterns.
    Returns the emotion name or None if no match is found.
    """
    if not user_text:
        return None
    
    clean_text = user_text.lower().strip()
    
    for emotion, patterns in INTENT_PATTERNS.items():
        if any(pattern in clean_text for pattern in patterns):
            return emotion
    
    return None


def get_intensity_multiplier(user_text):
    """
    Determines the 'volume' of the emotion based on intensity modifiers.
    Returns a multiplier (0.5 = low, 1.0 = normal, 1.5-2.0 = high)
    """
    if not user_text:
        return 1.0
    
    text = user_text.lower()
    
    # High Intensity
    if any(word in text for word in ["extremely", "totally", "pissed off", "can't handle", "unbearable"]):
        return 2.0
    
    # Medium Intensity
    if any(word in text for word in ["really", "very", "so", "quite"]):
        return 1.5
    
    # Low Intensity
    if any(word in text for word in ["kinda", "sort of", "a little", "somewhat"]):
        return 0.5
    
    return 1.0


def check_for_assessment_trigger():
    """
    Checks if the user has had 3 days of 'Heavy' weather in the saved history.
    Only available in standalone mode.
    """
    if not STANDALONE_MODE:
        return False
    
    try:
        history = load_history()
        
        if not history or len(history) < 3:
            return False
        
        # Check the last 3 entries
        last_three = history[-3:]
        heavy_weather_count = sum(
            1 for entry in last_three 
            if entry.get("weather") in ["STEADY RAIN", "THUNDERSTORM"]
        )
        
        return heavy_weather_count >= 3
    except Exception:
        return False


def analyze_journal_entry(user_text):
    """
    Analyzes the sentiment of the text using TextBlob.
    Returns a polarity score from -1.0 (very negative) to 1.0 (very positive).
    """
    if not user_text or not user_text.strip():
        return 0.0
    
    try:
        blob = TextBlob(user_text)
        sentiment = blob.sentiment.polarity
        
        # INTENSITY BOOSTERS: Check for ALL CAPS or excessive punctuation
        if user_text.isupper() or "!!!" in user_text:
            sentiment = sentiment * 1.5
        
        # Clamp to valid range
        sentiment = max(-1.0, min(1.0, sentiment))
        
        return sentiment
    except Exception:
        return 0.0


def translate_score_to_weather(sentiment_score, user_text):
    """
    Translates the sentiment score and detected intent into a weather state.
    
    Args:
        sentiment_score: Float from -1.0 to 1.0
        user_text: The original text (for intent detection)
    
    Returns:
        String representing the weather state
    """
    intent = detect_intent(user_text)
    multiplier = get_intensity_multiplier(user_text)
    
    # --- PRIORITY 1: Positive Intents ---
    if intent in ["JOY", "GRATITUDE", "EXCITEMENT"]:
        return "RADIANT SUN"
    
    # --- PRIORITY 2: Specific Negative Intents ---
    if intent == "ANXIETY":
        return "FOGGY MIST"
    
    # --- PRIORITY 3: Anger or Overwhelmed (High Intensity) ---
    if intent in ["ANGER", "OVERWHELMED"] and multiplier >= 1.5:
        return "THUNDERSTORM"
    
    # --- PRIORITY 4: Standard Sadness ---
    if intent == "SADNESS":
        return "STEADY RAIN"
    
    # --- FALLBACK: Use sentiment score ---
    adjusted_score = sentiment_score * multiplier
    
    if adjusted_score > 0.5:
        return "RADIANT SUN"
    elif adjusted_score > 0.1:
        return "CLEAR SKIES"
    elif adjusted_score > -0.1:
        return "FOGGY MIST"
    elif adjusted_score > -0.5:
        return "STEADY RAIN"
    else:
        return "THUNDERSTORM"


def update_world_visual(weather, score):
    """
    Creates a visual text-based 'scene' for the user based on their mood.
    Used in standalone terminal mode.
    """
    report = f"\n--- YOUR INNERVERSE REPORT (Score: {score:.2f}) ---\n"
    
    # Weather-based scenes (using safe ASCII/emoji)
    scenes = {
        "RADIANT SUN": "☀️ ✨ 🌈\nTHE SKY IS GLOWING! Your energy is radiant and the world is wide open.",
        "CLEAR SKIES": "☀️ 🌤️\nIt's a calm, bright day. Everything feels steady and manageable.",
        "PARTLY CLOUDY": "⛅\nThere's a mix of light and shadow. You're finding your balance.",
        "FOGGY MIST": "🌫️ 💭\nVisibility is low. It's okay not to have all the answers right now.",
        "STEADY RAIN": "🌧️ 💧\nThe clouds are releasing weight. Take this time to rest and reflect.",
        "THUNDERSTORM": "⛈️ ⚡\nThe atmosphere is heavy. Be kind to yourself while the storm passes."
    }
    
    scene = scenes.get(weather, "🌈\nA unique atmosphere is forming...")
    
    return report + scene + "\n" + "═" * 45


def analyze_structure(user_text):
    """
    Analyzes the 'shape' of the writing to find stress patterns.
    Returns tuple: (is_run_on, is_frantic)
    """
    if not user_text:
        return False, False
    
    word_count = len(user_text.split())
    
    # Check for run-on sentences (long text without punctuation)
    is_run_on = word_count > 40 and "," not in user_text and "." not in user_text
    
    # Check for frantic punctuation
    is_frantic = "!!!" in user_text or "???" in user_text
    
    return is_run_on, is_frantic


# ============================================================
# STANDALONE MODE - Command Line Interface
# ============================================================

if __name__ == "__main__":
    if not STANDALONE_MODE:
        print("ERROR: utils module not found. Cannot run in standalone mode.")
        print("This file is meant to be imported by app.py for web use.")
        exit(1)
    
    slow_print("=" * 50)
    slow_print("    🏠 WELCOME TO INNERVERSE 🏠")
    slow_print("=" * 50)
    
    # 1. Get Input
    user_input = slow_input("\nWhat thoughts are moving through your mind right now?\n>")
    
    # 2. SAFETY INTERCEPTION
    is_crisis = check_for_crisis(user_input)
    
    if is_crisis:
        print("\n" + "!" * 50)
        print("🚨 SAFETY ALERT")
        print("!" * 50)
        print("Your words indicate you might be in distress.")
        print("Please reach out for immediate support:")
        print("\n📞 CRISIS RESOURCES (24/7 Free & Confidential):")
        print("• Call or Text: 988 (Suicide & Crisis Lifeline)")
        print("• Website: https://988lifeline.org")
        print("• Chat: https://988lifeline.org/chat/")
        print("!" * 50)
    else:
        # 3. Proceed to analysis
        mood_score = analyze_journal_entry(user_input)
        weather = translate_score_to_weather(mood_score, user_input)
        
        # 4. Show result
        description = update_world_visual(weather, mood_score)
        display_report(weather, mood_score, description)
        
        # 5. Avatar response
        current_intent = detect_intent(user_input)
        avatar_voice = get_avatar_response(weather, current_intent)
        print(f"\n✨ {avatar_voice}\n")
        
        # 6. SKILLS TRIGGER
        if current_intent == "OVERWHELMED":
            import time
            print("\n[Avatar: Let's take a moment together...]")
            time.sleep(1)
            print("Inhale... (4s)")
            time.sleep(4)
            print("Hold... (4s)")
            time.sleep(4)
            print("Exhale... (4s)")
            time.sleep(4)
            print("[Avatar: You're doing great. One step at a time.]\n")
        
        elif current_intent == "ANXIETY" or weather == "FOGGY MIST":
            from utils.avatar import run_grounding_exercise
            run_grounding_exercise()
        
        # 7. MEMORY LINK
        save_entry(weather, mood_score)
        
        # 8. CLINICAL TRIGGER
        if check_for_assessment_trigger():
            print("\n" + "!" * 50)
            print("NOTICE: The atmosphere has been heavy for a few days.")
            print("Would you like to take a quick GAD-7 or PHQ-9 check-in?")
            choice = input("Type 'YES' to start or 'NO' to continue: ").upper()
            
            if choice == 'YES':
                print("\nWhich assessment would you like?")
                print("1. GAD-7 (Anxiety)")
                print("2. PHQ-9 (Depression)")
                assess_choice = input("Enter 1 or 2: ").strip()
                
                if assess_choice == "1":
                    run_gad7()
                elif assess_choice == "2":
                    run_phq9()
                else:
                    print("Invalid choice. Continuing...")