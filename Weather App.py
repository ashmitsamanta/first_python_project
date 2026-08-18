import os
import sys
import requests
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

console = Console()

load_dotenv()
API_KEY = os.environ.get("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
    except requests.exceptions.RequestException:
        console.print("[bold red]❌ Error: Could not connect to the weather service.[/bold red]")
        return

    if response.status_code == 200:
        data = response.json()

        weather_desc = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']

        details = (
            f"[cyan]🌡️  Temperature:[/cyan] [bold white]{temperature}°C[/bold white] "
            f"[dim](Feels like {feels_like}°C)[/dim]\n"
            f"[yellow]☁️  Condition:[/yellow]   [bold white]{weather_desc.title()}[/bold white]\n"
            f"[blue]💧 Humidity:[/blue]    [bold white]{humidity}%[/bold white]"
        )

        weather_panel = Panel(
            details,
            title=f"[bold magenta]🌍 Weather in {city.title()}[/bold magenta]",
            border_style="green",
            expand=False
        )
        
        console.print(weather_panel)

    elif response.status_code == 404:
        console.print("[bold red]❌ Error: City not found. Check the spelling and try again.[/bold red]")
    elif response.status_code == 401:
        console.print("[bold red]❌ Error: Invalid API key. Check your .env file.[/bold red]")
    else:
        console.print(f"[bold red]❌ Error: Unexpected response from the server (status {response.status_code}).[/bold red]")

def main():
    if not API_KEY:
        console.print("[bold red]❌ No API key found. Set API_KEY in a .env file.[/bold red]")
        return

    if len(sys.argv) > 1:
        city = " ".join(sys.argv[1:])
    else:
        city = console.input("[bold green]Enter a city name: [/bold green]")
        
    console.print(f"\n[italic dim]Fetching weather data for {city.title()}...[/italic dim]\n")
    get_weather(city)

if __name__ == "__main__":
    main()