# Project 4 – Image
# Name: Leo Rivera
# Instructor: Dr. S. Einakian
# Section: 7
# main program

import imageFuncs
from imageFuncs import *


def main():
    header_lst, image_data_lst = read('ny.ppm')
    write_files(header_lst)
    negate(image_data_lst)
    high_contrast(image_data_lst)
    gray_scale(image_data_lst)
    remove_color(image_data_lst)
    process_body(image_data_lst, header_lst)


if __name__ == '__main__':
    main()
