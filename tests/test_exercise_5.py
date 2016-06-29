from exercise_5 import bottle_deposit


def test_calculate_bottle_deposit_refunded():
    assert bottle_deposit(10, 6) == 2.50