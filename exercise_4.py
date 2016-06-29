ACRE_SQAURE_FEET = 43560


def acerage(length, width):
    return round((length*width)/ACRE_SQAURE_FEET, 2)


if __name__ == '__main__':
    length = float(input('Enter length of field: '))
    width = float(input('Enter width of field: '))
    print('The field is {} acres.'.format(acerage(length, width)))


