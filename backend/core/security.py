'''
STEP 1: THE LIST (The Database of Concern)
In this section, we define a collection of "Red Flag" words or phrases. 
This is the most sensitive part of the app. 
Think: What specific words indicate that the user needs a human lifeline 
rather than a digital weather change?
'''

# RED_FLAGS = ["word1", "word2", "phrase 1"]
#our acutal Red flags demo words: RED_FLAGS = ["Hate","Angry","Hurt"]
#with the words, we will add a strip().uppercase()


'''
STEP 2: THE SCANNER (The Search Engine)
We need a function (a "box") that takes the user's journal entry 
and compares it against our RED_FLAGS list.
Logic: 
1. Take the text.
2. Make it lowercase (so 'Hurt' and 'hurt' both get caught).
3. Loop through every word in our list.
4. If a match is found, raise a 'Safety Flag'.
'''


'''
STEP 3: THE OVERRIDE (The Traffic Controller)
This logic decides what happens when a flag is found.
Logic:
- If Safety Flag is True: Stop the Weather Engine. Send the 'Help Bridge' message.
- If Safety Flag is False: Proceed to the Sentiment Analysis in engine.py.
'''


'''
STEP 4: THE HELP BRIDGE (The Lifeline)
This is the actual message or resource links the user sees.
It needs to be empathetic, non-judgmental, and provide immediate 
real-world contact info (like a hotline or a saved emergency contact).
'''


# STEP 1: THE CONTAINER (The Watch List / Database)


# We name this in ALL_CAPS because it is a 'Global Constant'—a list that 
# stays the same throughout the entire program's life.
# Each item is a "String" (text) separated by a comma.
RED_FLAGS = [
    "hurt myself", 
    "end it all", 
    "suicide", 
    "emergency", 
    "kill me"
]


# STEP 2 & 3: THE MACHINE (The Scanner / Search Engine)
# i use a prompt text in google to understand the text Sentiment and Complexity Analysis so it can help me understand the how to measure sentence complexity and length in Python, which is exactly the "Structural Analysis" we are building here.

def check_for_crisis(user_text):
    """
    Smarter scanner that looks at keywords AND writing structure.
    """
    score = 0
    clean_text = user_text.strip().lower()
    words = clean_text.split() # Splits the text into a list of words
    word_count = len(words)

    # --- PART A: KEYWORD CHECK (The "What") ---
    # Keywords are still the strongest indicators.
    for flag in RED_FLAGS:
        if flag in clean_text:
            score += 5  # High score for direct red-flag words

    # --- PART B: STRUCTURE CHECK (The "How") ---
    
    # 1. Check for "Spiraling" / Run-on sentences
    # Logic: If it's over 30 words and has no periods or commas.
    if word_count > 30 and "." not in clean_text and "," not in clean_text:
        score += 3
        print("DEBUG: Run-on sentence detected (+3)")

    # 2. Check for "Franticness" (Punctuation Density)
    # Logic: Multiple exclamation points often signal high distress.
    if "!!!" in user_text or "???" in user_text:
        score += 2
        print("DEBUG: Frantic punctuation detected (+2)")

    # 3. Check for "Fragmented/Short" (Despair Pattern)
    # Logic: Very short, repetitive, heavy sentences.
    if word_count < 4 and any(w in ["no", "never", "done", "stop"] for w in words):
        score += 3
        print("DEBUG: Heavy fragment detected (+3)")

    # --- PART C: THE FINAL VERDICT ---
    # We trigger the alert if the total score is 5 or higher.
    if score >= 5:
        return True
    
    return False


# STEP 4: THE TESTER (The Main Gate / The Lifeline)


# This line checks if you are running 'security.py' directly (like 
# 'python security.py') or if another file is just borrowing its tools.
if __name__ == "__main__":
    
    # We use 'input' to create a live prompt in the terminal.
    # This 'captures' the user's typing into the 'test_entry' variable.
    test_entry = input("How are you feeling? (Safety Test): ")
    
    # We pass 'test_entry' into our function and store the result (True/False).
    is_danger = check_for_crisis(test_entry)
    
    # CONDITIONALS: If 'is_danger' is True, run the first block.
    if is_danger:
        print("\n" + "═"*50)
        print(" 🕯️  INNERVERSE: A MOMENT OF SUPPORT  🕯️")
        print("═"*50)
        print("It sounds like your thoughts are moving very fast,")
        print("or you are carrying some heavy feelings right now.")
        print("\nBefore we continue with the weather, please know")
        print("that you don't have to navigate this alone.")
        print("\nHELP RESOURCES:")
        print("• National Crisis Lifeline: Dial 988")
        print("• Text HOME to 741741 to connect with a Crisis Counselor")
        print("• Website: https://988lifeline.org")
        print("═"*50)
    
    # If 'is_danger' is False, run the 'else' block instead.
    else:
        print("\n✅ Atmosphere Clear. Moving to Weather Engine...")