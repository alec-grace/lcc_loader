# Driver class for generating data for Local Community College project
import randominfo

import building_create
import calendar_create
import course_create
import enrollment_create
import room_create
import section_create
import stu_fac_create
import departments_create

# tables left:
#     - Stu_maj_T
#     - Stu_min_T
import stu_min_maj_create


def main():

    outfile = "py_generated_inserts.sql"
    depts = departments_create.department_T()
    students = []
    faculty = []
    courses = []

    with open(outfile, 'w') as o_file:
        # Write the stuff not generated here so the whole file is generated
        o_file.write('/* To view the code used for the creation of \n'
                     'data please see: https://github.com/alec-grace/lcc_loader */\n\n'
                     'use agrace072; \n\n'
                     '/* Country inserts */\n\n'
                     'INSERT INTO agrace072.Country_T SELECT * FROM aalbina.country_tbl;\n\n'
                     '/* State inserts */\n\n'
                     'INSERT INTO agrace072.State_T SELECT * FROM aalbina.st_tbl;\n')

        # -----
        # Create departments
        # -----
        o_file.write('\n/* Department inserts */\n\n')
        for row in depts:
            o_file.write(row + "\n")

        # -----
        # Create calendar
        # -----
        o_file.write('\n/* Calendar inserts */\n\n')
        o_file.write(calendar_create.calendar_T() + '\n')

        # -----
        # Create buildings
        # -----
        o_file.write('\n/* Building inserts */\n\n')
        for i in range(10):
            o_file.write(building_create.building_T() + "\n")

        # -----
        # Create rooms
        # -----
        o_file.write('\n/* Room inserts */\n\n')
        for i in range(100):
            o_file.write(room_create.room_T() + "\n")

        # -----
        # Create courses
        # -----
        o_file.write('\n/* Course inserts */\n\n')
        for i in range(30):
            course = course_create.course_T()
            courses.append(course)
            o_file.write(course + "\n")

        # -----
        # Create students
        # -----
        o_file.write('\n/* Student inserts */\n\n')
        for i in range(50):
            stu = stu_fac_create.student_T()
            students.append(stu)
            o_file.write(stu + '\n')

        # -----
        # Create faculty
        # -----
        o_file.write('\n/* Faculty inserts */\n\n')
        for i in range(50):
            fac = stu_fac_create.faculty_T()
            faculty.append(fac)
            o_file.write(fac + '\n')

        # -----
        # Create sections
        # -----
        o_file.write('\n/* Section inserts */\n\n')
        for i in range(30):
            o_file.write(section_create.section_T() + '\n')

        # -----
        # Create enrollments
        # -----
        o_file.write('\n/* Enrollment inserts */\n\n')
        for i in range(100):
            o_file.write(enrollment_create.enrollment_T() + '\n')

        # -----
        # Create majors and minors
        # -----
        o_file.write('\n/* Major inserts */\n\n')
        for statement in departments_create.major_T():
            o_file.write(statement + '\n')

        o_file.write('\n/* Minor inserts */\n\n')
        for statement in departments_create.minor_T():
            o_file.write(statement + '\n')

        # -----
        # Create student majors
        # -----
        o_file.write('\n/* Student minor inserts */\n\n')
        for i in range(100):
            o_file.write(stu_min_maj_create.stu_min_T() + '\n')

        # -----
        # Create student majors
        # -----
        o_file.write('\n/* Student major inserts */\n\n')
        for i in range(100):
            o_file.write(stu_min_maj_create.stu_maj_T() + '\n')

    o_file.close()


if __name__ == "__main__":
    main()
