"""
FILE: interface.py
PURPOSE: Handles all User Interface (UI) elements, including typewriter effects 
and color-coded terminal panels using the 'rich' library.
"""

import time
import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Initialize the Rich Console
console = Console()

def slow_print(message, delay=0.03):
    """
    Prints text one character at a time to create a 'human' feel.
    Use this for headers or information that doesn't require a user response.
    """
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # New line at the end

def slow_input(prompt, delay=0.03):
    """
    Prints a prompt slowly AND waits for the user to type an answer.
    This returns the string the user types, preventing 'NoneType' errors.
    """
    for char in prompt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    # This is the vital fix: capture and return the input
    user_response = input(" ")
    return user_response

def display_report(weather, score, description):
    """
    Takes the weather state and score, then displays it inside a 
    beautiful, color-coded Rich Panel.
    """
    
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
    
    # Create the text object for the panel body
    # We strip the description to remove any double-headers from engine.py
    clean_description = description.split("---")[-1].strip()
    
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

def clear_console():
    """Simple utility to clear the terminal screen."""
    print("\033[H\033[J", end="")