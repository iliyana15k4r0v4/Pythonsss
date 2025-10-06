print("Registration form \n")

first_name=input("First name: ")
last_name=input("Last name: ")
birth=input("Birth year: ")

print("Welcome "+first_name,last_name, "!")
print("Your registration is complete.")
print("Your temporary password is: "+first_name+"*"+str(birth))
