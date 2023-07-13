# Lab 7
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 7


# purpose- this function gets a list and breaks it into a list of list in 3 parts
def groups_of_4(lst : list) -> list:
    return [lst[i:i + 4] for i in range(0, len(lst), 4)]


# purpose- this function gets a list of list and get the last value of the list of list and makes a new list
def search_2D(lst, num):
    main_lst = []
    sub = ()
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[j][i] == num:
                sub += (lst[i], lst[i][j] - 2)
                main_lst.append(sub)
    return main_lst

def add_values(lst):
    n = 0
    for num in range(len(lst)):
        if type(num) in [int, float]:
            n += num
        if type(num) in [list]:
            n += num
    return n



