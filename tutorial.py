# ask the user to input to values to store them in two values in variable that have the anmes num1 and num2
num1, num2= input('Enter two numbers').split()
#convert the strings into regualr numbers Integer
num1 = int(num1)
num2 = int(num2)
#add the values enter and store in a variable named sum
sum = num1 + num2
#subtract values and store in difference
difference = num1 - num2
#multiply values and store in product
product = num1  num2
#divide values and store in quotient
quotient = num1  num2
#use modulous to find remainder
remainder = num1 % num2
#print values
print({} + {} = {}.format(num1, num2, sum))
print({} - {} = {}.format(num1, num2, difference))
print({}  {} = {}.format(num1, num2, product))
print({}  {} = {}.format(num1, num2, quotient))
print({} % {} = {}.format(num1, num2, remainder))