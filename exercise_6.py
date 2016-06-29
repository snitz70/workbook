TAX = .07
TIP = .18


def calculate_tax_and_tip(meal_cost):
    _tax = round(meal_cost * TAX, 2)
    _tip = round(meal_cost * TIP, 2)

    return _tax, _tip


if __name__ == '__main__':
    meal_cost = float(input('Enter cost of meal: '))
    print('Meal {:>10.2f}'.format(meal_cost))
    tax, tip = calculate_tax_and_tip(meal_cost)
    print('Tax {:>10.2f}'.format(tax))
    print('Tip {:>10.2f}'.format(tip))
    print('Total {:>10.2f}'.format(meal_cost + tax + tip))
