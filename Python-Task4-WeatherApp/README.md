# Basic Weather App

**Oasis Infobyte SIP — Python Programming Track — Task 4 (Beginner Tier)**

A command-line Python application that fetches and displays real-time weather
data for any city using the [OpenWeatherMap](https://openweathermap.org/) API.

## Features

- Prompts the user for a city name or ZIP code
- Calls the OpenWeatherMap API and parses the JSON response
- Displays:
  - Current temperature in both °C and °F
  - "Feels like" temperature
  - Humidity percentage
  - Weather condition description (e.g., "Light Rain")
  - Wind speed
- Graceful error handling for:
  - City not found
  - Network timeouts
  - Invalid API key
- Input validation (rejects empty input)
- Loop to check multiple cities in one session

## Setup

1. Install the one dependency:
   ```bash
   pip install requests
   ```

2. Get a **free** API key:
   - Sign up at https://openweathermap.org/appid
   - Copy your API key (it can take a few minutes to activate after signup)

3. Add your API key. Either:
   - Open `weather_app.py` and replace `PASTE_YOUR_API_KEY_HERE`, **or**
   - Set it as an environment variable (safer — keeps your key out of git):
     ```bash
     export OWM_API_KEY="your_key_here"      # macOS/Linux
     setx OWM_API_KEY "your_key_here"        # Windows
     ```

4. Run it:
   ```bash
   python weather_app.py
   ```

## Example Session

```
=== Basic Weather App ===
Type 'quit' at any time to exit.

Enter a city name (or ZIP code): Bhubaneswar

========================================
  Weather in Bhubaneswar, IN
========================================
  Condition     : Haze
  Temperature   : 31.2°C  (88.2°F)
  Feels Like    : 36.4°C
  Humidity      : 74%
  Wind Speed    : 3.1 m/s
========================================

Check another city? (y/n): n
Goodbye!
```

## Tech Stack

- Python 3
- `requests` library
- OpenWeatherMap Current Weather Data API (free tier)

## Notes on Error Handling

| Scenario | Behaviour |
|---|---|
| Empty input | Re-prompts without calling the API |
| Unknown city | Catches HTTP 404, shows a friendly message |
| Invalid API key | Catches HTTP 401, tells the user to check their key |
| No internet / DNS failure | Catches `ConnectionError` |
| Slow/unresponsive server | Catches `Timeout` after 6 seconds |

## Possible Next Steps (Advanced Tier)

- Wrap this in a `tkinter` GUI with a "Get Weather" button
- Add hourly/5-day forecast panels (One Call API)
- Add a Celsius/Fahrenheit toggle button
- Auto-detect location via IP using `ipinfo.io`
