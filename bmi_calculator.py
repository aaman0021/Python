Weight = float(input("Enter your weight in kg: "))
Height = float(input("Enter your height in m: "))
BMI = Weight / (Height*Height)
print(f"Your BMI is {BMI} ")

if BMI < 18.5:
  print("Underweight")

elif 18.5 <= BMI < 24.9:
  print("Normalweight")

elif 25 <= BMI < 29.9:
 print("Overwight")

else:
  print("Obese")


