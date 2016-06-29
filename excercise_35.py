DOG_YEARS_UNDER_TWO = 10.5
DOG_YEARS_OVER_TWO = 4


def dog_years(human_years):
    if human_years <= 0:
        raise ValueError('human years have to be greater than zero')

    if human_years > 2:
        return (2 * DOG_YEARS_UNDER_TWO) + ((human_years - 2) * DOG_YEARS_OVER_TWO)
    else:
        return human_years * DOG_YEARS_UNDER_TWO


if __name__ == '__main__':
    human_years = float(input('Enter human age of dog: '))
    print('Your dog is {} years old in dog years'.format(dog_years(human_years)))

