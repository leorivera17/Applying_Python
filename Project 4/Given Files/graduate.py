# Project 4 – Graduate Rate (2017-2018)
# Name: Leo Rivera
# Instructor: Dr. S. Einakian
# Section: 3
# main program
from graduate_funcs import *


def main():
    header, lst = read_file('graduate_rate.csv')
    div_lst_obj = create_division(lst)
    grad_lst_obj = create_graduate(lst)
    create_files(grad_lst_obj)
    lst_avg_tot = find_total_avg(div_lst_obj, grad_lst_obj)
    major = input('Search up major you need: ')
    males, females = find_graduate_rate(grad_lst_obj, major)
    totally = total_of_computer(grad_lst_obj)
    print('Total of Processed Graduate in Computer and information sciences and support: ', totally)
    avg_f, avg_m = science(grad_lst_obj)
    print('Average of Processed Female and Male in '
          'Computer and information sciences and support: ' +
          '(Males :', round(avg_m, 2), ', Females: ', round(avg_f, 2), ')')
    male, female = in_all(grad_lst_obj)
    print('Total of all Females and Males Graduate in all Majors: ', male, female)


if __name__ == '__main__':
    main()
