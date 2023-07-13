# Lab 7
#
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 3

# purpose- this function gets a list and breaks it into a list of list in 3 parts
def groups_of_3(listed: list) -> list:
    return [listed[i:i + 3] for i in range(0, len(listed), 3)]


# purpose- this function gets a list of list and get the last value of the list of list and makes a new list
def final_value(lista: list) -> list:
    listb = []
    for i in range(len(lista)):
        if len(lista[i]) != 0:
            listb.append(lista[i][-1])
    return listb


# purpose- this function get a list and makes a new list depending on what number it multiplies but the number
def repeat_value(lists: list) -> list:
    listed = []
    for i in range(len(lists)):
        lis = []
        if lists[i] == 0:
            listed.append([])
        else:
            for j in range(lists[i]):
                lis.append(lists[i])
            listed.append(lis)
    return listed
