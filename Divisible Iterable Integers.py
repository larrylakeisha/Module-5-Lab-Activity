# Lakeisha Larry
# October 30, 2021

# This program iterates integers from 1 to 50 and tells the user what it is divisible by

for x in range(1, 50):
    if x % 3 == 0:
        print("Divisible by three")
    if x % 5 == 0:
        print("Divisible by five")

    if x % 3 == 0 and x % 5 == 0:
        print("Divisible by both")
