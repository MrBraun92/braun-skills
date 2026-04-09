# Open-Meteo API Reference

Open-Meteo is a free weather API that requires no API key.

## Base URL

```
https://api.open-meteo.com/v1/forecast
```

## Common Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `latitude` | float | Latitude coordinate | `52.52` |
| `longitude` | float | Longitude coordinate | `13.41` |
| `current` | string | Current weather variables (comma-separated) | `temperature_2m,wind_speed_10m` |
| `hourly` | string | Hourly forecast variables (comma-separated) | `temperature_2m,precipitation` |
| `daily` | string | Daily forecast variables (comma-separated) | `temperature_2m_max,precipitation_sum` |
| `temperature_unit` | string | Temperature unit: `celsius` or `fahrenheit` | `celsius` |
| `wind_speed_unit` | string | Wind speed unit: `kmh`, `ms`, `mph`, `kn` | `kmh` |
| `timezone` | string | Timezone for time values | `America/New_York` |
| `forecast_days` | int | Number of forecast days (1-16) | `7` |

## Current Weather Variables

- `temperature_2m` - Air temperature at 2 meters
- `relative_humidity_2m` - Relative humidity at 2 meters
- `apparent_temperature` - Feels-like temperature
- `precipitation` - Precipitation amount
- `rain` - Rain amount
- `showers` - Shower amount
- `snowfall` - Snowfall amount
- `weather_code` - WMO weather code
- `cloud_cover` - Cloud cover percentage
- `pressure_msl` - Sea level pressure
- `surface_pressure` - Surface pressure
- `wind_speed_10m` - Wind speed at 10 meters
- `wind_direction_10m` - Wind direction at 10 meters
- `wind_gusts_10m` - Wind gusts at 10 meters

## Daily Variables

- `temperature_2m_max` - Maximum daily temperature
- `temperature_2m_min` - Minimum daily temperature
- `apparent_temperature_max` - Maximum feels-like temperature
- `apparent_temperature_min` - Minimum feels-like temperature
- `sunrise` - Sunrise time
- `sunset` - Sunset time
- `precipitation_sum` - Total precipitation
- `rain_sum` - Total rain
- `showers_sum` - Total showers
- `snowfall_sum` - Total snowfall
- `precipitation_hours` - Hours with precipitation
- `precipitation_probability_max` - Maximum precipitation probability
- `wind_speed_10m_max` - Maximum wind speed
- `wind_gusts_10m_max` - Maximum wind gusts
- `wind_direction_10m_dominant` - Dominant wind direction
- `uv_index_max` - Maximum UV index

## Weather Codes (WMO)

| Code | Description |
|------|-------------|
| 0 | Clear sky |
| 1, 2, 3 | Mainly clear, partly cloudy, overcast |
| 45, 48 | Fog and depositing rime fog |
| 51, 53, 55 | Drizzle: Light, moderate, dense |
| 56, 57 | Freezing drizzle: Light, dense |
| 61, 63, 65 | Rain: Slight, moderate, heavy |
| 66, 67 | Freezing rain: Light, heavy |
| 71, 73, 75 | Snow fall: Slight, moderate, heavy |
| 77 | Snow grains |
| 80, 81, 82 | Rain showers: Slight, moderate, violent |
| 85, 86 | Snow showers: Slight, heavy |
| 95 | Thunderstorm: Slight or moderate |
| 96, 99 | Thunderstorm with slight or heavy hail |

## Example Response

```json
{
  "latitude": 52.52,
  "longitude": 13.419,
  "timezone": "GMT",
  "current": {
    "time": "2024-01-15T10:00",
    "temperature_2m": 5.2,
    "wind_speed_10m": 12.5,
    "weather_code": 3
  },
  "daily": {
    "time": ["2024-01-15", "2024-01-16", "2024-01-17"],
    "temperature_2m_max": [8.1, 9.3, 7.5],
    "temperature_2m_min": [2.4, 3.1, 1.8],
    "precipitation_sum": [0.0, 2.5, 0.0]
  }
}
```
