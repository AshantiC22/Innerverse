"""
FILE: app.py
PURPOSE: Flask server that connects the web interface to the emotion analysis engine.
FIXED ISSUES:
- Corrected function parameter mismatch
- Added state persistence to JSON file
- Improved error handling
- Added proper cooling logic
"""

from flask import Flask, render_template, request, jsonify
import json
from pathlib import Path
from engine import analyze_journal_entry, detect_intent, translate_score_to_weather

app = Flask(__name__)

# State file for persistence across server restarts
STATE_FILE = Path("house_state.json")

def load_state():
    """Load the current house state from file."""
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"heat": 0.0}
    return {"heat": 0.0}

def save_state(heat):
    """Save the current house state to file."""
    with open(STATE_FILE, 'w') as f:
        json.dump({"heat": heat}, f)

@app.route('/')
def home():
    """Serve the main HTML page."""
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    """
    Process the user's journal entry and return the atmosphere state.
    Returns JSON with: score, intent, weather, heat_level
    """
    try:
        # Load current state
        state = load_state()
        current_heat = state["heat"]
        
        # Get user input
        data = request.json
        user_text = data.get('text', '').strip()
        
        if not user_text:
            return jsonify({
                "error": "No text provided",
                "score": 0,
                "intent": None,
                "weather": "FOGGY MIST",
                "heat_level": current_heat
            }), 400
        
        # Analyze the text
        score = analyze_journal_entry(user_text)
        intent = detect_intent(user_text)
        
        # --- THERMAL LOGIC (Heat represents intensity/distress) ---
        
        # INSTANT HEAT TRIGGERS
        if intent == "ANGER":
            current_heat = 1.0  # Instant lava
        elif intent == "OVERWHELMED":
            current_heat = min(1.0, current_heat + 0.5)  # Rapid heating
        
        # COOLING LOGIC (Positive emotions cool the house)
        elif intent in ["JOY", "GRATITUDE", "EXCITEMENT"]:
            current_heat = max(0.0, current_heat - 0.4)  # Fast cooling
        elif score > 0.3:
            current_heat = max(0.0, current_heat - 0.3)  # Moderate cooling
        
        # SLOW COOLING (Neutral or slightly negative)
        elif score > -0.2:
            current_heat = max(0.0, current_heat - 0.1)  # Gentle cooling
        
        # HEATING (Negative emotions)
        elif score < -0.5:
            current_heat = min(1.0, current_heat + 0.3)  # Heating up
        
        # Natural decay over time (house slowly cools)
        current_heat = max(0.0, current_heat - 0.05)
        
        # Get the weather state
        weather = translate_score_to_weather(score, user_text)
        
        # Save the updated state
        save_state(current_heat)
        
        # Return the atmosphere data
        return jsonify({
            "score": round(score, 2),
            "intent": intent,
            "weather": weather,
            "heat_level": round(current_heat, 2)
        })
    
    except Exception as e:
        # Log the error (in production, use proper logging)
        print(f"Error processing request: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "score": 0,
            "intent": None,
            "weather": "FOGGY MIST",
            "heat_level": 0.0
        }), 500

@app.route('/reset', methods=['POST'])
def reset():
    """Reset the house state to default."""
    save_state(0.0)
    return jsonify({"message": "House reset successfully", "heat_level": 0.0})

if __name__ == '__main__':
    print("=" * 50)
    print("🏠 INNERVERSE SERVER STARTING")
    print("=" * 50)
    print("📍 Visit: http://127.0.0.1:5000")
    print("💡 Press CTRL+C to stop the server")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)