# Calendar reqs
#     - Year
#     - Term
#     - Midterm date
#     - Final date


def calendar_T():

    all_statements = ''
    term_list = ['FA', 'WI', 'SP', 'SU']

    for year in range(2000, 2031):
        for term in term_list:
            midterm = str(year) + '-01-01'
            final = str(year) + '-12-31'
            all_statements += f'INSERT INTO Calendar_T VALUES(\"{year}\",' \
                              f'\"{term}\",\"{midterm}\",\"{final}\");\n'

    return all_statements
