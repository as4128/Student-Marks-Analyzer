print("===== Student Marks Analyzer =====")
name = input("Enter student name: ")
marks = []
for i in range(5):
    mark = float(input(f"Enter marks for Subject {i + 1}: "))
    marks.append(mark)
total = sum(marks)
average = total / 5
highest = max(marks)
lowest = min(marks)
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"
print("\n===== Student Result =====")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Grade:", grade)