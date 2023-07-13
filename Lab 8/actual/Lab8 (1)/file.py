# Lab 8
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 3

# purpose - to write in a new file and add a few words
def read(fout)-> None:
    file = open(fout, 'r')
    count = 0
    for word in file:
        word = word[slice(len(word) - 1)]
        count += 1
        print('Line ' + str(count) + ' (' + str(len(word)) + ' chars): ' + word)


def main():
    read('in.txt')


if __name__ == '__main__':
    main()
