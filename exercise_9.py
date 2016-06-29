INTEREST_RATE = .04


def compound_interest(amount):
    return amount * INTEREST_RATE


if __name__ == '__main__':
    amount = float(input('Enter starting amount: '))
    oneyr = compound_interest(amount)
    twoyr = compound_interest(amount+oneyr)
    threeyr = compound_interest(amount+oneyr+twoyr)

    print('amount after 1 year:  {:.2f}'.format((oneyr+amount)))
    print('amount after 2 years {:.2f}'.format(twoyr+amount+oneyr))
    print('amount after 3 years {:.2f}'.format(oneyr+twoyr+threeyr+amount))
