# Project 4 – Graduate Rate (2017-2018)
# Name: Leo Rivera
# Instructor: Dr. S. Einakian
# Section: 3
# classes and functionalities will be provided here

# class Division
class Division:
    def __init__(self, ids, name):
        self.id = ids
        self.division_name = name


# class Graduate:
class Graduate:
    def __init__(self, ids, majors, bachelors, masters, doctors):
        self.id = ids
        self.major = majors
        self.bach = bachelors
        self.master = masters
        self.doc = doctors

    def __eq__(self, other):
        return type(self) == type(other) and \
               self.bach == other.bach and \
               self.master == other.master and \
               self.doc == other.doc

    def __repr__(self):
        return '(' + str(self.id) + ', ' + str(self.major) + ', ' + str(self.bach) \
               + ', ' + str(self.master) + ', ' + str(self.doc) + ')'

    # read file and return list of strings


def read_file(book):
    fout = open(book, 'r')
    header = []
    for i in range(3):
        header1 = fout.readline()
        header.append(header1)
    lst = []
    for line in fout:
        line = line.split(',')
        lst.append(line)
    fout.close()
    return header, lst


# create list of Division objects
def create_division(lst):
    div_lst_obj = []
    for relate_line in lst:
        if relate_line[0][2] == '0' and relate_line[0][3] == '0':
            obj_div = Division(relate_line[0], relate_line[1])
            # print(obj_div)
            div_lst_obj.append(obj_div)
    # print(div_lst_obj)
    return div_lst_obj


# create list of Graduate objects
def create_graduate(lst):
    grad_lst_obj = []
    for objects in lst:
        if objects[0][2] != '0' or objects[0][3] != '0':
            obj_grad = Graduate(objects[0], objects[1], (int(objects[2]), int(objects[3])),
                                (int(objects[4]), int(objects[5])), (int(objects[6]), int(objects[7])))
            grad_lst_obj.append(obj_grad)
    # print(grad_lst_obj)
    return grad_lst_obj


def create_files(grad_lst_obj):
    file1 = open('agriculture.csv', 'w')
    file2 = open('computer.csv', 'w')
    file3 = open('education.csv', 'w')
    file4 = open('engineering.csv', 'w')
    file1.write('ID Major Bachelor Master Doctor\n')
    file2.write('ID Major Bachelor Master Doctor\n')
    file3.write('ID Major Bachelor Master Doctor\n')
    file4.write('ID Major Bachelor Master Doctor\n')
    for i in grad_lst_obj:
        if i.id[1] == '2':
            file1.write(str(i) + '\n')
        if i.id[1] == '4':
            file2.write(str(i) + '\n')
        if i.id[1] == '6':
            file3.write(str(i) + '\n')
        if i.id[1] == '8':
            file4.write(str(i) + '\n')
    file1.close()
    file2.close()
    file3.close()
    file4.close()


# find total and average graduate for all divisions
def find_total_avg(div_lst_obj, grad_lst_obj):
    lst_avg_tot = []
    for divs in div_lst_obj:
        total = count = 0
        for majors in grad_lst_obj:
            if divs.id[:2] == majors.id[:2]:
                # print(majors.bach)
                total = majors.bach[0] + majors.bach[1] + majors.master[0] + \
                        majors.master[1] + majors.doc[0] + majors.doc[1]
                count += 1
        lst_avg_tot.append((total, round(total / count, 2)))
    # print(lst_avg_tot)
    return lst_avg_tot


# find (female, male) graduate rate for given major
def find_graduate_rate(grad_lst_obj, major):
    for this in grad_lst_obj:
        if major == this.major:
            males = int(this.bach[0]) + int(this.master[0]) + int(this.doc[0])
            females = int(this.bach[1]) + int(this.master[1]) + int(this.doc[1])
            # print('Males: ', males)
            # print('Females: ', females)
            return males, females









def total_of_computer(grad_lst_obj):
    for thing in grad_lst_obj:
        if thing.id[1] == '4':
            totally = int(thing.bach[0]) + int(thing.master[0]) + int(thing.doc[0]) + \
                      int(thing.bach[1]) + int(thing.master[1]) + int(thing.doc[1])
            return totally
# print('Total of Processed Graduate in Computer and information sciences and support: ')
# print('Average of Processed Female and Male in Computer and information sciences and support: ')
# print('Compare total graduate rate of Computer and information sciences and support to all other Majors: ')


def science(grad_lst_obj):
    count = 0
    for think in grad_lst_obj:
        count += 1
        if think.id[1] == '4':
            male = int(think[2][0]) + int(think[3][0]) + int(think[4][0])
            female = int(think[2][1]) + int(think[3][1]) + int(think[4][1])
            avg_f = female / count
            avg_m = male / count
            return avg_f, avg_m
        # if thing.major: all = (int(thing.bach[0]) + int(thing.master[0]) + int(thing.doc[0]) + int(thing.bach[1]) +
        # int(thing.master[1]) + int(thing.doc[1])) print('Total of all Females and Males Graduate in all Majors: ',
        # all)


def in_all(grad_lst_obj):
    for everyone in grad_lst_obj:
        male = int(everyone.bach[0]) + int(everyone.master[0]) + int(everyone.doc[0])
        female = int(everyone.bach[1]) + int(everyone.master[1]) + int(everyone.doc[1])
        return male, female
