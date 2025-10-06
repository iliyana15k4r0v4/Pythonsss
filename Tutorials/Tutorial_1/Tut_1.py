# IS1110 Tutorial 1 - Exercises
# =============================================================================
# 0. FILE STRUCTURE AND WORKING WITH PYTHON FILES
# =============================================================================
# Create a main folder for your IS1110 work.
# Inside that folder, create a subfolder called Tutorials.
# Inside the Tutorials folder, create a subfolder called Tutorial_1.
# Create a Python file and save it to your Tutorial_1 subfoler in the Tutorials folder.
# Copy the code from this exercise file into your Python file and complete the coding exercises.
# =============================================================================
# 1. HELLO WORLD
# ============================================================================

print("Hello World")

# =============================================================================
# 2. VARIABLES AND SIMPLE MATH
# =============================================================================
# Variables are like labelled boxes that store information

name = "Iliyana"
age = 19
print("Hello, my name is ", name)
print("I am", age, "years old")
print("Next year I will be", age + 1, "years old")

# Inventor exercise
# -----------------
# The following steps give the name and birth year of a famous inventor.
# (a) Declare the variable first_name and assign it the value “Thomas”.
# (b) Declare the variable middle_name and assign it the value “Alva”.
# (c) Declare the variable last_name and assign it the value “Edison”.
# (d) Declare the variable year_of_birth and assign it the value 1847.
# (e) Display the phrase “The year of birth of” followed by the inventor's full name,
# followed by “is”, and the inventor's year of birth.
# Based on: Schneiders, 2016, p. 62

first_name = "Thomas "
middle_name = "Alva "
last_name = "Edison "
year_of_birth = 1847
print("The year of birth of "+first_name+middle_name+last_name+ "is "+ str(year_of_birth))

# =============================================================================
# 3. BASIC CALCULATIONS
# =============================================================================
# Direct calculations with numbers
print(12 + 3) # Addition
print(10 - 2) # Subtraction
print(4 * 5) # Multiplication
print(20 / 4) # Division
# Using variables in calculations
a = 3
b = 4
c = a + b
print("a =", a)
print("b =", b)
print("c = a + b =", c)

d = a * b
print("a * b =", d)
e = b - a
print("b - a =", e)
f = b / a
print("b / a =", f, "\n")

# Create a Distance calculator
# ----------------------------
# Declare variables for speed (in km/h) and time elapsed (in hours)
# Assign values to these variables (e.g., 50 for speed and 14 for time elapsed)
# Calculate the distance travelled (distance = speed x time elapsed)
# Print the distance
# Based on: Schneiders, 2016, p. 41

speed = 50
time_elapsed= 14
distance = speed * time_elapsed
print("distance =" ,distance , "\n")

# =============================================================================
# 4. USER INPUT
# =============================================================================
# Basic interactive input
name = input("What is your name? ")
age = input("How old are you? ")
print("Hello", name, "you are", age, "years old!")
# Check the type of each variable
print(type(name))
print(type(age))
# What do you notice?
# Converting input to numbers for maths
age = int(input("How old are you? "))
print("In 10 years you will be", age + 10, "years old!", "\n")

# Distance from a Storm Calculator
# --------------------------------
# If n is the number of seconds between lightning and thunder,
# the storm is n/5 miles away. Write a program that requests the number
# of seconds between lightning and thunder and reports the distance from the storm
# rounded to two decimal places.
# Sample output:
# Enter number of seconds between lightning and thunder: 1.25
# Enter your age: 20
# Enter your resting heart rate: 70
# Distance from storm: 0.25 miles
# Based on: Schneiders, 2016, p. 62

seconds = input("Enter number of seconds between lightning and thunder: ")
distance_from_storm = float(seconds)/5
print("Distance from storm:",distance_from_storm,"miles")
