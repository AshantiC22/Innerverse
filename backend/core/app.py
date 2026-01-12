from flask import Flask, render_template, request, jsonify
# Import your verified logic functions
from engine import analyze_journal_entry, translate_score_to_weather, detect_intent
from security import check_for_crisis 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    user_input = data.get('text')
    
    # 1. Check for Crisis First
    is_crisis = check_for_crisis(user_input)
    if is_crisis:
        return jsonify({
            "weather": "CRISIS",
            "avatar_msg": "🚨 Please reach out for support. Dial 988.",
            "is_crisis": True
        })

    # 2. Run Analysis
    score = analyze_journal_entry(user_input)
    weather = translate_score_to_weather(score, user_input)
    intent = detect_intent(user_input)
    
    # 3. Handle Special Skill Triggers (Logic for Frontend)
    skill_needed = None
    if intent == "OVERWHELMED":
        skill_needed = "breathing"
    elif intent == "ANXIETY" or weather == "FOGGY MIST":
        skill_needed = "grounding"

    return jsonify({
        "weather": weather,
        "score": round(score, 2),
        "intent": intent,
        "skill": skill_needed,
        "is_crisis": False
    })

if __name__ == '__main__':
    app.run(debug=True)