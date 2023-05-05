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

