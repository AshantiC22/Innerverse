"""
FILE: interface.py (utils/interface.py)
PURPOSE: Handles all User Interface (UI) elements, including typewriter effects
         and color-coded terminal panels using the 'rich' library.
FIXED ISSUES:
- Added fallback for when 'rich' is not installed
- Better error handling
- Improved formatting
"""

import time
import sys

# Try to import Rich, but provide fallback if not available
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    RICH_AVAILABLE = True
    console = Console()
except ImportError:
    RICH_AVAILABLE = False
    print("Note: 'rich' library not found. Using plain text mode.")
    print("Install with: pip install rich")


def slow_print(message, delay=0.03):
    """
    Prints text one character at a time to create a 'human' feel.
    Use this for headers or information that doesn't require a user response.
    
    Args:
        message: String to print
        delay: Seconds between each character (default: 0.03)
    """
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # New line at the end


def slow_input(prompt, delay=0.03):
    """
    Prints a prompt slowly AND waits for the user to type an answer.
    
    Args:
        prompt: String to display as prompt
        delay: Seconds between each character (default: 0.03)
    
    Returns:
        str: The user's input
    """
    for char in prompt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    # CRITICAL FIX: Capture and return the input
    user_response = input(" ")
    return user_response


def display_report(weather, score, description):
    """
    Takes the weather state and score, then displays it inside a
    beautiful, color-coded panel (if Rich is available).
    
    Args:
        weather: String weather state (e.g., "RADIANT SUN")
        score: Float sentiment score
        description: String description from engine
    """
    
    if RICH_AVAILABLE:
        _display_report_rich(weather, score, description)
    else:
        _display_report_plain(weather, score, description)


def _display_report_rich(weather, score, description):
    """Display report using Rich library with colors and panels."""
    
    # Map weather states to Rich colors
    color_map = {
        "RADIANT SUN": "bold yellow",
        "CLEAR SKIES": "bright_blue",
        "PARTLY CLOUDY": "cyan",
        "FOGGY MIST": "grey70",
        "STEADY RAIN": "blue",
        "THUNDERSTORM": "bold red"
    }
    
    # Default to white if weather doesn't match
    style = color_map.get(weather, "white")
    
    # Clean the description (remove any double-headers from engine.py)
    if "---" in description:
        clean_description = description.split("---")[-1].strip()
    else:
        clean_description = description.strip()
    
    # Create the text object for the panel body
    content = Text()
    content.append(f"{clean_description}\n", style=style)
    content.append(f"\nMood Index: {score:.2f}", style="italic dim")
    
    # Print the Panel to the console
    console.print(
        Panel(
            content,
            title=f"[bold]{weather}[/bold]",
            subtitle="Innerverse Atmosphere",
            border_style=style,
            expand=False
        )
    )


def _display_report_plain(weather, score, description):
    """Display report using plain text (fallback when Rich not available)."""
    
    # Clean the description
    if "---" in description:
        clean_description = description.split("---")[-1].strip()
    else:
        clean_description = description.strip()
    
    # Create ASCII box
    width = 60
    print("\n" + "=" * width)
    print(f"  {weather}".center(width))
    print("=" * width)
    print()
    
    # Print description with word wrapping
    words = clean_description.split()
    line = ""
    for word in words:
        if len(line) + len(word) + 1 <= width - 4:
            line += word + " "
        else:
            print(f"  {line.strip()}")
            line = word + " "
    if line:
        print(f"  {line.strip()}")
    
    print()
    print(f"  Mood Index: {score:.2f}".center(width))
    print("=" * width)
    print(f"  Innerverse Atmosphere".center(width))
    print("=" * width + "\n")


def clear_console():
    """Simple utility to clear the terminal screen."""
    print("\033[H\033[J", end="")


def print_header(title):
    """
    Prints a formatted header.
    
    Args:
        title: String to display as header
    """
    width = 60
    print("\n" + "=" * width)
    print(f"  {title}".center(width))
    print("=" * width + "\n")


def print_separator():
    """Prints a visual separator line."""
    print("-" * 60)


# ============================================================
# TESTING INTERFACE
# ============================================================

if __name__ == "__main__":
    print_header("INTERFACE MODULE TEST")
    
    print("Testing slow_print...")
    slow_print("This text appears character by character.", delay=0.02)
    
    print("\nTesting slow_input...")
    response = slow_input("What's your name?", delay=0.02)
    print(f"You said: {response}")
    
    print("\nTesting display_report...")
    test_description = "☀️ ✨ 🌈\nTHE SKY IS GLOWING! Your energy is radiant."
    display_report("RADIANT SUN", 0.85, test_description)
    
    print("\nTesting different weather states...")
    weathers = [
        ("CLEAR SKIES", 0.5, "It's a calm, bright day."),
        ("FOGGY MIST", -0.05, "Visibility is low."),
        ("THUNDERSTORM", -0.8, "The atmosphere is heavy.")
    ]
    
    for weather, score, desc in weathers:
        display_report(weather, score, desc)
        time.sleep(1)
    
    print("\nInterface module test complete!")