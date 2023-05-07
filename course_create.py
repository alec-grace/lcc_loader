# Need:
#     - Course ID
#     - Department ID
#     - Title
#     - Credit hours
#     - Active status


import departments_create
import random

id_list = []

def course_T():

    courseID = ''
    for i in range(5):
        courseID += str(random.randint(0, 9))
    id_list.append(courseID)

    depts = list(departments_create.majors.keys())
    code = depts[random.randint(0, len(depts) - 1)]

    title = "temporary title"

    cred_hours = str(random.randint(2, 8)) + '.' + str(5 if random.randint(0, 3) == 1 else 0)

    status = '0' if random.randint(0, 10) == 5 else '1'

    return f'INSERT INTO Course_T VALUES(\"{courseID}\",\"{code}\",\"{title}\",\"{cred_hours}\",\"{status}\");'
