# Room reqs
#     - RoomID
#     - BuildingID
#     - available seats
#     - computer (t/f)
#     - projector (t/f)
#     - audio (t/f)
#     - active (t/f)
import random

import building_create

rooms = []


def room_T():
    roomID = ''
    unique = False
    while not unique:
        for i in range(6):
            roomID += str(random.randint(0, 9))
        if roomID not in rooms:
            unique = True
        else:
            roomID = ''
            unique = False

    buildingID = random.choice(building_create.buildings)

    rooms.append((roomID, buildingID))

    seats = str(random.randint(10, 50))

    comp = '0' if random.randint(0, 5) == 3 else '1'

    project = '0' if random.randint(0, 3) == 1 else '1'

    audio = '0' if random.randint(0, 3) == 1 else '1'

    active = '0' if random.randint(0, 15) == 10 else '1'

    return f'INSERT INTO Room_T VALUES(\"{roomID}\",\"{buildingID}\",\"{seats}\",' \
           f'\"{comp}\",\"{project}\",\"{audio}\",\"{active}\");'
