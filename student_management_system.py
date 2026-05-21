print("=========Result========")

Stud_name = input("Student name: ")
Math_mark = float(input("Math: "))
Eng_mark = float(input("Enlish: "))
Sci_mark = float(input("Science: "))

Total_Mark = Math_mark + Eng_mark + Sci_mark
print(f"Total: {Total_Mark} ")
Avg_mark = Total_Mark / 3
print(f"Average: {Avg_mark: .2f} ")

if Avg_mark >= 101:
  print("Invalid Grade")

elif Avg_mark >= 80:
  print("Grade: A")
  print("Status: Pass")
  print("Excelent Work!")

elif Avg_mark >= 70:
  print("Grade: B")
  print("Status: Pass")
  print("Good Job!")

elif Avg_mark >= 60:
  print("Grade: C")
  print("Status: Pass")
  print("Keep Improving!")

else:
  print("Grade: F")
  print("Status: Fail")
  print("Good Job!")

print("=======================")