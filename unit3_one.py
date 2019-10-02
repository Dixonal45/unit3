# by Allison Dixon
# last updated October 1, 2019
# this program calculates the surface area of a rectangle


def input_length():
    return float(input("What is the length of the rectangle?"))


def input_width():
    width = float(input("What is the width of the rectangle?"))
    return width


def input_height():
    return float(input("What is the height of the rectangle?"))


def area_of_rectangle(length, width):
    return length * width


def surface_area(length, width, height):
    return (area_of_rectangle(length, width) * 2) + (area_of_rectangle(height, width) * 2) + (area_of_rectangle(height, length) * 2)


def main():
    print(surface_area(5, 3, 4))


main()