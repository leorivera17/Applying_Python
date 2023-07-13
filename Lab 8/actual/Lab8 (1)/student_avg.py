# Lab 8
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 3

# purpose - function reads the file and makes a list to use
def read(std)-> list:
    fout = open(std)
    lst = []
    for word in fout:
        lst.append(word)
    fout.close()
    return lst


# purpose - calculate the average in tot, for cpe, and ee
def average(lst) -> tuple:
    tot = cnt = 0
    ee_tot = ee_cnt = 0
    cpe_tot = cpe_cnt = 0
    for line in lst:
        line = line.split()
        tot += float(line[3])
        cnt += 1
        if line[2] == 'EE':
            ee_cnt += 1
            ee_tot += float(line[3])
        if line[2] == 'CPE':
            cpe_cnt += 1
            cpe_tot += float(line[3])
    cpe_avg = cpe_tot / cpe_cnt
    ee_avg = ee_tot / ee_cnt
    avg = tot / cnt
    return ee_avg, cpe_avg, avg


# purpose - write the average of each wanted major in the end of the txt
def write(file, ee_avg, cpe_avg, avg, lst)-> None:
    fout = open(file, 'w')
    for line in lst:
        fout.write(line)
    fout.write('EE average = %.2f' % ee_avg + '\n')
    fout.write('CPE average = %.2f' % cpe_avg + '\n')
    fout.write('Total average = %.2f' % avg + '\n')
    fout.close()


def main():
    lst = read('std_info.txt')
    ee_avg, cpe_avg, avg = average(lst)
    write('std_info.txt', ee_avg, cpe_avg, avg, lst)


if __name__ == '__main__':
    main()
