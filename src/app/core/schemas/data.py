from pydantic import BaseModel


class CurrentWeatherData(BaseModel):
    temperature: float
    windspeed: float
    winddirection: int
    weathercode: int
