# Main Program
# Project 2: Barista Coffee Assistant
#
# Name: Your Name
# Section: Your Section
# Date:
#
from baristaCoffee import *


# signature: none -> string
# purpose: asks use what type of coffee they want
def input_coffee():
    count = 1
    coffee = input('What coffee type would you like? ')
    while coffee.lower() not in ['americano', 'latte', 'flat white', 'espresso']:
        #, 'Americano', 'AMERICANO','LATTE', 'Latte', 'FLAT WHITE', 'Flat white', 'ESPRESSO', 'Espresso'
        print("Can you please try again?")
        coffee = input('What coffee type would you like? ')
        count += 1
        if count == 3:
            exit('Sorry, we cannot help you here.')
    return coffee.lower()


# signature: none -> str
# purpose: asks user what size they would like
def size_type():
    count = 1
    size = input('What size do you want [Large, Medium, Small]? ')
    while size.lower() not in ['large', 'medium', 'small']:
        #, 'Large', 'Medium', 'Small', 'LARGE', 'MEDIUM', 'SMALL'
        print("Can you please try again?")
        size = input('What size do you want [Large, Medium, Small]? ')
        count += 1
        if count == 3:
            exit('Sorry, we cannot help you here.')
    return size.lower()


# signature: none -> str
# purpose: asks user to choose if they want an extra
def input_extras(coffee):
    count = 1
    if coffee not in ['americano', 'espresso']:
        #'Americano', 'AMERICANO', 'ESPRESSO', 'Espresso',
        return 'No extras'
    if coffee in ['americano', 'espresso']:
        #'Americano', 'AMERICANO', 'ESPRESSO', 'Espresso',
        extra = input('Would you like milk on the side [y, n]? ')
        while extra not in ['y', 'n', 'Y', 'N']:
            print("Can you please try again?")
            extra = input('Would you like milk on the side [y, n]? ')
            count += 1
            if count == 3:
                exit('Sorry, we cannot help you here.')
        if extra in ['y', 'Y']:
           return 'Milk on the side'
        if extra in ['n', 'N']:
            return 'No extras'
        return extra.lower()


# signature: none -> str
# purpose: asks user if they want to take out the order or not
def takeout():
    count = 1
    take = input('Is your coffee takeout [y, n]? ')
    while take not in ['y', 'n', 'Y', 'N']:
        print("Can you please try again?")
        take = input('Is your coffee takeout [y, n]? ')
        count += 1
        if count == 3:
            exit('Sorry, we cannot help you here.')
    if take in ['y', 'Y']:
        return 'Takeout'
    if take in ['n', 'N']:
        return 'In Cafe'


# signature: none -> int
# purpose: calculates the price depending on what is chosen
def prices(coffee, size, extra):

    if coffee in ['flat white'] and size in ['large']:
        #, 'Large', 'LARGE'
        #'FLAT WHITE', 'Flat white',
        price = 3.75
        return price
    if coffee in ['flat white'] and size in ['medium']:
        #, 'Medium', 'MEDIUM'
        #'FLAT WHITE', 'Flat white',
        price = 3.00
        return price
    if coffee in ['flat white'] and size in ['small']:
        #, 'Small', 'SMALL'
        #'FLAT WHITE', 'Flat white',
        price = 2.95
        return price
    if coffee in ['americano'] and size in ['large']:
        #, 'Large', 'LARGE'
        #,'Americano', 'AMERICANO'
        price = 3.25
        if extra in ['No extras']:
            return price
        if extra in['Milk on the side']:
            return price + 0.25
    if coffee in ['americano'] and size in ['medium']:
        #, 'Medium', 'MEDIUM'
        #,'Americano', 'AMERICANO'
        price = 2.95
        if extra in ['No extras']:
            return price
        if extra in['Milk on the side']:
            return price + 0.25
        return price
    if coffee in ['americano'] and size in ['small']:
        #, 'Small', 'SMALL'
        #,'Americano', 'AMERICANO'
        price = 2.75
        if extra in ['No extras']:
            return price
        if extra in['Milk on the side']:
            return price + 0.25
        return price
    if coffee in ['espresso'] and size in ['large']:
        #, 'Large', 'LARGE'
        #'ESPRESSO', 'Espresso',
        price = 3.25
        if extra in ['No extras']:
            return price
        if extra in['Milk on the side']:
            return price + 0.25
        return price
    if coffee in ['espresso'] and size in ['medium']:
        #, 'Medium', 'MEDIUM'
        #'ESPRESSO', 'Espresso',
        price = 2.95
        if extra in ['No extras']:
            return price
        if extra in['Milk on the side']:
            return price + 0.25
        return price
    if coffee in ['espresso'] and size in ['small']:
        #, 'Small', 'SMALL'
        #'ESPRESSO', 'Espresso',
        price = 2.75
        if extra in ['No extras']:
            return price
        if extra in['Milk on the side']:
            return price + 0.25
        return price
    if coffee in ['latte'] and size in ['large']:
        #, 'Large', 'LARGE'
        #'LATTE', 'Latte',
        price = 4.15
        return price
    if coffee in ['latte'] and size in ['medium']:
        #, 'Medium', 'MEDIUM'
        #'LATTE', 'Latte',
        price = 3.75
        return price
    if coffee in ['latte'] and size in ['small']:
        #, 'Small', 'SMALL'
        #'LATTE', 'Latte',
        price = 2.85
        return price


# signature:
# purpose:
def printall(coffee, extra, take, price):
    print(coffee)
    print(extra)
    print(take)
    print('Please pay $',price, 'to the cashier.')




