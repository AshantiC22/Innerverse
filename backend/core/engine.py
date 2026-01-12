#for step 1: the interpreter, we will install the library(from textblob import Textblob)
#the link on using textblob and understanding how im going to use its polarity score. website link: https://textblob.readthedocs.io/en/dev/quickstart.html#quickstart
from textblob import TextBlob
from security import check_for_crisis  # Go to the file named security.py, find the machine named check_for_crisis, and bring it here so I can use it in this file.
from assessments import run_gad7, run_phq9  # Go to the file named assessments.py, find the machines named run_gad7 and run_phq9, and bring them here so I can use them in this file.
from utils.interface import slow_print, slow_input, display_report
from utils.storage import load_history, save_entry
from utils.avatar import get_avatar_response

'''
we are going to build a bridge between 'Text' and Action. In this file, I will need to think through these three steps:
1. The Analysis: How do I take a sentence like "I'm feeling really lonely today" and turn it into a number?
2. The translation: if that number is low(negative), what does that mean for my "innerverse" app or how will that significant low number effect the app
3. The Delivery: How do I show the user that their world has changed based on the translation affect with the number choice.
'''
'''
As we start begin to code, I need to put my thoughts down for what's gonna happen in this file.
1. we are gonna be using functions for almost throughout this whole project. The function 'def' is a unique tool for analyzing the text and another for deciding the world state
2. Conditionals statements shows how we are going to create the "rules" of the world. Example: If score is Y, then weather is Y
3. The Main Gate (if __name__ == "__main__":): This is a professional standard in Python. It tells the computer: "Only run this code if I am running this specific file directly
'''

'''
This is the State-Logic Table: this tells how an emotion in the "Real World" changes the "Virtual World". In other words we are State Mapping.
1. User Mood(The Trigger): High joy(0.8 to 1.0)| World State(The Result): Brightest Sunlight | Avatar Behavior: Avatar dances or hums | Environmental Detail: Flowers bloom instantly
2. User Mood(The Trigger): Calm(0.2 to 0.7)| World State(The Result): Soft Golden Hour | Avatar Behavior: Avatar sits and reads | Environmental Detail: Wind chimes tinkle
3. User Mood(The Trigger): Neutral(-0.1 to 0.1)| World State(The Result): Overcast/Grey/Sky | Avatar Behavior: Avatar stands still | Environmental Detail: Fog settles on the ground
4. User Mood(The Trigger): Sadness(-0.2 to -0.6)| World State(The Result): Gentle Rain | Avatar Behavior: Avatar carries an umbrella | Environmental Detail: Puddles form on paths
5. User Mood(The Trigger): Distress(-0.7 to -1.0)| World State(The Result): Thunderstorm | Avatar Behavior: Avatar seeks shelter | Environmental Detail: Trees sway violently

'''

'''
Step 1: The Interpreter

we need to turn "I'm feeling lonely" into a number, and we need an external library.
-The concept: now we can use a pre built in library that we can use it to read millions of sentences
-the tool that we will use will be "textblob" its a library
-we can the library tool to get the polarity score. Polarity is the "Number" that is what we wrote down called the State-logic table that ranges from -1.0 to 1.0
'''

'''
Step 2: The Translator

we will use conditionals(if/else) to build our state-logic table
-the concept: we need to divide the -1.0 to 1.0 range into "buckets" and to do that we will use modulo operator
-the logic task: Decides where the "rain" starts
- is -0.1 cloudy?
- is -0.5 a thunderstorm?
-in order to make our state of logic come true we will use "if"."elif"(else if) and else

'''

'''
Step 3: The Reporter

we will show the user the world has changed, and for that we will need to use string formatting.
-the concept: we want the computer to say "Because your score was [Number], the innerverse is now [Weather]
-the tool that i will be using will be "f-strings". they allow you to put variable(like your mood number directly inside a sentence)
'''

'''
Now lets build the skeleton
- we will create three "empty boxes or functions"
-first we gotta install the textblob library: how I do it is "pip install -U textblob and then python -m textblob.download_corpora
'''

# The "Emotion Lexicon" derived from your guide
INTENT_PATTERNS = {
    "JOY": ["i'm so happy", "feeling great", "love this", "i'm excited"],
    "ANGER": ["i'm frustrated because", "i'm pissed off", "felt disrespected", "i hate", "upset", "i'm upset"],
    "SADNESS": ["i'm really sad about", "i'm hurting right now", "this is hard for me", "i feel lonely"],
    "ANXIETY": ["i'm anxious about", "i'm really anxious", "i'm worried that", "my anxiety's really high", "freaks me out"],
    "OVERWHELMED": ["i'm totally overwhelmed", "too much on my plate", "can't handle all of this"],
    "CONFUSION": ["i'm confused about", "i don't get it", "need some clarity"],
    "GRATITUDE": ["i really appreciate", "thanks for", "i'm grateful"],
    "EXCITEMENT": ["i'm so pumped", "can't wait for"]
}

def detect_intent(user_text):
    """Checks if the user used a specific 'Sentence Starter' from the guide."""
    clean_text = user_text.lower().strip()
    for emotion, patterns in INTENT_PATTERNS.items():
        if any(p in clean_text for p in patterns):
            return emotion
    return None

def get_intensity_multiplier(user_text):
    """Determines the 'volume' of the emotion based on intensity modifiers."""
    text = user_text.lower()
    # High Intensity
    if any(word in text for word in ["extremely", "totally", "pissed off", "can't handle"]):
        return 2.0  
    # Medium Intensity
    if any(word in text for word in ["really", "very", "so"]):
        return 1.5  
    # Low Intensity
    if any(word in text for word in ["kinda", "sort of", "a little"]):
        return 0.5  
    return 1.0

def check_for_assessment_trigger():
    """
    Checks if the user has had 3 days of 'Heavy' weather in the saved history.
    """
    history = load_history()  # Pull from your JSON storage
    
    if not history or len(history) < 3:
        return False
    
    # Check the last 3 entries in the list of dictionaries
    # (Since save_entry saves a dictionary like {"weather": "RAIN", "score": -0.5})
    last_three = history[-3:]
    heavy_weather_count = sum(1 for entry in last_three if entry.get("weather") in ["STEADY RAIN", "THUNDERSTORM"])
    
    return heavy_weather_count >= 3
    

def analyze_journal_entry(user_text):
    # We use TextBlob to get the raw polarity (-1 to 1)
    blob = TextBlob(user_text)
    sentiment = blob.sentiment.polarity
    
    # ADVANCED LOGIC: Check for 'Intensity Boosters'
    # If the user uses ALL CAPS or '!!!', we amplify the score
    if user_text.isupper() or "!!!" in user_text:
        sentiment = sentiment * 1.5  # Boost the intensity
        
    return sentiment

def translate_score_to_weather(sentiment_score, user_text):
    intent = detect_intent(user_text)
    multiplier = get_intensity_multiplier(user_text)
    
    # --- PRIORITY 1: Positive Intents ---
    if intent in ["JOY", "GRATITUDE", "EXCITEMENT"]:
        return "RADIANT SUN"
    
    # --- PRIORITY 2: Specific Negative Intents ---
    if intent == "ANXIETY":
        return "FOGGY MIST"
    
    # --- PRIORITY 3: Anger or Overwhelmed ---
    if intent in ["ANGER", "OVERWHELMED"] and multiplier >= 1.5:
        return "THUNDERSTORM"
    
    # --- PRIORITY 4: Standard Sadness/Rain ---
    if intent == "SADNESS":
        return "STEADY RAIN"
    
    # Fallback to math
    adjusted_score = sentiment_score * multiplier
    if adjusted_score > 0.5: 
        return "RADIANT SUN"
    elif adjusted_score < -0.5: 
        return "THUNDERSTORM"
    elif -0.1 < adjusted_score < 0.1: 
        return "FOGGY MIST"
    else: 
        return "STEADY RAIN"
    
def update_world_visual(weather, score):
    """
    Creates a visual text-based 'scene' for the user based on their mood.
    """
    # Header for the report
    report = f"\n--- YOUR INNERVERSE REPORT (Score: {score:.2f}) ---\n"
    
    if weather == "RADIANT SUN":
        scene = "☀️ ✨ 🌈\nTHE SKY IS GLOWING! Your energy is radiant and the world is wide open."
    elif weather == "CLEAR SKIES":
        scene = "☀️ 🌤️\nIt's a calm, bright day. Everything feels steady and manageable."
    elif weather == "PARTLY CLOUDY":
        scene = "⛅\nThere's a mix of light and shadow. You're finding your balance."
    elif weather == "FOGGY MIST":
        scene = "🌫️ 💭\nVisibility is low. It's okay not to have all the answers right now."
    elif weather == "STEADY RAIN":
        scene = "🌧️ 💧\nThe clouds are releasing weight. Take this time to rest and reflect."
    elif weather == "THUNDERSTORM":
        scene = "⛈️ ⚡\nThe atmosphere is heavy. Be kind to yourself while the storm passes."
    else:
        scene = "🌈\nA unique atmosphere is forming..."

    return report + scene + "\n" + "═" * 45

def analyze_structure(user_text):
    """
    Analyzes the 'shape' of the writing to find stress patterns.
    """
    # 1. Count the words (Check for run-on sentences or frantic typing)
    word_count = len(user_text.split())
    
    # 2. Check for "Spiraling" (Very long sentences without pauses)
    # If a sentence has more than 40 words without a comma or period.
    is_run_on = word_count > 40 and "," not in user_text and "." not in user_text

    # 3. Check for "Frantic Punctuation" 
    # (Multiple exclamation points like "!!!" or "???")
    is_frantic = "!!!" in user_text or "???" in user_text

    return is_run_on, is_frantic

# --- The Main Gate ---
if __name__ == "__main__":
    slow_print("--- Welcome to Innerverse ---")
    
    # 1. Get Input
    user_input = slow_input("What thoughts are moving through your mind right now? ")
    
    # 2. THE SAFETY INTERCEPTION
    is_crisis = check_for_crisis(user_input)

    if is_crisis:
        # If the security file says "True", we stop everything else.
        print("\n🚨 SAFETY ALERT: Please reach out for support. Dial 988.")
    else:
        # 3. Proceed to analysis (This only runs if NO crisis)
        mood_score = analyze_journal_entry(user_input)
        weather = translate_score_to_weather(mood_score, user_input)
        
        # 4. Show result
        description = update_world_visual(weather, mood_score) 
        display_report(weather, mood_score, description)

        current_intent = detect_intent(user_input)
        avatar_voice = get_avatar_response(weather, current_intent)
        print(f"\n✨ {avatar_voice}\n")

        # --- THE SKILLS TRIGGER ---
        # 1. Overwhelmed gets Breathing
        if current_intent == "OVERWHELMED":
            import time
            print("\n[bold cyan]Avatar: Let's take a moment together...[/bold cyan]")
            time.sleep(1)
            print("Inhale... (4s)"); time.sleep(4)
            print("Hold... (4s)"); time.sleep(4)
            print("Exhale... (4s)"); time.sleep(4)
            print("[bold green]Avatar: You're doing great. One step at a time.[/bold green]")

        # 2. Anxiety or Foggy Mist gets Grounding
        elif current_intent == "ANXIETY" or weather == "FOGGY MIST":
            from utils.avatar import run_grounding_exercise
            run_grounding_exercise()

        # --- THE MEMORY LINK ---
        save_entry(weather, mood_score)

        # 5. CLINICAL TRIGGER (Now correctly inside the 'else' block)
        # This will NO LONGER trigger if is_crisis is True
        if check_for_assessment_trigger():
            print("\n" + "!"*30)
            print("NOTICE: The atmosphere has been heavy for a few days.")
            print("Would you like to take a quick GAD-7 or PHQ-9 check-in?")
            choice = input("Type 'YES' to start or 'NO' to continue: ").upper()
            
            if choice == 'YES':
                run_phq9()