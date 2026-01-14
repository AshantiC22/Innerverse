"""
FILE: security.py
PURPOSE: Crisis detection system that scans for urgent language requiring intervention.
FIXED ISSUES:
- Expanded keyword list based on clinical standards
- Improved scoring system
- Better documentation
- Fixed emoji encoding
"""


# ============================================================
# RED FLAGS - Critical keywords that indicate crisis
# ============================================================

RED_FLAGS = [
    # Suicidal ideation
    "kill myself",
    "end my life",
    "want to die",
    "suicide",
    "suicidal",
    "end it all",
    "better off dead",
    "no reason to live",
    "wish i was dead",
    
    # Self-harm
    "hurt myself",
    "self harm",
    "cut myself",
    "harm myself",
    
    # Plans/intent
    "have a plan",
    "going to kill",
    "tonight is the night",
    
    # Desperation indicators
    "can't go on",
    "no way out",
    "give up on life"
]

# Secondary warning phrases (lower severity but concerning)
WARNING_PHRASES = [
    "no point",
    "what's the point",
    "tired of living",
    "can't take it anymore",
    "want it to end",
    "everyone better without me"
]


def check_for_crisis(user_text):
    """
    Advanced crisis detection that analyzes keywords AND writing structure.
    
    Returns:
        bool: True if crisis indicators detected, False otherwise
    
    Scoring System:
        - Red flag keyword: +5 points
        - Warning phrase: +2 points
        - Run-on sentence: +3 points
        - Frantic punctuation: +2 points
        - Heavy fragments: +3 points
        - Threshold: 5+ points triggers alert
    """
    if not user_text or not user_text.strip():
        return False
    
    score = 0
    clean_text = user_text.strip().lower()
    words = clean_text.split()
    word_count = len(words)
    
    # ============================================================
    # PART A: KEYWORD ANALYSIS (The "What")
    # ============================================================
    
    # Critical red flags - immediate concern
    for flag in RED_FLAGS:
        if flag in clean_text:
            score += 5
            print(f"[Security] Red flag detected: '{flag}' (+5)")
    
    # Warning phrases - concerning but less severe
    for phrase in WARNING_PHRASES:
        if phrase in clean_text:
            score += 2
            print(f"[Security] Warning phrase detected: '{phrase}' (+2)")
    
    # ============================================================
    # PART B: STRUCTURAL ANALYSIS (The "How")
    # ============================================================
    
    # 1. Run-on sentences (cognitive overwhelm pattern)
    # Long text without punctuation suggests racing thoughts
    if word_count > 40 and "." not in clean_text and "," not in clean_text:
        score += 3
        print("[Security] Run-on sentence detected (+3)")
    
    # 2. Frantic punctuation (high emotional intensity)
    # Multiple exclamation/question marks suggest distress
    if "!!!" in user_text or "???" in user_text:
        score += 2
        print("[Security] Frantic punctuation detected (+2)")
    
    # 3. Heavy fragments (despair pattern)
    # Very short, heavy statements like "no more" or "done"
    despair_words = ["no", "never", "done", "stop", "end", "nothing", "nowhere"]
    if word_count < 5 and any(word in words for word in despair_words):
        score += 3
        print("[Security] Heavy fragment detected (+3)")
    
    # ============================================================
    # PART C: FINAL VERDICT
    # ============================================================
    
    print(f"[Security] Total crisis score: {score}")
    
    # Threshold: 5 or more points triggers safety alert
    if score >= 5:
        return True
    
    return False


def display_crisis_resources():
    """
    Displays crisis resources in a clear, empathetic format.
    Call this function when check_for_crisis() returns True.
    """
    print("\n" + "=" * 60)
    print("    🕯️  INNERVERSE: A MOMENT OF SUPPORT  🕯️")
    print("=" * 60)
    print("\nIt sounds like your thoughts are moving very fast,")
    print("or you are carrying some heavy feelings right now.")
    print("\nBefore we continue, please know that you don't have")
    print("to navigate this alone.")
    print("\n" + "-" * 60)
    print("📞 IMMEDIATE HELP RESOURCES (24/7 Free & Confidential)")
    print("-" * 60)
    print("\n• 🆘 Call or Text: 988")
    print("  (Suicide & Crisis Lifeline)")
    print("\n• 💬 Text 'HELLO' to: 741741")
    print("  (Crisis Text Line)")
    print("\n• 🌐 Website: https://988lifeline.org")
    print("\n• 💻 Live Chat: https://988lifeline.org/chat/")
    print("\n• 🏥 Emergency: 911 (for immediate danger)")
    print("\n" + "=" * 60)
    print("You matter. Your life has value. Help is available.")
    print("=" * 60 + "\n")


# ============================================================
# TESTING INTERFACE
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("    INNERVERSE SECURITY MODULE - CRISIS DETECTION TEST")
    print("=" * 60)
    print("\nThis module screens for urgent language patterns.")
    print("Type a message to test the crisis detection system.\n")
    
    test_entry = input("How are you feeling? (Safety Test)\n> ")
    
    # Run the detection
    is_danger = check_for_crisis(test_entry)
    
    print("\n" + "-" * 60)
    
    if is_danger:
        display_crisis_resources()
    else:
        print("✅ Atmosphere Clear. Moving to Weather Engine...")
        print("-" * 60)
    
    # Show some test cases
    print("\n" + "=" * 60)
    print("EXAMPLE TEST CASES:")
    print("=" * 60)
    
    test_cases = [
        ("I'm feeling okay today", False, "Normal entry"),
        ("I'm so frustrated with work!!!", False, "High emotion but not crisis"),
        ("I want to end my life", True, "Direct suicidal ideation"),
        ("can't go on anymore what's the point", True, "Multiple warning phrases"),
        ("I just feel so tired of everything and everyone would be better without me and there's no point in any of this anymore", True, "Run-on + warning phrases")
    ]
    
    print("\nRunning automated tests...")
    for text, expected, description in test_cases:
        result = check_for_crisis(text)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"\n{status} - {description}")
        print(f"  Input: \"{text}\"")
        print(f"  Expected: {expected}, Got: {result}")
    
    print("\n" + "=" * 60)