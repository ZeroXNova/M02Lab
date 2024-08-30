#Dean's List/Honor Roll Checker
#James Klick
#8/30/2024
#This program will take a students name and GPA, checking if it meets the qualifiers for Honor Roll/Dean's List

print("Enter last name as 'ZZZ' to exit")
lname = str(input("Enter Student's Last Name: "))

while lname != "ZZZ":
    fname = str(input("Enter Student's First Name: "))
    gpa = float(input("Enter Student's GPA : "))
    if gpa > 4.0:
        print("That GPA is too high to be possible, try again!")
    elif gpa >= 3.5:
        print(fname + " " + lname + " " + "has made the Dean's List!")
    elif gpa >= 3.25:
        print(fname + " " + lname + " " + "has made the Honor Roll!")
    else:
        print("GPA is too low for Honor Roll or Dean's List")
    print("Enter last name as 'ZZZ' to exit")
    lname = str(input("Enter Student's Last Name: "))


