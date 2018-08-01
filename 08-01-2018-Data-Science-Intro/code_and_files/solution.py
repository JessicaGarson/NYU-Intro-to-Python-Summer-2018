abbv = 'AK, AL, AR, AZ, CA, CO, CT, DC, DE, FL, GA, HI, IA, ID, IL, IN, KS, KY, LA, MA, MD, ME, MI, MN, MO, MS, MT, NC, ND, NE, NH, NJ, NM, NV, NY, OH, OK, OR, PA, RI, SC, SD, TN, TX, UT, VA, VT, WA, WI, WV, WY'
print(abbv)
state_abbreviations = abbv.split(',')
print(state_abbreviations)


state_names = 'Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, District of Columbia, Florida, Georgia, Hawaii, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, Wisconsin, Wyoming'
print(state_names)
states = state_names.split(',')
print(states)

def createSelectStateHTML(abbrev, state):
    print('<select>')
    for state_code, state_name in zip(abbrev, state):
        print('\t<option value="{}">{}</option>'.format(state_code, state_name))
    print('</select>')


createSelectStateHTML(abbrev=state_abbreviations, state=states)
