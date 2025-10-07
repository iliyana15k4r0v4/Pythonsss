#1) Receipt: subtotal, tax, and total
#A shop applies a sales tax to a purchase. Ask for the subtotal and the tax rate as a
#percentage (e.g., enter 23 for 23%). Compute the tax amount and the grand total.
# Print in the following format: Subtotal: €X.XX | Tax (XX%): €X.XX | Total: €X.XX
from zoneinfo import available_timezones

from HomeWork.chapter2 import height

print ("1)")
subtotal=input("Enter subtotal:")
tax=input("Enter tax:")
taxCalc=int(subtotal)*int(tax)/100
total=int(subtotal)+taxCalc
print("Subtotal: €"+str(subtotal)+" | Tax ("+str(tax)+"%): €"+str(taxCalc)+" | Total: €"+str(total))

#2) Seconds → hh:mm:ss
#Ask a user for a number of seconds (int). Convert it to hours:minutes:seconds using // and
#% only.
# Result should look like 01:05:09
print("2)")
secondsImp=input("Enter seconds:")
hours=int(secondsImp)//3600
seconds=int(secondsImp)%3600
minutes=seconds//60
seconds=seconds%60

if(hours<10):
    hours="0"+str(hours)
else: str(hours)

if(minutes<10):
    minutes="0"+str(minutes)
else: str(minutes)

if(seconds<10):
    seconds="0"+str(seconds)
else: str(seconds)


print(hours+":"+minutes+":"+seconds)

#3) Triangle area (base & height)
#Ask user for base and a height in metres. Compute area = 0.5 * base * height.
#Round answer to 1 decimal place and print answer with unit
print("3)")
base=input("Enter base:")
height=input("Enter height:")
area=0.5*int(height)*int(base)
area=round(area,1)
print("Area= "+str(area))

print("4)")
#Ask the user for two whole numbers, but read them as strings βirst.
#1. Print their string concatenation (variable a + variable b).
#2. Then convert both to integers and
#o Calculate sum
#o Multiply together
#o Find average as a βloat with 1 decimal place.
#o Print results for sum, multiply and average

a=input("Enter whole number:")
b=input("Enter whole number:")
print("Concat: "+a+b)
a=int(a)
b=int(b)
print("Sum= "+str(a+b))
print("Multi= "+str(a*b))
avr=(a+b)/2
avr=round(avr,1)
print("Avr= "+str(avr))

#Ask for the bill amount (βloat), tip percent (e.g., 12.5), and number of people (int).
#Compute tip, total, and amount per person.
# Print in the following format: Tip: €X.XX | Total: € X.XX | Each: € X.XX

print("5)")
bill=input("Enter bill:")
tip=input("Enter tip:")
people=input("Enter number of people:")
bill=float(bill)
tip=float(tip)/100
people=int(people)

tipAmount=bill*tip
total=bill+tipAmount
perPerson=total/people

print("Tip: €"+str(tipAmount)+" | Total: €"+str(total)+" | Each: €"+str(perPerson))