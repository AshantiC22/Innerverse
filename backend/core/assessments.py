"""
FILE: assessments.py
PURPOSE: Clinical-standard screening tools (GAD-7 and PHQ-9).
FIXED ISSUES:
- Fixed emoji encoding
- Improved error handling
- Better formatting
- Added result interpretation
"""


def run_gad7():
    """
    Runs the 7-question anxiety screening (GAD-7).
    
    Scoring:
        0-4:   Minimal Anxiety
        5-9:   Mild Anxiety
        10-14: Moderate Anxiety
        15-21: Severe Anxiety
    
    Returns:
        tuple: (score, result_text)
    """
    print("\n" + "=" * 60)
    print("          GAD-7: ANXIETY SCREENING TOOL")
    print("=" * 60)
    print("\nOver the last 2 weeks, how often have you been")
    print("bothered by the following problems?")
    print("\n  0 = Not at all")
    print("  1 = Several days")
    print("  2 = More than half the days")
    print("  3 = Nearly every day")
    print("\n" + "-" * 60)

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
    if score <= 4:
        result = "Minimal Anxiety"
        interpretation = "Your anxiety levels appear to be in the normal range."
    elif score <= 9:
        result = "Mild Anxiety"
        interpretation = "You may be experiencing mild anxiety. Consider stress management techniques."
    elif score <= 14:
        result = "Moderate Anxiety"
        interpretation = "You're experiencing moderate anxiety. Consider speaking with a healthcare provider."
    else:
        result = "Severe Anxiety"
        interpretation = "You're experiencing severe anxiety. Please consult with a mental health professional."

    print("\n" + "=" * 60)
    print(f"Your GAD-7 Score: {score} out of 21")
    print(f"Result: {result}")
    print(f"\n{interpretation}")
    
    # Recommendation for moderate/severe
    if score >= 10:
        print("\n💡 RECOMMENDATION:")
        print("Given your score, it's recommended to follow up with")
        print("a healthcare provider for a comprehensive evaluation.")
        print("\n📞 Resources:")
        print("• SAMHSA National Helpline: 1-800-662-4357 (24/7)")
        print("• Anxiety & Depression Association: www.adaa.org")
    
    print("=" * 60 + "\n")
    
    return score, result


def run_phq9():
    """
    Runs the 9-question depression screening (PHQ-9).
    Includes integrated safety protocols for Question 9 (suicidal ideation).
    
    Scoring:
        0-4:   Minimal Depression
        5-9:   Mild Depression
        10-14: Moderate Depression
        15-19: Moderately Severe Depression
        20-27: Severe Depression
    
    Returns:
        tuple: (score, result_text)
    """
    print("\n" + "=" * 60)
    print("         PHQ-9: DEPRESSION SCREENING TOOL")
    print("=" * 60)
    print("\nOver the last 2 weeks, how often have you been")
    print("bothered by the following problems?")
    print("\n  0 = Not at all")
    print("  1 = Several days")
    print("  2 = More than half the days")
    print("  3 = Nearly every day")
    print("\n" + "-" * 60)

    questions = [
        "1. Little interest or pleasure in doing things",
        "2. Feeling down, depressed, or hopeless",
        "3. Trouble falling or staying asleep, or sleeping too much",
        "4. Feeling tired or having little energy",
        "5. Poor appetite or overeating",
        "6. Feeling bad about yourself — or that you are a failure",
        "7. Trouble concentrating on things (e.g., reading)",
        "8. Moving or speaking slowly, or being fidgety/restless",
        "9. Thoughts that you would be better off dead, or hurting yourself"
    ]

    # Collect individual scores to check Question 9
    individual_scores = []
    for q in questions:
        while True:
            try:
                val = int(input(f"\n{q}\nYour answer (0-3): "))
                if 0 <= val <= 3:
                    individual_scores.append(val)
                    break
                else:
                    print("⚠️  Please enter a number between 0 and 3.")
            except ValueError:
                print("⚠️  Invalid input. Please enter a number (0, 1, 2, or 3).")
            except KeyboardInterrupt:
                print("\n\nAssessment cancelled.")
                return 0, "Cancelled"

    total_score = sum(individual_scores)
    q9_score = individual_scores[8]  # Question 9: Suicidal ideation

    # Interpretation Logic
    if total_score <= 4:
        result = "Minimal Depression"
        interpretation = "Your depression symptoms appear to be minimal."
    elif total_score <= 9:
        result = "Mild Depression"
        interpretation = "You may be experiencing mild depression. Monitor your symptoms."
    elif total_score <= 14:
        result = "Moderate Depression"
        interpretation = "You're experiencing moderate depression. Consider professional support."
    elif total_score <= 19:
        result = "Moderately Severe Depression"
        interpretation = "You're experiencing moderately severe depression. Professional help is recommended."
    else:
        result = "Severe Depression"
        interpretation = "You're experiencing severe depression. Please seek immediate professional help."

    print("\n" + "=" * 60)
    print(f"Your PHQ-9 Score: {total_score} out of 27")
    print(f"Result: {result}")
    print(f"\n{interpretation}")
    print("=" * 60)

    # ============================================================
    # SAFETY OVERRIDE - Critical intervention points
    # ============================================================
    
    needs_intervention = False
    
    # Trigger 1: ANY thoughts of self-harm (Q9 > 0)
    if q9_score > 0:
        needs_intervention = True
        print("\n" + "!" * 60)
        print("🚨 CRITICAL SAFETY ALERT")
        print("!" * 60)
        print("\nYou indicated having thoughts about being better off dead")
        print("or hurting yourself. This requires immediate attention.")
        
    # Trigger 2: Moderate to Severe Score (Total >= 10)
    elif total_score >= 10:
        needs_intervention = True
        print("\n" + "!" * 60)
        print("💡 IMPORTANT RECOMMENDATION")
        print("!" * 60)
    
    if needs_intervention:
        print("\n📞 IMMEDIATE SUPPORT RESOURCES (24/7 Free & Confidential):")
        print("-" * 60)
        print("\n• 🆘 Call or Text: 988")
        print("  (Suicide & Crisis Lifeline)")
        print("\n• 💬 Text 'HELLO' to: 741741")
        print("  (Crisis Text Line)")
        print("\n• 🌐 Website: https://988lifeline.org")
        print("  Online Chat: https://988lifeline.org/chat/")
        print("\n• 📱 SAMHSA Helpline: 1-800-662-4357")
        print("  (Treatment referral & information)")
        
        if q9_score > 0:
            print("\n" + "-" * 60)
            print("🆘 SPECIFIC RESOURCE FOR SUICIDAL THOUGHTS:")
            print("-" * 60)
            print("\nPlease visit immediately:")
            print("👉 https://988lifeline.org/help-yourself/suicidal-thoughts/")
            print("\nIf you are in immediate danger:")
            print("🏥 Call 911 or go to your nearest emergency room")
        
        if total_score >= 20:
            print("\n" + "-" * 60)
            print("🆘 URGENT: SEVERE DEPRESSION DETECTED")
            print("-" * 60)
            print("\nYour score indicates severe depression.")
            print("Please connect to the 988 center immediately")
            print("or visit an emergency room.")
        
        print("\n" + "!" * 60)
        print("You don't have to face this alone. Help is available.")
        print("!" * 60 + "\n")

    return total_score, result


def _collect_scores(questions):
    """
    Helper function to collect scores for multiple questions.
    Ensures valid 0-3 inputs and handles errors gracefully.
    
    Args:
        questions: List of question strings
    
    Returns:
        int: Total score
    """
    total = 0
    
    for q in questions:
        while True:
            try:
                val = int(input(f"\n{q}\nYour answer (0-3): "))
                if 0 <= val <= 3:
                    total += val
                    break
                else:
                    print("⚠️  Please enter a number between 0 and 3.")
            except ValueError:
                print("⚠️  Invalid input. Please enter a number (0, 1, 2, or 3).")
            except KeyboardInterrupt:
                print("\n\nAssessment cancelled.")
                return 0
    
    return total


# ============================================================
# TESTING INTERFACE
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("    INNERVERSE ASSESSMENT MODULE")
    print("=" * 60)
    print("\nThis module provides clinical-standard screening tools.")
    print("\nIMPORTANT DISCLAIMERS:")
    print("• These are screening tools, not diagnostic instruments")
    print("• Results should be discussed with a healthcare provider")
    print("• These assessments do not replace professional evaluation")
    print("\n" + "=" * 60)
    
    choice = input("\nWhich assessment would you like to test?\n  (A) GAD-7 (Anxiety)\n  (B) PHQ-9 (Depression)\n  (Q) Quit\n\nYour choice: ").upper()
    
    if choice == "A":
        run_gad7()
    elif choice == "B":
        run_phq9()
    elif choice == "Q":
        print("\nGoodbye!")
    else:
        print("\nInvalid choice. Please run again and select A, B, or Q.")