# by Allison Dixon
# last updated October 1, 2019
# this program calculates the surface area of a rectangle


def input_length():
    """
    This function gets user input for the length of the rectangle
    :return: The length of the rectangle
    """
    return float(input("What is the length of the rectangle?"))


def input_width():
    """
    This function gets user input for the width of the rectangle
    :return: The width of the rectangle
    """
    return float(input("What is the width of the rectangle?"))


def input_height():
    """
    This function gets user input for the height of the rectangle
    :return: The height of the rectangle
    """
    return float(input("What is the height of the rectangle?"))


def area_of_rectangle(a, b):
    """
    This function finds the area of a rectangle
    :param a: Side 'a' of the rectangle
    :param b: Side 'b' of the rectangle
    :return: The area of the rectangle
    """
    return a * b


def surface_area(length, width, height):
    """
    This function finds the surface area of the rectangle
    :param length: The length of the rectangle from the user's input
    :param width: The width of the rectangle from the user's input
    :param height: The height of the rectangle from the user's input
    :return: The surface area of the rectangle
    """
    return (area_of_rectangle(length, width) * 2) + (area_of_rectangle(length, height) * 2) \
        + (area_of_rectangle(width, height) * 2)


def main():
    length = input_length()
    width = input_width()
    height = input_height()
    print(surface_area(length, width, height))


if __name__ == '__main__':
    main()
