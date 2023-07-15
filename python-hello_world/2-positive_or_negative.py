# Importing the necessary module
import random

# Generating a random number between -10 and 10 (inclusive)
number = random.randint(-10, 10)

# Checking whether the number is positive, negative, or zero
if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")