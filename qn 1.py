score = int(input("enter the student's score(between 0 and 100):"))
if 90 <= score <= 100:
    grade = "A"
elif 80<= score<= 89:
    grade = "B"
elif 70<= score<= 79:
    grade = "C"
elif 60<= score<= 69:
    grade = "D"
else:
    grade = "F"
    print(f"the student's grade is: {grade}")
