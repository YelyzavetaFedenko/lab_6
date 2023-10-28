import pytest
from main import Car, Bicycle

# Test the Car class


def test_car_acceleration():
    car = Car(speed=100, power=150, fuel="Бензин")
    car.accelerate(30)
    assert car.speed == 130


def test_car_fuel():
    car = Car(speed=100, power=150, fuel="Бензин")
    assert car.fuel == "Бензин"


# Test the Bicycle class
def test_bicycle_acceleration():
    bicycle = Bicycle(speed=20, power=5, pedals=2)
    bicycle.accelerate(10)
    assert bicycle.speed == 30


def test_bicycle_pedals():
    bicycle = Bicycle(speed=20, power=5, pedals=2)
    assert bicycle.pedals == 2


# Run the tests
if __name__ == "__main__":
    import pytest
    pytest.main()
