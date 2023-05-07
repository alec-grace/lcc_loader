# Driver class for generating data for Local Community College project
import randominfo
import course_create
import section_create
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
    courses = []

    with open(outfile, 'w') as o_file:
        # -----
        # Create departments
        # -----
        o_file.write('\n/* Department inserts */\n\n')
        for row in depts:
            o_file.write(row + "\n")

        # -----
        # Create courses
        # -----
        o_file.write('\n/* Course inserts */\n\n')
        for i in range(15):
            course = course_create.course_T()
            courses.append(course)
            o_file.write(course + "\n")

        # -----
        # Create students
        # -----
        o_file.write('\n/* Student inserts */\n\n')
        for i in range(4):
            stu = stu_fac_create.student_T()
            students.append(stu)
            o_file.write(stu + '\n')

        # -----
        # Create faculty
        # -----
        o_file.write('\n/* Faculty inserts */\n\n')
        for i in range(4):
            fac = stu_fac_create.faculty_T()
            faculty.append(fac)
            o_file.write(fac + '\n')

        # -----
        # Create sections
        # -----
        o_file.write('\n/* Section inserts */\n\n')
        for i in range(30):
            o_file.write(section_create.section_T() + '\n')

    o_file.close()


if __name__ == "__main__":
    main()
