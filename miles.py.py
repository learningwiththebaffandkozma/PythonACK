#Problem : Intake miles and convert to kilometers
# kilometers = miles * 1.60934
#Enter miles 5
# 5 miles equals 8.04 kilometers.

miles = input('Enter miles:')

miles = int(miles)
conversion = 1.60934

kilometers = miles * conversion

print(miles, "miles is equal to", kilometers, "kilometers.")