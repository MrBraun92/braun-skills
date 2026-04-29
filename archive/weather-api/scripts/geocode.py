#!/usr/bin/env python3
"""
Geocode a location name to latitude/longitude using Open-Meteo's geocoding API.
"""
import sys
import requests


def geocode(location: str) -> dict:
    """
    Convert location name to coordinates.
    
    Args:
        location: City name or address
        
    Returns:
        dict with 'latitude', 'longitude', 'name', 'country'
    """
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": location, "count": 1, "language": "en", "format": "json"}
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    data = response.json()
    
    if "results" not in data or len(data["results"]) == 0:
        raise ValueError(f"Location '{location}' not found")
    
    result = data["results"][0]
    
    return {
        "latitude": result["latitude"],
        "longitude": result["longitude"],
        "name": result["name"],
        "country": result.get("country", ""),
        "admin1": result.get("admin1", ""),
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: geocode.py <location>")
        print("  Example: geocode.py 'New York'")
        sys.exit(1)
    
    location = " ".join(sys.argv[1:])
    
    try:
        coords = geocode(location)
        print(f"📍 {coords['name']}, {coords['country']}")
        print(f"   Latitude: {coords['latitude']}")
        print(f"   Longitude: {coords['longitude']}")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
