from random import *
import random

Car_count = 0
Goat_count = 0
All_count = 0
for i in range(10000):
    door = {}
    things = ["Goat", "Car", "Goat"]
    for i in range(3):
        random_choice = random.choice(things)
        door[i+1] = str(random_choice)
        things.remove(random_choice)
    choice = randint(1, 3)
    choice_thing = door[choice]
    del door[choice]
    goat_Key_list = [k for k, v in door.items() if v == 'Goat']
    goat_Key = goat_Key_list[0]
    del door[goat_Key]
    door_change = 0
    door1 = 1 in door
    door2 = 2 in door
    door3 = 3 in door
    if door1 == True:
        door_change = door[1]
    elif door2 == True:
        door_change = door[2]
    elif door3 == True:
        door_change = door[3]

    if door_change == 'Car':
        Car_count += 1
    elif door_change == 'Goat':
        Goat_count += 1
    All_count += 1
Car_per  = (Car_count / All_count) * 100
Goat_per = (Goat_count / All_count) * 100
Car_per = round(Car_per, 2)
Goat_per = round(Goat_per, 2)
print("차가 나올 확률: {}%".format(Car_per))
print("염소가 나올 확률: {}%".format(Goat_per))