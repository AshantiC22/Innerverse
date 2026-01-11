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


def check_for_crisis(user_text):
    """
    PURPOSE: This is the 'Logic Gate'. It decides if the text is safe.
    INPUT: 'user_text' (The raw sentence the user typed).
    OUTPUT: Returns True (Danger) or False (Safe).
    """

    # .strip() removes accidental empty spaces at the start or end.
    # .lower() turns "HURT" into "hurt" so it matches our list.
    # We use lowercase because our RED_FLAGS list is written in lowercase.
    clean_text = user_text.strip().lower()
    
    # THE LOOP: This line tells Python to pick up every 'flag' in our 
    # 'RED_FLAGS' box one by one and run the code below for each.
    for flag in RED_FLAGS:
        
        # 'in' is a Membership Operator. It checks if the flag-string 
        # exists anywhere inside the larger clean_text string.
        if flag in clean_text:
            # If a match is found, we stop the whole function immediately.
            # We 'return' True to tell the app: "Stop! Trigger the safety bridge."
            return True 
            
    # If the 'for' loop finishes and never found a match, we reach this line.
    # We return False to tell the app: "Everything is clear, proceed to weather."
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
        print("\n" + "="*30)
        print("🚨 INNERVERSE SAFETY BRIDGE 🚨")
        print("="*30)
        print("It sounds like you're going through a lot.")
        print("Please reach out for support: Dial 988 (USA) or 111 (UK).")
        print("You don't have to face this alone.")
    
    # If 'is_danger' is False, run the 'else' block instead.
    else:
        print("\nInnerverse Status: Atmosphere is stable. Analyzing mood...")