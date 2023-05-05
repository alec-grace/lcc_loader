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
    depts = departments_create.department_T()
    students = []
    faculty = []

    with open(outfile, 'w') as o_file:
        # -----
        # Create departments
        # -----
        o_file.write('\n/* Department inserts */\n\n')
        for row in depts:
            o_file.write(row + "\n")
        o_file.write('\n/* Student inserts */\n\n')
        # -----
        # Create students
        # -----
        for i in range(4):
            stu = stu_fac_create.student_T()
            students.append(stu)
            o_file.write(stu + '\n')
        o_file.write('\n/* Faculty inserts */\n\n')
        for i in range(4):
            fac = stu_fac_create.faculty_T()
            faculty.append(fac)
            o_file.write(fac + '\n')
    o_file.close()


if __name__ == "__main__":
    main()
