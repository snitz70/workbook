from exercise_6 import calculate_tax_and_tip


def test_calculate_tax_and_tip():
    assert calculate_tax_and_tip(25.00) == (1.75, 4.50)
