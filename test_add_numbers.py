
import pytest
import requests


class Request_from_Weather:
    def __init__(self, apid):
        self.url = "https://api.openweathermap.org/data/2.5/weather"
        self.api_key = apid

    def __get_info(self, city):
        result = requests.get(self.url)
        if result.status_code == 200:
            return result.json()
        else:
            return result.text

    def get_weather(self, city):
        try:
            data = self.__get_info(city)
            return dict(city=data("name"), temperature=data["main"]["temp"])
        except TypeError:
            return None

if __name__ == "__main__":
    api_key = "https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={API key}"
    weathers = Request_from_Weather(api_key)
    city = "London"
    print(weathers.get_weather(city))


@pytest.fixture()
def weather_test_code(apid):
    return Request_from_Weather(apid)

def test_requests_result():
    city = "london"
    result = weather_test_code().get_weather()

    assert "city" in result
    assert "temperature" in result
    assert result["city"] == city
    assert apid is True
        print('Error')
    assert "error" in result
    assert result["error"] == "City not found or invalid API key"