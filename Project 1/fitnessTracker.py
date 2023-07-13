# Main Program
# Project 1 Fitness Tracking
#
# Name: Leo Rivera
# Section: 3
# Date:1/14/22
from fitnessTrackerFuncs import *


def main():
    welcome()
    user_input = 'y'
    while user_input == 'y':
        name = input_name()
        age = input_age()
        height = input_height()
        weight = input_weight()
        duration = input_duration()
        exercise_type = input_exercise_type()
        weight_kg = convert_lb_to_kg(weight)
        miles = compute_equivalent_miles(height, exercise_type, duration)
        met_value = compute_MET(exercise_type)
        calories_burned = compute_calorie_burned(duration, weight_kg, met_value)
        BMI = compute_BMI(weight, height)
        category = BMI_category(BMI)
        print_info(name, age, height, weight, miles, calories_burned, category, BMI)
        user_input = input('Do you want to apply fitness tracking for another user (y/n)? ')


if __name__ == '__main__':
    main()
