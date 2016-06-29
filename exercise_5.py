SMALL_DEPOSIT = .10
LARGE_DEPOSIT = .25


def bottle_deposit(small, large):
    return round(small*SMALL_DEPOSIT + large*LARGE_DEPOSIT, 2)


if __name__ == '__main__':
    small = float(input('Enter number of bottles 1 liter or less: '))
    large = float(input('Enter number of bottle over 1 liter: '))
    print('Total refund: ${:.2f}'.format(bottle_deposit(small, large)))
