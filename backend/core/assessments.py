"""
FILE: assessments.py
PURPOSE: This module provides clinical-standard screening tools (GAD-7 and PHQ-9).
WHY WE ADDED THIS: 
While sentiment analysis (engine.py) tracks 'how' a user feels in the moment, 
these assessments track 'symptoms' over time. This helps users differentiate 
between a 'bad day' (weather) and a 'pattern' (clinical anxiety/depression).

WHAT IS GAD-7? 
Generalized Anxiety Disorder 7-item scale. It is a world-standard 
screening tool for measuring the severity of anxiety.

WHAT IS PHQ-9? 
Patient Health Questionnaire 9-item scale. It is used to screen, 
diagnose, and monitor the severity of depression.
"""


# GAD-7: ANXIETY ASSESSMENT

def run_gad7():
    """
    Runs the 7-question anxiety screening.
    Scoring: 0-4 Minimal, 5-9 Mild, 10-14 Moderate, 15+ Severe.
    """
    print("\n" + "═"*50)
    print("      GAD-7: ANXIETY SCREENING TOOL")
    print("  Over the last 2 weeks, how often have you been")
    print("  bothered by the following problems?")
    print("  (0: Not at all | 1: Several days | 2: Half the days | 3: Every day)")
    print("═"*50)

    questions = [
        "1. Feeling nervous, anxious, or on edge",
        "2. Not being able to stop or control worrying",
        "3. Worrying too much about different things",
        "4. Trouble relaxing",
        "5. Being so restless that it is hard to sit still",
        "6. Becoming easily annoyed or irritable",
        "7. Feeling afraid as if something awful might happen"
    ]

    score = _collect_scores(questions)
    
    # Interpretation Logic
    if score <= 4: result = "Minimal Anxiety"
    elif score <= 9: result = "Mild Anxiety"
    elif score <= 14: result = "Moderate Anxiety"
    else: result = "Severe Anxiety"

    print(f"\nYour GAD-7 Score: {score}")
    print(f"Result: {result}")
    return score, result



# PHQ-9: DEPRESSION ASSESSMENT

def run_phq9():
    """
    Runs the 9-question depression screening with integrated safety protocols.
    """
    print("\n" + "═"*50)
    print("      PHQ-9: DEPRESSION SCREENING TOOL")
    print("  Over the last 2 weeks, how often have you been")
    print("  bothered by the following problems?")
    print("  (0: Not at all | 1: Several days | 2: Half the days | 3: Every day)")
    print("═"*50)

    questions = [
        "1. Little interest or pleasure in doing things",
        "2. Feeling down, depressed, or hopeless",
        "3. Trouble falling or staying asleep, or sleeping too much",
        "4. Feeling tired or having little energy",
        "5. Poor appetite or overeating",
        "6. Feeling bad about yourself — or that you are a failure",
        "7. Trouble concentrating on things (e.g. reading)",
        "8. Moving or speaking so slowly... or being fidgety/restless",
        "9. Thoughts that you would be better off dead, or hurting yourself"
    ]

    # --- MODIFIED COLLECTION ---
    # We collect scores into a list so we can check Question 9 (index 8)
    individual_scores = []
    for q in questions:
        while True:
            try:
                val = int(input(f"{q}: "))
                if 0 <= val <= 3:
                    individual_scores.append(val)
                    break
                else:
                    print("⚠️  Please enter 0, 1, 2, or 3.")
            except ValueError:
                print("⚠️  Invalid input. Please enter a number.")

    total_score = sum(individual_scores)
    q9_score = individual_scores[8]  # This is the "Suicidal Ideas" question

    # Interpretation Logic
    if total_score <= 4: result = "Minimal Depression"
    elif total_score <= 9: result = "Mild Depression"
    elif total_score <= 14: result = "Moderate Depression"
    elif total_score <= 19: result = "Moderately Severe Depression"
    else: result = "Severe Depression"

    print(f"\nYour PHQ-9 Score: {total_score}")
    print(f"Result: {result}")

    # --- THE SAFETY OVERRIDE ---
    # Trigger 1: Any thoughts of self-harm (Q9 > 0)
    # Trigger 2: Moderate to Severe Score (Total >= 10)
    if q9_score > 0 or total_score >= 10:
        print("\n" + "!"*60)
        print("💡 IMPORTANT RECOMMENDATION:")
        print("Based on your screening, it is recommended that you follow up")
        print("with a crisis counselor or healthcare provider.")
        
        print("\n📞 REACH OUT FOR SUPPORT (24/7 Free & Confidential):")
        print("• Call or Text: 988")
        print("• 988 Lifeline Website: https://988lifeline.org")
        print("• Chat Online: https://988lifeline.org/chat/")

        if q9_score > 0:
            print("\n🚨 SPECIFIC RESOURCE FOR SUICIDAL IDEATION:")
            print("Since you noted thoughts of self-harm, please visit:")
            print("👉 https://988lifeline.org/help-yourself/suicidal-thoughts/")
        
        if total_score >= 20:
            print("\n🆘 URGENT: Your score is in the 'Severe' range.")
            print("Please consider connecting to the 988 center immediately.")
        
        print("!"*60 + "\n")

    return total_score, result


# INTERNAL HELPER (The Input Machine)

def _collect_scores(questions):
    """
    A helper function to prevent code repetition. 
    It loops through questions and ensures valid 0-3 inputs.
    """
    total = 0
    for q in questions:
        while True:
            try:
                val = int(input(f"{q}: "))
                if 0 <= val <= 3:
                    total += val
                    break
                else:
                    print("⚠️  Please enter a number between 0 and 3.")
            except ValueError:
                print("⚠️  Invalid input. Please enter a number (0, 1, 2, or 3).")
    return total


# TESTER BLOCK

if __name__ == "__main__":
    # This allows you to test the file independently
    print("Innerverse Assessment Module Active.")
    choice = input("Test GAD-7 (A) or PHQ-9 (B)? ").upper()
    if choice == "A":
        run_gad7()
    elif choice == "B":
        run_phq9()