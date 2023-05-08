# building info:
#     - buildingID
#     - name
#     - active status

import random
import names

buildings = []


def building_T():

    buildingID = ''
    unique = False
    while not unique:
        for i in range(4):
            buildingID += str(random.randint(0, 9))
        if buildingID in buildings:
            unique = False
            buildingID = ''
        else:
            buildings.append(buildingID)
            unique = True

    name = names.get_last_name() + " Hall"

    active = 0 if random.randint(0, 10) == 5 else 1

    return f'INSERT INTO Building_T VALUES(\"{buildingID}\",\"{name}\",\"{active}\");'

