import httpx

from src.app.core.schemas import CurrentWeatherData


class WeatherClient:
    BASE_URL = "https://api.open-meteo.com/v1/"

    async def fetch_current_weather_async(self, latitude: float, longitude: float) -> CurrentWeatherData:
        url = f"{self.BASE_URL}forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True,
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()["current_weather"]
            return CurrentWeatherData(**data)

    def fetch_current_weather_sync(self, latitude: float, longitude: float) -> CurrentWeatherData:
        url = f"{self.BASE_URL}forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True,
        }
        with httpx.Client() as client:
            response = client.get(url, params=params)
            response.raise_for_status()
            data = response.json()["current_weather"]
            return CurrentWeatherData(**data)
