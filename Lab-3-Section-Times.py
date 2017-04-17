# Dan Ryan
# Lab 3: Section
# Challenge
# This script converts heights between imperial and metric units.-
# gather information from the user
# * enhance the output portion of the script
#  X * Concatenate stuff: MATH 098-04
#   * return errors like ERROR: Unrecognized section number.
# X * determine the meeting time for the class, based on the table shown above
# X * Make sure that the department code is all upper case. If it isn't, issue a warning message and convert it to upper case before you echo the value to the user.
# * Make sure that the course number is 3 characters long and is numeric. If it isn't, print out the regular output message and a warning message.
# * If the section number is unrecognized, don't print out the warning message(s), just print the error message.

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
    if not dept.isupper():
        print("WARNING: department code is not upper-case.")
        if not len(course) == 3 and course.isdigit():
            print("WARNING: course number is not 3-digits.")
    try:
        int(course)
        course = course.zfill(3)

    except ValueError:
        print("WARNING: course number is not numeric.")


except ValueError:
    print("ERROR: Unrecognized section number.")
    meeting_time = 'unknown'
    sys.exit(0)


# output the information to the user
print("Your course {} {}-{} meets {}".format(dept.upper(), course, section, meeting_time))
