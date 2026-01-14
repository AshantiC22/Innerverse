"""
FILE: storage.py (utils/storage.py)
PURPOSE: Handles persistent storage of mood history for pattern tracking
FIXED ISSUES:
- Added timestamp to entries
- Better error handling
- Added data retrieval functions
- Improved file management
"""

import json
import os
from datetime import datetime
from pathlib import Path


# File path for the journal storage
FILE_PATH = "journal.json"


def load_history():
    """
    Loads the complete mood history from the JSON file.
    
    Returns:
        list: List of entry dictionaries, or empty list if no file exists
    """
    if not os.path.exists(FILE_PATH):
        return []
    
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        print(f"Warning: {FILE_PATH} is corrupted. Creating backup...")
        _backup_corrupted_file()
        return []
    except Exception as e:
        print(f"Error loading history: {e}")
        return []


def save_entry(weather, score, user_text=None):
    """
    Saves a new mood entry to the JSON file.
    
    Args:
        weather: String weather state (e.g., "RADIANT SUN")
        score: Float sentiment score
        user_text: Optional string of user's journal entry (first 100 chars)
    """
    try:
        history = load_history()
        
        # Create a new entry with timestamp
        new_entry = {
            "timestamp": datetime.now().isoformat(),
            "weather": weather,
            "score": round(score, 2)
        }
        
        # Optionally store a snippet of the entry (for context, not full text)
        if user_text:
            new_entry["snippet"] = user_text[:100] + ("..." if len(user_text) > 100 else "")
        
        history.append(new_entry)
        
        # Write back to the file
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4, ensure_ascii=False)
        
        return True
    
    except Exception as e:
        print(f"Error saving entry: {e}")
        return False


def get_recent_entries(count=5):
    """
    Retrieves the most recent N entries.
    
    Args:
        count: Number of entries to retrieve (default: 5)
    
    Returns:
        list: List of the most recent entries
    """
    history = load_history()
    return history[-count:] if history else []


def get_weather_pattern(days=7):
    """
    Analyzes weather patterns over the last N days.
    
    Args:
        days: Number of days to analyze (default: 7)
    
    Returns:
        dict: Weather frequency counts
    """
    history = load_history()
    recent = history[-days:] if len(history) >= days else history
    
    weather_counts = {}
    for entry in recent:
        weather = entry.get("weather", "UNKNOWN")
        weather_counts[weather] = weather_counts.get(weather, 0) + 1
    
    return weather_counts


def get_average_score(days=7):
    """
    Calculates the average mood score over the last N days.
    
    Args:
        days: Number of days to analyze (default: 7)
    
    Returns:
        float: Average score, or None if no data
    """
    history = load_history()
    recent = history[-days:] if len(history) >= days else history
    
    if not recent:
        return None
    
    scores = [entry.get("score", 0) for entry in recent]
    return sum(scores) / len(scores) if scores else None


def clear_history():
    """
    Clears all history (creates a backup first).
    Use with caution!
    """
    if os.path.exists(FILE_PATH):
        # Create backup before clearing
        backup_path = f"journal_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            import shutil
            shutil.copy(FILE_PATH, backup_path)
            print(f"Backup created: {backup_path}")
        except Exception as e:
            print(f"Could not create backup: {e}")
        
        # Clear the file
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump([], file)
        
        print("History cleared.")


def _backup_corrupted_file():
    """Internal function to backup corrupted files."""
    backup_path = f"journal_corrupted_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    try:
        import shutil
        shutil.copy(FILE_PATH, backup_path)
        print(f"Corrupted file backed up to: {backup_path}")
    except Exception as e:
        print(f"Could not backup corrupted file: {e}")


def display_history_summary():
    """
    Displays a formatted summary of the user's mood history.
    """
    history = load_history()
    
    if not history:
        print("\nNo journal entries found yet.")
        return
    
    print("\n" + "=" * 60)
    print("  📊 YOUR INNERVERSE HISTORY")
    print("=" * 60)
    print(f"\nTotal Entries: {len(history)}")
    
    # Recent entries
    print("\n--- RECENT ENTRIES ---")
    recent = get_recent_entries(5)
    for entry in recent:
        timestamp = entry.get("timestamp", "Unknown")
        weather = entry.get("weather", "UNKNOWN")
        score = entry.get("score", 0)
        
        # Format timestamp
        try:
            dt = datetime.fromisoformat(timestamp)
            time_str = dt.strftime("%Y-%m-%d %H:%M")
        except:
            time_str = timestamp
        
        print(f"\n{time_str}")
        print(f"  Weather: {weather}")
        print(f"  Score: {score:.2f}")
        
        if "snippet" in entry:
            print(f"  Entry: {entry['snippet']}")
    
    # Weather pattern
    print("\n--- 7-DAY WEATHER PATTERN ---")
    pattern = get_weather_pattern(7)
    for weather, count in sorted(pattern.items(), key=lambda x: x[1], reverse=True):
        print(f"  {weather}: {count} day(s)")
    
    # Average score
    avg = get_average_score(7)
    if avg is not None:
        print(f"\n--- 7-DAY AVERAGE SCORE ---")
        print(f"  {avg:.2f}")
        if avg > 0.3:
            print("  Trend: Generally positive")
        elif avg < -0.3:
            print("  Trend: Consider reaching out for support")
        else:
            print("  Trend: Balanced")
    
    print("\n" + "=" * 60 + "\n")


# ============================================================
# TESTING INTERFACE
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("    STORAGE MODULE TEST")
    print("=" * 60)
    
    print("\nCurrent storage file:", FILE_PATH)
    
    # Test saving entries
    print("\nTesting save_entry()...")
    save_entry("RADIANT SUN", 0.85, "I'm feeling great today!")
    save_entry("STEADY RAIN", -0.45, "Feeling a bit down.")
    save_entry("FOGGY MIST", 0.05, "Not sure how I feel.")
    print("✓ Saved 3 test entries")
    
    # Test loading history
    print("\nTesting load_history()...")
    history = load_history()
    print(f"✓ Loaded {len(history)} entries")
    
    # Test recent entries
    print("\nTesting get_recent_entries()...")
    recent = get_recent_entries(3)
    print(f"✓ Retrieved {len(recent)} recent entries")
    
    # Display full summary
    display_history_summary()
    
    # Test clearing (commented out for safety)
    # print("\nTest clear_history()? (type 'YES' to confirm)")
    # if input("> ").upper() == "YES":
    #     clear_history()
    
    print("\nStorage module test complete!")