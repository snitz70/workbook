def integer_sum(number):
    return int((number * (number+1)) / 2)


if __name__ == '__main__':
    number = int(input('Enter a number to calculate sum for: '))
    print('The sum of numbers 1-{} is {}'.format(number, integer_sum(number)))
