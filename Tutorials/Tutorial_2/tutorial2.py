#2) Variables & Assignment
#Create variables for your name, your age, and the value of pi (3.14159). Print them all in one sentence

first_name=input("1st name: ")
age=input("Age: ")
pi=3.14159

print("Hello, my name is",first_name,"! I am",age,"years old. The number pi is around", pi)

print("\n3) Operators Practice")
#Before running these, guess the result. Then check:
n = 7 // 3
m = 7 % 3
l = 2 ** 3

print("7 // 3 =",n,"\n"
      "7 % 3 =",m,"\n"
      "2 ** 3 =",l)

print ("\n4) Full Name Concatenation")
#Ask the user for their first name and last name. Print their full name in a sentence, e.g.:
#Hello, your full name is Alice Smith.

last_name=input("Last name: ")
whole_name=first_name+" "+last_name
print("Hello, your full name is",whole_name)

print("\n5) Gross Pay Calculator")
#Ask the user for hours worked and rate per hour. Multiply and print the result.
hours=input("Hours worked = ")
rate=input("Rate per hour = ")
pay=float(hours)*float(rate)
print ("Pay = ",pay)

print("\n6) Celsius to Fahrenheit")
#Ask for a temperature in Celsius. Convert to Fahrenheit using the formula F = (C × 9/5) + 32.
Celsius=input("Temperature in Celsius = ")
Fahrenheit=(float(Celsius)*9/5)+32
print ("The temp",Celsius,"is",Fahrenheit,"degrees in Fahrenheit.")

print("\n7) Even or Odd?")
#Ask the user for an integer. Use the modulus operator (%) to check if it is even or odd, and print the result.
randmint=input("Type in a random int = ")
if int(randmint)%2==0:
    print (randmint,"is even.")
else: print (randmint,"is odd.")

print("\n8) Challenge – Time Converter")
#Ask the user for a total number of minutes (integer). Use // and % to compute hours and
#leftover minutes. Example: 135 minutes → 2 hour(s) and 15 minute(s).
minutes=input("Minutes = ")
hours = int(minutes)/60
leftOverMinutes=int(minutes)%60
print(minutes,"->",int(hours),"hour(s) &",leftOverMinutes,"minute(s)")
