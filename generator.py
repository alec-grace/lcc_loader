# Driver class for generating data for Local Community College project
import randominfo

import stu_fac_create
import departments_create
import names
import random
from random_address import real_random_address
from datetime import date, timedelta


def main():

    outfile = "py_generated_ddl.txt"
    with open(outfile, 'w') as o_file:
        # o_file.write('/* Student inserts */\n\n')
        # for i in range(4):
        #     o_file.write(stu_fac_create.student_T() + '\n')
        # o_file.write('\n/* Faculty inserts */\n\n')
        # for i in range(4):
        #     o_file.write(stu_fac_create.faculty_T() + '\n')
        o_file.write('\n/* Department inserts */\n\n')
        depts = departments_create.department_T()
        for row in depts:
            o_file.write(row + "\n")
    o_file.close()


if __name__ == "__main__":
    main()
