username = "Russell"
password = "000000"

name = input("Enter your username: ")
passcode =  input("Enter your passcode: ")

if name == username and passcode == password:
  print("Login sucessful!")
  print(f"Welcome, {username}!")

elif name != username  and passcode != password:
  print("Both username and password are incorrect.")

elif name == "" and passcode == "":
  print("Please enter your username/password. ")

elif name != username:
  print("Incorrect username. ")

else:
  print("Incorrect password")