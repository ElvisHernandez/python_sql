import sys
from cs50 import SQL

import sys
import csv
from cs50 import SQL

def main():
    if len(sys.argv) != 2:
        print ('Incorrect number of command line arguments')
        return 1

    db = SQL("sqlite:///students.db")
    try:
        with open(sys.argv[1]) as csv_file:
            students = csv.DictReader(csv_file)

            for row in students:
                student_names = row['name'].split()
                if len(student_names) == 3:
                    middle = student_names[1]
                else:
                    middle = None
                first = student_names[0]
                last = student_names[-1]

                sql_insert = '''INSERT INTO students (first,middle,last,house,birth)
                                VALUES (?, ?, ?, ?, ?)'''
                db.execute(sql_insert, first,middle,last,row['house'],row['birth'])
        return 0

    except FileNotFoundError:
        print ('The command line argument provided is not a valid file name in the current directory')

if main() == 0:
    print ('Database has been successfully updated')
else:
    print ('There was an error updating the database')