---
name: weather-api
description: Weather data retrieval using the Open-Meteo API. Use when users request weather forecasts, current conditions, or historical weather data for any location. No API key required.
license: MIT
---

# Weather API

Retrieve weather data using the free Open-Meteo API with no authentication required.

## Quick Start

### Step 1: Get Coordinates

If location name is provided, convert to coordinates using the geocoding script:

```bash
python /home/ubuntu/skills/weather-api/scripts/geocode.py "New York"
```

### Step 2: Fetch Weather Data

Use Python's `requests` library to call the API:

```python
import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "current": "temperature_2m,wind_speed_10m,weather_code",
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "temperature_unit": "celsius",
    "timezone": "America/New_York",
    "forecast_days": 7
}

response = requests.get(url, params=params)
data = response.json()
```

### Step 3: Parse and Present

Extract relevant data and format for user:

```python
current = data["current"]
daily = data["daily"]

print(f"Current: {current['temperature_2m']}°C")
print(f"Wind: {current['wind_speed_10m']} km/h")
```

## Common Use Cases

### Current Weather

Request current conditions with:
- `current="temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m"`

### 7-Day Forecast

Request daily forecast with:
- `daily="temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max,wind_speed_10m_max"`
- `forecast_days=7`

### Hourly Forecast

Request hourly data with:
- `hourly="temperature_2m,precipitation,weather_code"`
- Include `forecast_days` parameter for extended forecasts

## API Details

Read `/home/ubuntu/skills/weather-api/references/open_meteo_api.md` for:
- Complete parameter reference
- Available weather variables
- Weather code interpretations
- Response format examples

## Helper Scripts

### geocode.py

Convert location names to coordinates:

```bash
python /home/ubuntu/skills/weather-api/scripts/geocode.py "Tokyo"
```

Returns latitude, longitude, and location details.

## Best Practices

- Always specify `timezone` parameter for accurate time values
- Use `temperature_unit` and `wind_speed_unit` to match user's preference
- Include `weather_code` for condition descriptions
- Limit `forecast_days` to 7 for most use cases (max 16)
- Handle API errors gracefully with try-except blocks
