import sys
from cs50 import SQL

def main():

    if len(sys.argv) != 2:
        print ('Incorrect number of command line arguments')
        return 1

    db = SQL("sqlite:///students.db")

    sql_query = '''SELECT * FROM students
                   WHERE house = ?
                   ORDER BY last, first;'''
    students = db.execute(sql_query,sys.argv[1])

    if len(students) == 0:
        print ('No house by that name')
        return 1

    for student in students:
        first = student['first']
        middle = "" if student['middle'] == None else student['middle']
        last = student['last']
        birth_year = student['birth']
        print (f"{first} {middle} {last}, born {birth_year}")
    return 0

if main() == 0:
    print ('Your query was successful')
else:
    print ('Your query was unsuccessful')