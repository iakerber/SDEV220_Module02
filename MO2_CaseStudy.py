#Ilze Akerbergs
#M02_CaseStudy.py
#inputs student first and last names and GPA, if GPA 3.5 or greater, notifies on Deans List, if 3.25 or greater, notifies on Honor Roll

LName = input("What is your last name?")
if LName == 'ZZZ':
    exit()
FName = input("What is your first name?")
GPA = input("What is your GPA?")
GPA = float(GPA)
if GPA >= 3.5:
    print("You are on the Dean's List!")
if GPA >= 3.25:
    print("You are on the Honor Roll!")
else:
    print("Try harder!")