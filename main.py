# Author: Woosung Lim wml5207@psu.edu
grade1 = input("Enter your course 1 letter grade: ")
credit1 = input("Enter your course 1 credit: ")
credit1 = float(credit1)
if grade1 == "A":
  gpa1 = 4.0
  print("Grade point for course 1 is: 4.0")
elif grade1 == "A-":
  gpa1 = 3.67
  print("Grade point for course 1 is: 3.67")
elif grade1 == "B+":
  gpa1 = 3.33
  print("Grade point for course 1 is: 3.33")
elif grade1 == "B":
  gpa1 = 3.0 
  print("Grade point for course 1 is: 3.0")
elif grade1 == "B-":
  gpa1 = 2.67
  print("Grade point for course 1 is: 2.67")
elif grade1 == "C+":
  gpa1 = 2.33
  print("Grade point for course 1 is: 2.33")
elif grade1 == "C":
  gpa1 = 2.0
  print("Grade point for course 1 is: 2.0")
elif grade1 == "D":
  gpa1 = 1.0
  print("Grade point for course 1 is: 1.0")
else:
  gpa1 = 0.0
  print("Grade point for course 1 is: 0.0")

grade2 = input("Enter your course 2 letter grade: ")
credit2 = input("Enter your course 2 credit: ")
credit2 = float(credit2)
if grade2 == "A":
  gpa2 = 4.0
  print("Grade point for course 2 is: 4.0")
elif grade2 == "A-":
  gpa2 = 3.67
  print("Grade point for course 2 is: 3.67")
elif grade2 == "B+":
  gpa2 = 3.33
  print("Grade point for course 2 is: 3.33")
elif grade2 == "B":
  gpa2 = 3.0 
  print("Grade point for course 2 is: 3.0")
elif grade2 == "B-":
  gpa2 = 2.67
  print("Grade point for course 2 is: 2.67")
elif grade2 == "C+":
  gpa2 = 2.33
  print("Grade point for course 2 is: 2.33")
elif grade2 == "C":
  gpa2 = 2.0
  print("Grade point for course 2 is: 2.0")
elif grade2 == "D":
  gpa2 = 1.0
  print("Grade point for course 2 is: 1.0")
else:
  gpa2 = 0.0
  print("Grade point for course 2 is: 0.0")\

grade3 = input("Enter your course 3 letter grade: ")
credit3 = input("Enter your course 3 credit: ")
credit3 = float(credit3)
if grade3 == "A":
  gpa3 = 4.0
  print("Grade point for course 3 is: 4.0")
elif grade3 == "A-":
  gpa3 = 3.67
  print("Grade point for course 3 is: 3.67")
elif grade3 == "B+":
  gpa3 = 3.33
  print("Grade point for course 3 is: 3.33")
elif grade3 == "B":
  gpa3 = 3.0 
  print("Grade point for course 3 is: 3.0")
elif grade3 == "B-":
  gpa3 = 2.67
  print("Grade point for course 3 is: 2.67")
elif grade3 == "C+":
  gpa3 = 2.33
  print("Grade point for course 3 is: 2.33")
elif grade3 == "C":
  gpa3 = 2.0
  print("Grade point for course 3 is: 2.0")
elif grade3 == "D":
  gpa3 = 1.0
  print("Grade point for course 3 is: 1.0")
else:
  gpa3 = 0.0
  print("Grade point for course 3 is: 0.0")
credit1 = float(credit1)
credit2 = float(credit2)
credit3 = float(credit3)
GPA = ((gpa1 * credit1) + (gpa2 * credit2) + (gpa3 * credit3))/(credit1 + credit2 + credit3)
print("Your GPA is: " + str(GPA))