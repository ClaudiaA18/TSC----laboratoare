import pytest
from car import Car

""" Exercise 0a: Write a fixture that returns a car instance. """

# TODO
@pytest.fixture
def my_car():
    return Car(50)

def test_car_accelerate(my_car):
    """ Exercise 0b: Using the just created fixture test the accelerate method. Hint: accelerate, then check. """
    # TODO
    my_car.accelerate()
    assert my_car.speed == 55

def test_car_brake(my_car):
    """ Exercise 0c: Using the just created fixture test the brake method. Hint: break, then check. """
    # TODO
    my_car.brake()
    assert my_car.speed == 45
#--------------------------------------------------------------------------------------------------------------------

speed_data = {45, 50, 75, 45}

@pytest.mark.parametrize("speed_brake", speed_data)
def test_car_brake(speed_brake):
    car = Car(50)
    car.brake()
    assert car.speed == speed_brake


""" Exercise 1a: Write a parameterized test for accelerate. You can use the speed_data dataset. """

# TODO


@pytest.mark.parametrize("speed, expected_speed", [(50, 55), (40, 45), (30, 35), (100, 90)])
def test_car_accelerate(speed, expected_speed):
    car = Car(speed)
    car.accelerate()
    assert car.speed == expected_speed


""" Exercise 1b: Write a parameterized test for brake that receives different speeds and checks the
speed update after brake method is called. Hint: Look up! """
# TODO
@pytest.mark.parametrize("speed, expected_speed", [(50, 45), (40, 35), (30, 25), (100, 95)])
def test_car_brake_parametrized(speed, expected_speed):
    car = Car(speed)
    car.brake()
    assert car.speed == expected_speed

#--------------------------------------------------------------------------------------------------------------------

""" Exercise 2a: Mark this test to be skipped. """
# TODO
@pytest.mark.skip(reason="Skipping average_speed test for now")
def test_average_speed():
    car = Car(50)
    car.step()
    assert car.average_speed() == 50


""" Exercise 2b: Write a test and mark it as skippable if Python version is less than 3.7 """
# TODO
@pytest.mark.skipif(sys.version_info < (3, 7), reason="Requires Python 3.7 or higher")
def test_python_version():
    assert True


""" Exercise 2c: Write a test you expect to fail for any of the car methods and mark it accordingly (provide a reason 
too). """
# TODO
@pytest.mark.xfail(reason="Failing test: This is expected to fail")
def test_fail_method():
    car = Car(50)
    car.accelerate()
    assert car.speed == 60 
