import os
import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Path to your database
# This logic looks for the file in the parent directory (core/) 
# instead of the current directory (utils/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "journal.json")

console = Console()

def display_emotional_forecast():
    try:
        with open(FILE_PATH, "r") as file:
            history = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        console.print("[bold red]No history found yet. Start journaling to see your forecast![/bold red]")
        return

    # 1. Summary Statistics
    total_entries = len(history)
    weather_counts = {}
    
    for entry in history:
        w = entry.get("weather", "UNKNOWN")
        weather_counts[w] = weather_counts.get(w, 0) + 1

    # 2. Create a Beautiful Table
    table = Table(title="🌌 YOUR INNERVERSE FORECAST", title_style="bold magenta")
    
    table.add_column("Weather State", style="cyan", no_wrap=True)
    table.add_column("Frequency", justify="center", style="yellow")
    table.add_column("Visual", justify="center")

    icons = {
        "RADIANT SUN": "☀️",
        "CLEAR SKIES": "🌤️",
        "FOGGY MIST": "🌫️",
        "STEADY RAIN": "🌧️",
        "THUNDERSTORM": "⛈️"
    }

    for weather, count in weather_counts.items():
        table.add_row(weather, str(count), icons.get(weather, "❓"))

    # 3. Output to Terminal
    console.print(Panel(f"Analyzed [bold green]{total_entries}[/bold green] total journal entries.", expand=False))
    console.print(table)

    # 4. Final Insight
    if "THUNDERSTORM" in weather_counts and weather_counts["THUNDERSTORM"] > 2:
        console.print("\n[bold yellow]Insight:[/bold yellow] You've had several storms lately. Remember to use your coping tools!")

if __name__ == "__main__":
    display_emotional_forecast()