# Project 4 – Image
# Name: Leo Rivera
# Instructor: Dr. S. Einakian
# Section: 7
import math

def read(f_name):
    fout = open(f_name)
    header_lst = []
    for i in range(3):
        header = fout.readline()
        header_lst.append(header)
    image_data_lst = []
    for line in fout:
        line = line.split(',')
        image_data_lst.append(line)
    fout.close()
    return header_lst, image_data_lst


def process_body(image_data_lst, header_lst):
    pass


def negate(image_data_lst):
    file1 = open('negate.csv', 'w')
    count = 0
    pixel = 0
    for items in image_data_lst:
        if count < 2:
            if count == 0:
                pixel = int(items) - 255
                if pixel > 0:
                    pixel = abs(pixel)
            count += 1
        else:
            file1.write(str(pixel) + '\n' + str(pixel) + '\n' + str(pixel) + '\n')
            count = 0
    file1.close()


def high_contrast(image_data_lst):
    file2 = open('high_contrast.csv', 'w')
    count = 0
    pixel = 0
    for items in image_data_lst:
        if count < 2:
            if count == 0:
                pixel = int(items)
                if pixel > 127:
                    pixel = 255
                else:
                    pixel = 0
            count += 1
        else:
            file2.write(str(pixel) + '\n' + str(pixel) + '\n' + str(pixel) + '\n')
            count = 0
    file2.close()


def gray_scale(image_data_lst):
    file3 = open('low_contrast.csv', 'w')
    count = 0
    pixel = 0
    for items in image_data_lst:
        if count < 2:
            if count == 0:
                pixel = int(items)
                if pixel > 127:
                    pixel = 255
                else:
                    pixel = 0
            count += 1
        else:
            file3.write(str(pixel) + '\n' + str(pixel) + '\n' + str(pixel) + '\n')
            count = 0
    file3.close()


def remove_color(image_data_lst):
    file4 = open('remove_primary.csv', 'w')
    count = 0
    pixel = 0
    for items in image_data_lst:
        if count < 2:
            if count == 0:
                pixel = int(items)
                if pixel > 127:
                    pixel = 255
                else:
                    pixel = 0
            count += 1
        else:
            file4.write(str(pixel) + '\n' + str(pixel) + '\n' + str(pixel) + '\n')
            count = 0
    file4.close()


def write_files(header_lst):
    file1 = open('negate.csv', 'w')
    file2 = open('high_contrast.csv', 'w')
    file3 = open('low_contrast.csv', 'w')
    file4 = open('remove_primary.csv', 'w')
    file1.write('P3\n' + header_lst + '255\n')
    file2.write('P3\n' + header_lst + '255\n')
    file3.write('P3\n' + header_lst + '255\n')
    file4.write('P3\n' + header_lst + '255\n')
    file1.close()
    file2.close()
    file3.close()
    file4.close()
