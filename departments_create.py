"""
dictionary for majors, minors, and departments to pull from
"""
import random

majors = {
    'CS': 'Computer Science',
    'BU': 'Business',
    'DA': 'Data Analytics',
    'TH': 'Theology',
    'PH': 'Physics',
    'PS': 'Psychology',
    'MA': 'Math',
    'EN': 'English',
    'PL': 'Politics',
    'CJ': 'Criminal Justice',
    'EE': 'Electrical Engineering',
    'CC': 'Cyber Criminology',
    'HI': 'History'
}

def department_T():
    departments = []

    for key in majors:
        name = majors[key]
        status = "0" if random.randint(0, 5) == 3 else "1"
        departments.append(f"INSERT INTO Department_T VALUES(\"{key}\","
                           f"\"{name}\",\"{status}\");")

    return departments


def major_T():

    major_list = []

    for key in majors:
        code = key
        desc = majors[key]
        active = '0' if random.randint(0, 10) == 5 else '1'
        deptId = key
        major_list.append(f'INSERT INTO Major_T (Major_code, Descriptn, Active_, DepartmentID) '
                          f'VALUES(\"{code}\",\"{desc}\",\"{active}\",\"{deptId}\");')

    return major_list


def minor_T():

    minor_list = []

    for key in majors:
        code = key
        desc = majors[key]
        active = '0' if random.randint(0, 10) == 5 else '1'
        deptId = key
        minor_list.append(f'INSERT INTO Minor_T (Minor_code, Descriptn, Active_, DepartmentID) '
                          f'VALUES(\"{code}\",\"{desc}\",\"{active}\",\"{deptId}\");')

    return minor_list
