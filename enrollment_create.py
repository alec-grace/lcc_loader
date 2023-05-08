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

def enrollment_T():

    # existing = []
    stuID = random.choice(stu_fac_create.stu_list)

    sectionID = random.choice(section_create.alpha)


