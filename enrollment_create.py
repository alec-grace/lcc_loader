# Enrollment reqs
#     - StuID
#     - SectionID
#     - CourseID
#     - Yr
#     - Term
#     - Midterm
#     - Final
#     - Add_Date
#     - Drop_date
#     - Withdraw_date
import section_create
import stu_fac_create
import random

stu_enrolls = []


def enrollment_T():

    exists = True

    while exists:
        stuID = random.choice(stu_fac_create.stu_list)
        class_info = random.choice(section_create.course_sect_yr)

        this_info = [stuID, class_info[0], class_info[1], class_info[2], class_info[3]]
        if this_info in stu_enrolls:
            exists = True
        else:
            stu_enrolls.append(this_info)
            exists = False

    sectionID = class_info[0]

    courseID = class_info[1]

    year = class_info[2]

    term = class_info[3]

    mid = str(year) + '-01-01'

    final = str(year) + '-12-31'

    add_date = str(year - 1) + '-11-16'

    drop_month = random.randint(2, 10)
    drop_day = random.randint(13, 28)
    drop_date = '\"' + str(year) + f'-{drop_month}-{drop_day}\"' if random.randint(0, 20) == 1 else 'null'

    if drop_date == 'null':
        wdraw = '\"' + str(year) + f'-{drop_month}-{drop_day}\"' if random.randint(0, 20) == 1 else 'null'
    else:
        wdraw = 'null'

    return f'INSERT INTO Enrollment_T (StuID, SectionID, CourseID, Yr, Term, Midterm, ' \
           f'Final, Add_date, Drop_date, Withdraw_date) VALUES(\"{stuID}\",\"{sectionID}\",\"' \
           f'{courseID}\",\"{year}\",\"{term}\",\"{mid}\",\"{final}\",\"{add_date}\",{drop_date},' \
           f'{wdraw});'
