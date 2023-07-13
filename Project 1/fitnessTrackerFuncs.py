# Project 1 Fitness Tracking
#
# Name: Leo Rivera
# Section: 3
# Date:1/14/22

# purpose: This will print the welcome text
# signature: none -> float
def welcome():
    print('Welcome to Fitness Tracker Application')
    print('To begin you must specify the participant"s name, age, height, (in inches), weight (in lb), '
          'exercise duration (in minutes), and exercise type (1-4)! Now you can compute the burned '
          'calories and BMI.')


# purpose: This will print the name on the application
# signature: none -> float
def input_name():
    print('Enter the name: ', end="")
    name = input()
    return name


# purpose: This function will print age that is greater than 0
# signature: None -> int
def input_age():
    # print('Enter age: ', end="")
    age = int(input('Enter age: '))
    # age = int(age)
    while age < 0:
        print("Error: age must be an integer > 0! ")
        age = int(input('Enter age: '))
    return age

    # if Age > 0:
    #   return
    # else:
    #   print('Error: Age must be greater than 0')
    # while True:
    #   x = input_age()
    #   return x
    #  Age = int(x)
    #   if x.strip() == Age > 0:
    #      break


# purpose: This function will print height that is greater than 0
# signature: None -> int
def input_height():
    height = int(input('Enter height in inches: '))
    # print('Enter height in inches: ', height)
    while height < 1:
        print("Error: height must be greater than 0! ")
        height = int(input('Enter height in inches : '))
    return height


# purpose: This function will weight age that is greater than 0
# signature: None -> int
def input_weight():
    weight = int(input('Enter in weight in lbs: '))
    # print('Enter in weight in lbs: ', weight)
    while weight < 0:
        print("Error: weight must be greater than 0! ")
        weight = int(input('Enter weight in pounds: '))
    return weight


# purpose: This function will print duration that is greater than 0
# signature: None -> int
def input_duration():
    duration = int(input('Enter duration of exercise in minutes: '))
    # print('Enter duration of exercise in minutes: ', duration)
    while duration < 1:
        print("Error: duration must be greater than 0! ")
        duration = int(input('Enter duration of exercise in minutes: '))
    return duration


# purpose: This function will print exercise type that is between 1 and 4.
# signature: None -> int
def input_exercise_type():
    exercise_type = int(input('Enter exercise type: 1) low-impact 2) high-impact 3) slow-paced 4) fast-paced '))
    # print('Enter exercise type: ', exercise)
    while (exercise_type < 1) or (exercise_type > 4):
        print("Error: exercise type must be an integer between [1,4]!")
        exercise_type = int(input('Enter exercise type [1,4]: '))
    return exercise_type


# purpose: prints the results
# signature: none -> strings
def print_info(name, age, height, weight, miles, calorie_burned, category, BMI):
    print("               Name : ", name)
    print('                Age : ', age)
    print('             Height : %6.2f' % height, 'inches')
    print('             Weight : %6.2f' % weight, 'lbs')
    print('              Miles : %6.2f' % miles)
    print('    Burned Calories : %6.2f' % calorie_burned)
    print('                BMI : ', category)
    print('       BMI Category : %6.2f ' % BMI)


# purpose: coverts pounds to kilograms
# signature:
def convert_lb_to_kg(weight):
    weight_kg = weight * 0.45359237
    return weight_kg


# purpose: converts height and exercise type and duration to miles
# signature: int -> int
def compute_equivalent_miles(height, exercise_type, duration):
    miles = (0.413 * height) / 12
    if exercise_type == 1:
        steps = 120
    elif exercise_type == 2:
        steps = 227
    elif exercise_type == 3:
        steps = 100
    elif exercise_type == 4:
        steps = 152
    return (duration * miles * steps) / 5280


# purpose:
# signature:
def compute_calorie_burned(duration, weight_kg, met_value):
    calories_burned = duration * ((met_value * 3.5 * weight_kg) / 200)
    return calories_burned


# purpose:
# signature:
def compute_MET(exercise_type):
    if exercise_type == 1:
        met_value = 5
    elif exercise_type == 2:
        met_value = 7
    elif exercise_type == 3:
        met_value = 3
    elif exercise_type == 4:
        met_value = 4
    else:
        print('Error: System Error')
    return met_value


# purpose:
# signature:
def compute_BMI(weight, height):
    category = 703 * weight / height ** 2
    return category


# purpose:
# signature: float -> str
def BMI_category(BMI):
    if BMI < 18.59:
        return 'Underweight'
    elif 18.59 <= BMI < 25:
        return 'Normal Weight'
    elif 25 < BMI < 30:
        return 'OverWeight'
    else:
        return 'Obesity'
