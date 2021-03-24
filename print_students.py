
# Program will run students information when pulled 

from define_student import Student 

student1 = Student("Jim", "Business" ,3.1, False)
student2 = Student("Pam", "Art", 2.5, True)
student3 = Student("Randy", "CS", 3.8, False)
student4 = Student("Melissa", "Music", 4.1, False)
print(f"{student1.name} is a {student1.major} major with a {student1.gpa} GPA.")
print(f"{student2.name} is a {student2.major} major with a {student2.gpa} GPA.")
print(f"{student3.name} is a {student3.major} major with a {student3.gpa} GPA.")
print(f"{student4.name} is a {student4.major} major with a {student4.gpa} GPA.")