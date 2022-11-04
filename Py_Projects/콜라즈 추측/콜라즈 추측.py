from random import randint
count = 0

number = 837799
while number != 1:
    if number % 2 == 0:
        number = number / 2
    elif number % 2 == 1:
        number = (3 * number) + 1
    count += 1
print(count)