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
    surface_area = area_of_rectangle() * 2


def main():
    print(area_of_rectangle(5,6))



main()