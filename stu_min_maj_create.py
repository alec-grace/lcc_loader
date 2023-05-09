# Stu_min reqs:
#     - StuID
#     - minor code
#     - facID
#
# stu_maj reqs:
#     - StuID
#     - major code
#     - facID

import random
import departments_create
import stu_fac_create

stu_mins = []
stu_majs = []


def stu_min_T():

    exists = True

    while exists:

        stuID = random.choice(stu_fac_create.stu_list)
        min_code = random.choice(list(departments_create.majors.keys()))
        combo = [stuID, min_code]
        count = 0
        if combo in stu_mins:
            for thing in stu_mins:
                if combo[0] == thing[0]:
                    count += 1

            if count >= 2:
                exists = True
            else:
                stu_mins.append(combo)
                exists = True
        else:
            stu_mins.append(combo)
            exists = False

    facID = random.choice(stu_fac_create.fac_list)

    return f'INSERT INTO Stu_min_T (StuID, Minor_code, FacID) VALUES(\"{stuID}\",\"{min_code}\",\"{facID}\");'


def stu_maj_T():

    exists = True

    while exists:

        stuID = random.choice(stu_fac_create.stu_list)
        maj_code = random.choice(list(departments_create.majors.keys()))
        combo = [stuID, maj_code]
        count = 0
        if combo in stu_majs:
            for thing in stu_majs:
                if combo[0] == thing[0]:
                    count += 1

            if count >= 2:
                exists = True
            else:
                stu_majs.append(combo)
                exists = True
        else:
            stu_majs.append(combo)
            exists = False

    facID = random.choice(stu_fac_create.fac_list)

    return f'INSERT INTO Stu_maj_T (StuID, Major_code, FacID) VALUES(\"{stuID}\",\"{maj_code}\",\"{facID}\");'
