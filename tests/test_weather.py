import pytest

from library.Weather import Weather

@pytest.mark.parametrize("temperature, humidity, chance_of_rain", [
    (10, 20, 30), 
    (25, 80, 90), 
    (15, 50, 60),
    (30, 90, 95),
])
@pytest.mark.tags("TC01")
def test_verify_that_today_should_not_be_rainy_day(temperature, humidity, chance_of_rain):
    todayWeatherObj = Weather(temperature, humidity, chance_of_rain)
    isTodayRainy = todayWeatherObj.check_rain()

    assert not isTodayRainy