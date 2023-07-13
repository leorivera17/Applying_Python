# Main Program
# Project 2: Barista Coffee Assistant
#
# Name: Your Name
# Section: Your Section
# Date:
#import baristaCoffeeFuncs
from baristaCoffeeFuncs import *

def main():
    user_input = 'y'
    while user_input == 'y':
        coffee = input_coffee()
        size = size_type()
        extra = input_extras(coffee)
        take = takeout()
        price = prices(coffee, size, extra)
        printall(coffee, extra, take, price)
        user_input = input('Would you like to make another order (y/n)? ')


if __name__ == '__main__':
    main()


