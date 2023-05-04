# Driver class for generating data for Local Community College project
import randominfo

import stu_fac_create
import names
import random
from random_address import real_random_address
from datetime import date, timedelta


def main():

    outfile = "py_generated_ddl.txt"
    with open(outfile, 'w') as o_file:
        for i in range(50):
            o_file.write(stu_fac_create.student_T() + '\n')
        for i in range(50):
            o_file.write(stu_fac_create.faculty_T() + '\n')
    o_file.close()


if __name__ == "__main__":
    main()
