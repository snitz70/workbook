def area(length, width):
    """Calculate the area given the
    length and width"""

    return float(length * width)


if __name__ == '__main__':
    length = float(input('Enter the length of the room: '))
    width = float(input('Enter the width of the room: '))

    print('The area of the room is {} feet.'.format(area(length, width)))
