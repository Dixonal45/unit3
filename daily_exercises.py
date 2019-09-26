# by Allison Dixon
# last updated September 25, 2019
# daily function exercises

# This program (1) creates egg.py


def make_top_of_hexagon():
    print("   ________   ")
    print("  /        \\ ")
    print(" /          \\")


def make_bottom_of_hexagon():
    print(" \\          / ")
    print("  \\________/  ")


def make_quote_lines():
    print(" _\"_\'_\"_\'_\"_")


# This program (2) prints happy birthday


def happy_birthday():
    print("Happy Birthday to you")


def dear_name(x):
    print("Happy Birthday dear", x)


# This program (3) adds two numbers together


def add(x, y):
    return x + y


def main():
    make_top_of_hexagon()
    make_bottom_of_hexagon()
    make_quote_lines()
    make_top_of_hexagon()
    make_bottom_of_hexagon()
    make_quote_lines()
    make_bottom_of_hexagon()
    make_top_of_hexagon()
    make_quote_lines()
    make_bottom_of_hexagon()
    happy_birthday()
    happy_birthday()
    dear_name("Scoutie")
    happy_birthday()
    answer = add(7, 8)
    print("The answer is", answer)


main()
