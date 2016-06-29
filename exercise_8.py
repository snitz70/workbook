WIDGETS = 75
GIZMOS = 112


def widgets_and_gizmos(widgets, gizmos):
    return widgets * WIDGETS + gizmos * GIZMOS


if __name__ == '__main__':
    widgets = int(input('Enter number of widgets: '))
    gizmos = int(input('Enter number of gizmos: '))
    print('Total weight for widgets and gizmos is {} grams'.format(
        widgets_and_gizmos(widgets, gizmos)
    ))