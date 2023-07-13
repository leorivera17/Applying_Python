# Lab 8
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 3

# purpose -
def picture(fout) -> tuple:
    file = open(fout)
    lst = []
    header = ''
    for i in range(3):
        head = file.readline()
        header += head
    for line in file:
        lst.append(line)
    file.close()
    return header, lst


# purpose -
def hidden(header, lst):
    fout = open('discovered.ppm', 'w')
    fout.write((header))
    cnt = 0
    red = 0
    for item in lst:
        if cnt < 2:
            if cnt == 0:
                red = int(item) * 10
                if red > 255:
                    red = 255
            cnt += 1
        else:
            fout.write(str(red) + '\n' + str(red) + '\n' + str(red) + '\n')
            cnt = 0
    fout.close()


def main():
    header, lst = picture('hidden.ppm')
    hidden(header, lst)


if __name__ == '__main__':
    main()
