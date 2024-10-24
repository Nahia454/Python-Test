# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F

if 90<=percent<=100:
    "A"
elif 80<=percent<=89:
    "B"
elif 70<=percent<=79:
    "C"
elif 60<=percent<=69:
    "D"
elif 40<=percent<=49:
    "E"
elif 0<=percent<=40:
    "F"
else:
    "invalid percentage" 
student_name=(input("Enter student_name"))
percent=65
grade=percent
print(f"student_name:{Annet}")
print(f"percentage:{percent}%")
print(f"grade:{grade}")