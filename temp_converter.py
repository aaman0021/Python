print("Temperature Converter")
print("1. F: Celsius to Fahrenheit")
print("2. C: Fahrenheit to Celsius")

Select = input("select an option (1 or 2): ")

if Select == "1":
  Temperature = float(input("Enter Temperature"))
  F = (Temperature * 9/5) + 32
  print(f"Your temperature in Celcius converted to Fahrenheit  {F} F")

elif Select == "2":
  Temperature = float(input("Enter Temperature"))
  C = (Temperature - 32) * 5/9
  print(f"Your temperature in Fahrenheit converted to Celsius  {C} C")

else: 
  print("Invalid Input")





