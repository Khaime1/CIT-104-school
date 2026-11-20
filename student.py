"""
CIT-104 Assignment Chapter 10
Khem Kafley
11/20/2026

This program returns the result of the comparison of the two students names and also shuffles it.
"""

class Student: # makes class for students for their name and id number.
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self): # returns a string representation of the student.
        return "Name: " + self.name + ", ID: " + str(self.number)


    def __eq__(self, other): # checks if two students have the same name.
        return self.name == other.name
    def __eq__(self, other): # checks if two students have the same number.
        return self.number == other.number

 
    def __lt__(self, other): # checks if one student's name is less than another's.
        return self.name < other.name
    def __lt__(self, other): # checks if one student's number is less than another's.
        return self.number < other.number

    def __ge__(self, other): # checks if one student's name is greater than or equal to another's.
        return self.name >= other.name
    def __ge__(self, other): # checks if one student's number is greater than or equal to another's.
        return self.number >= other.number
    
def main():
    student1 = Student("Khem Kafley", 1) # the name and id number of student 1.
    student2 = Student("John Python", 2) # the name and id number of student 2.

    print("Student 1:", student1) # prints the students details.
    print("Student 2:", student2) 

    print("\nComparison Results:") # prints the comparison results between the two students.

    print("Student 1 == Student 2:", student1 == student2) # prints if the results is true or false for ==, <, and >=.
    print("Student 1 < Student 2:", student1 < student2)
    print("Student 2 >= Student 1:", student2 >= student1)


if __name__ == "__main__": # checks if the script is being run.
    main()


import random

def main():
    # create a list of student objects.
    students = [
        Student("David Computer", 1),
        Student("John Johnson", 2),
        Student("Michael Jackson", 3),
        Student("Sarah Python", 4),
        Student("Khem Kafley", 5)
    ]

    # shuffles the list.
    random.shuffle(students)

    print("Students after shuffling:")
    for student in students: # prints the shuffled list.
        print(student)

    # sorts the list.
    students.sort()
    
    print("\nStudents after sorting:")
    for student in students: # prints the sorted list.
        print(student)


if __name__ == "__main__": 
    main()