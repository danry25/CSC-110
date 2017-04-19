# Dan Ryan
# Lab 3: Section
# Plus
# This script parses class info and returns your class info & time.

import sys

timetable = {"01": "8:00 - 8:50 am, Daily",
             "02": "9:00 - 9:50 am, Daily",
             "03": "10:00 - 10:50 am, Daily",
             "04": "11:00 - 11:50 am, Daily",
             "05": "12:00 - 1:05 pm, MTWTh",
             "06": "1:15 - 2:20 pm, MTWTh",
             "08": "6:00 - 8:20 pm, MW",
             "09": "6:00 - 8:20 pm, TTh"}

dept = input('Enter the department code: ')
course = input('Enter the course number: ')
section = input('Enter the section number: ')

try:
    int(section)
    # determine when the class meets
    meeting_time = timetable[section]
    if dept.isupper():
        pass
    else:
        print("WARNING: department code is not upper-case.")

    if len(course) == 3 and course.isdigit():
        pass
    else:
        print("WARNING: course number is not 3-digits.")

except (KeyError, ValueError):
    print("ERROR: Unrecognized section number.")
    meeting_time = 'unknown'
    sys.exit(0)

try:
    int(course)
    # course = course.zfill(3)  # Commented out cause input cleanup is overkill per professor

except ValueError:
    print("WARNING: course number is not numeric.")

# output the information to the user
print("Your course {} {}-{} meets {}".format(dept.upper(), course, section, meeting_time))
