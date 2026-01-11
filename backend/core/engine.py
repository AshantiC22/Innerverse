#for step 1: the interpreter, we will install the library(from textblob import Textblob)
#the link on using textblob and understanding how im going to use its polarity score. website link: https://textblob.readthedocs.io/en/dev/quickstart.html#quickstart
from textblob import TextBlob
from security import check_for_crisis#Go to the file named security.py, find the machine named check_for_crisis, and bring it here so I can use it in this file.
'''
we are going to buld a bridge between 'Text' and Action. In this file, I will need o think through these three steps:
1. The Analysis:How do I take a sentence like "Im feeling really lonely today" and turn it into a number?
2. The translation: if that number is low(negative), what does that mean for my "innerverse" app or how will that significant low number effect the app
3. The Delivery: How do I show the user that their world has changed base on the the translation affect with the number choice.
'''
'''
As we start begain to code, I need to but my thougths down for whats gonna happen in this file.
1.we are gonna be using a functions for almost throughtout this whole project. The function 'def' is a unique tool for analyzing the text and another for deciding the world state
2.Coonditionals statements shows how we are going to create the "rules" of the world. Example: If score is Y, then weather is Y
3.The Main Gate (if __name__ == "__main__":): This is a professional standard in Python. It tells the computer: "Only run this code if I am running this specific file directly
'''

'''
This is the State-Logic Table: this tells how an emotion in the "Real World" changes the "Virtual World". In other workds we are State Mapping.
1. User Mood(The Trigger): High joy(0.8 to 1.0)| World State(The Result): Brightest Sunlight | Avatar Behavior: Avatar dances or hums | Environmental Detail: Flowers bloom instantly
2. User Mood(The Trigger): Calm(0.2 to 0.7)| World State(The Result): Soft Golden Hour | Avatar Behavior: Avatar sites and reads | Environmental Detail: Wind chimes tinkle
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
-the concept: we need ot divide the -1.0 to 1.0 range into "buckets" and to do that we will use modulo operator
-the logic task: Decides where the "rain" starts
- is -0.1 cloudy?
- is -0.5 a thunderstorm?
-in order to make our state of logic come true we will use "if"."elif"(else if) and else

'''

'''
Step 3: The Reportor

we will show the user the world has changed, and for that we will need to use string formatting.
-the concept: we want the computer to say "Because your score was [Number],the innerverse is now[Weather]
-the tool that i will be using will be "f-strings". they allow you to put variable(like your mood number directly inside a sentence)
'''

'''
Now lets build the skeleton
- we will create three "empty boxes or functions"
-first we gotta install the textblob library: how I do it is "pip install -U textblob and then python -m textblob.download_corpora
'''

def analyze_journal_entry(user_text):
    """
    Step 1: The Interpreter
    Takes the text, checks if it's empty, and returns the polarity score.
    """
    if user_text.strip() == "":
        return None  # Return 'None' to signal an empty input
    
    # Create the 'Blob' from the user's text
    blob = TextBlob(user_text)
    
    # Extract the polarity (the number between -1.0 and 1.0)
    score = blob.sentiment.polarity
    return score

def translate_score_to_weather(score):
    """
    Step 2: The Translator
    Uses your State-Logic Table to turn a number into a weather string.
    """
    if score is None:
        return "Void"

    # --- YOUR TASK: Use your If/Elif logic here ---
    # Example:
    if score >= 0.8:
        return "Brightest Sunlight"
    elif score >= 0.2:
        return "Soft Golden Hour"
    # ADD YOUR OTHER BUCKETS HERE (Neutral, Sadness, Distress)
    else:
        return "Unknown Weather"

def update_world_visual(weather_type, score):
    """
    Step 3: The Reporter
    Uses f-strings to tell the user what happened.
    """
    # This is where we use the f-string tool you identified
    message = f"Because your score was {score:.2f}, the Innerverse is now {weather_type}."
    return message

# --- The Main Gate ---
if __name__ == "__main__":
    print("--- Welcome to Innerverse ---")
    
    # 1. Get Input
    user_input = input("What thoughts are moving through your mind right now? ")
    # 2. THE SAFETY INTERCEPTION (New!)
    # We call the function we imported from security.py
    is_crisis = check_for_crisis(user_input)

    if is_crisis:
        # If the security file says "True", we stop everything else.
        print("\n🚨 SAFETY ALERT: Please reach out for support. Dial 988.")
    else:
        # 3. If safe, we proceed to the mood analysis
        mood_score = analyze_journal_entry(user_input)
        weather = translate_score_to_weather(mood_score)
        
        # 4. Show the result
        final_report = update_world_visual(weather, mood_score)
        print("\n" + final_report)
    
    # 2. Run Step 1 (The Analysis)
    mood_score = analyze_journal_entry(user_input)
    
    # 3. Run Step 2 (The Translation)
    # We pass the result from Step 1 into Step 2
    weather = translate_score_to_weather(mood_score)
    
    # 4. Run Step 3 (The Delivery)
    final_report = update_world_visual(weather, mood_score)
    
    print("\n" + final_report)