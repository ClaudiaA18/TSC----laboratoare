import pytest
from primes import is_prime

""" Example unit test.

Creating a unit test is as simple as creating a function beginning with 'test_' that contains an assert.

"""


def test_find_next_prime():
    """ Exercise 0a: Create a unit test with a simple assert statement for equality. """
    # TODO
    assert 5 == 5

def test_find_next_prime():
    """ Exercise 0b: Create a unit test with a simple assert statement for inequality. """
    # TODO
    assert 5 != 6

"""Exercise 0c: Mark the tests above with the tag @next_prime and run all tests with this tag. """
# TODO
@pytest.mark.next_prime
def test_find_next_prime():
    assert 5 == 5

@pytest.mark.next_prime
def test_find_next_prime_inequality():
    assert 5 != 6
"""Grouping unit tests.

Sometimes it makes sense to group unit tests: for instance, you want to keep all unit tests for a function together.
Tests can be grouped in a file, but also in a class.

Unit tests in class can share fixture-like methods that are called every time a method is called.
More info on these so-called xunit-style setups: https://doc.pytest.org/en/latest/xunit_setup.html

Run all tests in the class with: >>>pytest test_primes.py::TestIsPrime
"""


class TestIsPrime(object):
    """ Tests can be grouped in a class. """

    def test_prime(self):
        """ Create a unit test as a method with at least 3 different assert statements. """
        # TODO
	assert is_prime(7)
        assert is_prime(11)
        assert is_prime(13)

    def test_one(self):
        """ Exercise 1a: Adjust is_prime() to let this test pass. """
        # TODO
        assert is_prime(1) is False

    def test_zero(self):
        """ Exercise 1b: Adjust is_prime() to let this test pass. """
        # TODO
        assert is_prime(0) is False

    def test_negative(self):
        """ Exercise 1c: Test that negative numbers result in False and adjust
        is_prime().
        """
        # TODO
	assert is_prime(-5) is False

"""Fixtures.

Fixtures provide more and better features than the setup & teardown methods: https://doc.pytest.org/en/latest/fixture.html

Define fixtures with the decorator @pytest.fixture. Scope fixtures by giving it arguments (e.g. pytest.fixture(
'session')).

Use a fixture by specifying it as an argument for your test function.
"""


@pytest.fixture
def give_three():
    """ Fixture that returns the integer 3. """
    return 3


def test_float(give_three):
    """ Exercise 2: Use fixture give_three by specifying it as an argument. """
    # TODO
    assert give_three == 3

"""Built-in fixtures.

pytest also ships with some common fixtures so you don't have to create these yourself.

https://docs.pytest.org/en/6.2.x/fixture.html
"""
