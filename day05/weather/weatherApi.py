import requests


class WeatherApiClient:

    BASE_URL = "http://api.weatherapi.com/v1"

    def __init__(self, api_key):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.params = {"key": self.api_key}

    def get_lat_and_long(self, city):
        response = self.session.get(f"{self.BASE_URL}/current.json", params={"q": city})
        response.raise_for_status()
        location = response.json()["location"]
        return location["lat"], location["lon"]

    def get_current_temperature(self, city):
        response = self.session.get(f"{self.BASE_URL}/current.json", params={"q": city})
        response.raise_for_status()
        return response.json()["current"]["temp_c"]

    def get_temperature_after(self, city, days, hour=None):
        if days < 1:
            raise ValueError("days must be at least 1")

        response = self.session.get(
            f"{self.BASE_URL}/forecast.json", params={"q": city, "days": days}
        )
        response.raise_for_status()

        forecast_day = response.json()["forecast"]["forecastday"][days - 1]
        hourly = forecast_day["hour"]

        if hour is not None:
            if not (0 <= hour <= 23):
                raise ValueError("hour must be between 0 and 23")
            return hourly[hour]["temp_c"]

        return [h["temp_c"] for h in hourly]


if __name__ == "__main__":
    client = WeatherApiClient(api_key="YOUR_API_KEY_HERE")

    city = "London"

    lat, lon = client.get_lat_and_long(city)
    print(f"Coordinates of {city}: lat={lat}, lon={lon}")

    current_temp = client.get_current_temperature(city)
    print(f"Current temperature in {city}: {current_temp}°C")

    temp_tomorrow = client.get_temperature_after(city, days=1, hour=12)
    print(f"Temperature in {city} tomorrow at noon: {temp_tomorrow}°C")

    temps_day2 = client.get_temperature_after(city, days=2)
    print(f"Hourly temperatures in {city} in 2 days: {temps_day2}")
