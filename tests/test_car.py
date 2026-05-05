from library.Car import Car
import pytest

@pytest.mark.parametrize("fuel_level,distance,expected_fuel_level",
    [
        (47.0,  100,  37.0), # positive case
        (47.0,  "@@", 37.0), # negative case
        (-32.0, 100, -42.0)  # negative case
    ]
)
@pytest.mark.tags("TC01", "fuel")
def test_verify_that_when_users_drive_car_then_fuel_level_should_be_dropped(fuel_level, distance, expected_fuel_level):
    ferrari = Car("Ferrari", "X", "2020", "yellow", fuel_level)
    ferrari.drive(distance)

    assert ferrari.fuel_level == expected_fuel_level

@pytest.mark.tags("TC02", "fuel")
def test_verify_that_users_can_refuel_car():
    ferrari = Car("Ferrari", "X", "2020", "yellow", 10.0)
    ferrari.refuel(7.0)

    assert ferrari.fuel_level == 17.0

@pytest.mark.tags("TC03", "engine")
def test_verify_that_users_can_start_engine():
    ferrari = Car("Ferrari", "X", "2020", "yellow", 10.0)
    ferrari.start_engine()

    assert ferrari.is_engine_on == True

@pytest.mark.tags("TC04", "engine")
def test_verify_that_users_can_stop_engine():
    ferrari = Car("Ferrari", "X", "2020", "yellow", 10.0)
    ferrari.start_engine()
    ferrari.stop_engine()

    assert ferrari.is_engine_on == False