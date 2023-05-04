import random
import names
from datetime import date, timedelta
import random_address

"""
creates insert statement for Student_T table
"""

ID_list = []


def student_T():
    statement = "INSERT INTO Student_T VALUES("

    # student id
    stuID = ''
    unique = False
    while not unique:
        for i in range(10):
            stuID += str(random.randint(0, 9))

        if stuID in ID_list:
            stuID = ''
            unique = False
        else:
            ID_list.append(stuID)
            unique = True

    # first name
    fname = names.get_first_name()
    # last name
    lname = names.get_last_name()

    # birthday creation
    begin_range, end_range = date(1980, 1, 1), date(2000, 12, 31)
    date_range = end_range - begin_range
    total_days = date_range.days
    # usable bday
    b_day = begin_range + timedelta(days=random.randint(0, total_days))

    # start year
    start_yr = random.randint(b_day.year, b_day.year + random.randint(18, 22))
    # year of graduation
    yog = random.randint(start_yr, start_yr + random.randint(4, 12))

    # gender
    gender = 'm' if random.randint(0, 1) == 0 else 'f'

    # generate random address
    full_add = random_address.real_random_address()
    # street 1
    str1 = full_add["address1"]
    # street 2
    str2 = full_add["address2"]
    # city
    city = full_add["city"]
    # zip code
    zip_code = full_add["postalCode"]
    # state code
    state = full_add["state"]

    # phone numbers
    phone1 = gen_phone()
    phone2 = gen_phone() if random.randint(0, 5) == 0 else ''

    # e-mails
    email = gen_email(fname, lname)
    email2 = gen_email(fname, lname) if random.randint(0, 3) == 0 else ''

    # country
    country_code = "US"

    return f'{statement}\"{stuID}\",\"{fname}\",\"{lname}\",\"{start_yr}\",\"{yog}\",\"{b_day}\",\"{gender}\",' \
           f'\"{str1}\",\"{str2}\",\"{city}\",\"{zip_code}\",\"{phone1}\",\"{phone2}\",\"{email}\",\"{email2}\",' \
           f'\"{country_code}\",\"{state}\");'


"""
creates insert statement for Faculty_T table
"""


def faculty_T():
    statement = "INSERT INTO Faculty_T VALUES("

    # unique faculty ID
    facID = ''
    unique = False
    while not unique:
        for i in range(10):
            facID += str(random.randint(0, 9))
        if facID in ID_list:
            facID = ''
            unique = False
        else:
            ID_list.append(facID)
            unique = True

    # first name
    fname = names.get_first_name()
    # last name
    lname = names.get_last_name()

    # title
    # ask about these requirements
    titles = ['professor', 'professor', 'professor', 'professsor', 'professor',
              'professor', 'professor', 'adjunct', 'tenured', 'teaching assistant']
    choose = random.randint(0, len(titles) - 1)
    title = titles[choose]

    # phone numbers
    phone1 = gen_phone()
    phone2 = gen_phone() if random.randint(0, 5) == 0 else ''

    # office num
    off_num = str(random.randint(1, 99999))

    # birthday creation
    begin_range, end_range = date(1940, 1, 1), date(1998, 12, 31)
    date_range = end_range - begin_range
    total_days = date_range.days
    # usable bday
    b_day = begin_range + timedelta(days=random.randint(0, total_days))

    # ADD THIS TO ERWIN & DDL
    # gender
    gender = 'm' if random.randint(0, 1) == 0 else 'f'

    # generate random address
    full_add = random_address.real_random_address()
    # street 1
    str1 = full_add["address1"]
    # street 2
    str2 = full_add["address2"]
    # city
    city = full_add["city"]
    # zip code
    zip = full_add["postalCode"]
    # state code
    state = full_add["state"]

    # e-mails
    email = gen_email(fname, lname)
    email2 = gen_email(fname, lname) if random.randint(0, 3) == 0 else ''

    # department id - approximated
    deptID = str(random.randint(100, 199))

    # country
    country_code = "US"

    return f'{statement}\"{facID}\",\"{fname}\",\"{lname}\",\"{title}\",\"{phone1}\",\"{off_num}\",\"{b_day}\",\"{str1}\",' \
           f'\"{str2}\",\"{city}\",\"{zip}\",\"{phone2}\",\"{email}\",\"{email2}\",\"{deptID}\",\"{country_code}\",' \
           f'\"{state}\");'


def gen_email(fname, lname):
    u_name = [fname, lname, random.randint(0, 9), random.randint(0, 9),
              random.randint(0, 9), random.randint(0, 9), random.randint(0, 9),
              random.randint(0, 9)]
    random.shuffle(u_name)
    login = ""
    for i in range(len(u_name) - 1):
        login += str(u_name[i])
    servers = ['@gmail', '@yahoo', '@redmail', '@hotmail', '@bing']
    servpos = random.randint(0, len(servers) - 1)
    email = login + servers[servpos]
    tlds = ['.com', '.net', '.org']
    tldpos = random.randint(0, len(tlds) - 1)
    email = email + tlds[tldpos]
    return email


def gen_phone():
    total = ''
    for i in range(10):
        num = random.randint(0, 9)
        total += str(num)

    return total
