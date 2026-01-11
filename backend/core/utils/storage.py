import json
import os

FILE_PATH = "journal.json"

def load_history():
    """Loads the mood history from the JSON file."""
    if not os.path.exists(FILE_PATH):
        return [] # Return empty list if no file exists yet
    
    with open(FILE_PATH, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_entry(weather, score):
    """Saves a new entry to the JSON file."""
    history = load_history()
    
    # Create a simple entry with the weather and score
    new_entry = {
        "weather": weather,
        "score": round(score, 2)
    }
    
    history.append(new_entry)
    
    # Write back to the file
    with open(FILE_PATH, "w") as file:
        json.dump(history, file, indent=4)