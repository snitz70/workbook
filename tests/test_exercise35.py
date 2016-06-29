from hamcrest import *
from excercise_35 import dog_years


def test_dog_years_over_2():
    assert dog_years(3) == 25


def test_dog_years_under_2():
    assert dog_years(2) == 21


def test_negative_number():
    assert_that(calling(dog_years).with_args(-1), raises(ValueError))
