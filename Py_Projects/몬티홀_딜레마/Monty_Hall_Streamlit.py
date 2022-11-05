from random import *
import random
import streamlit as st
from PIL import Image

def test():
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
    st.write("차가 나올 확률: {}%".format(Car_per))
    st.write("염소가 나올 확률: {}%".format(Goat_per))

tab1, tab2 = st.tabs(["테스트", "코드보기"])
with tab1:
    image = Image.open("Py_Projects/몬티홀_딜레마/Monty_Hall_site_Image.png")
    st.header("몬티홀 딜레마 테스트 사이트")
    st.image(image, caption='몬티홀 딜레마')
    button = st.button("테스트 해보기")
    if button:
        test()
    else:
        st.write("버튼을 눌러보세요")
with tab2:
    image2 = Image.open("Py_Projects/몬티홀_딜레마/monty hall.png")
    st.header("코드보기")
    st.image(image2, caption="코드")