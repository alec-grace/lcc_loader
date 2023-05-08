# Section_T has
#     - SectionID (char1)
#     - CourseID (varchar5)
#     - Year (Int)
#     - Term (char2)
#     - FacID (10)
#     - RoomID (10)
#     - Start-time (8)
#     - End-time (8)
#     - max-enroll (int)
#     - buildingID (5)
#     - Days (7)


import course_create
import stu_fac_create
import building_create
import room_create
import random

course_sections = []

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def section_T():



    exists = False

    while not exists:
        sectionID = random.choice(alpha)
        courseID = random.choice(course_create.id_list)
        unique = str(courseID) + ',' + sectionID
        if unique not in course_sections:
            course_sections.append(unique)
            exists = True
        else:
            exists = False

    year = random.randint(2000, 2030)

    term_list = ['FA', 'WI', 'SP', 'SU']
    term = random.choice(term_list)

    facID = random.choice(stu_fac_create.fac_list)

    room_building = random.choice(room_create.rooms)
    roomID = room_building[0]

    start_times = []
    for i in range(8, 12):
        start_times.append(f'{i}:00 AM')
    start = random.choice(start_times)

    end = start.rstrip('00 AM') + '50 AM'

    max_enroll = random.randrange(10, 51, 5)

    buildingID = room_building[1]

    day_choices = ['MWF', 'TR', 'MW', 'TRS', 'WFS', 'MWS', 'MTWRF', 'S', 'MWR', 'MTR']
    days = random.choice(day_choices)

    return f'INSERT INTO Section_T VALUES(\"{sectionID}\",\"{courseID}\",\"{year}\",\"{term}\",' \
           f'\"{facID}\",\"{roomID}\",\"{start}\",\"{end}\",\"{max_enroll}\",\"{buildingID}\",' \
           f'\"{days}\");'
