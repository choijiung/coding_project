from random import *
import streamlit as st
one = 0
two = 0
thr = 0
fou = 0
fiv = 0
six = 0
sev = 0
eig = 0
nin = 0


for i in range(99):
    random = str(randrange(99))
    rcut = str(random[:1])
    if rcut == "1":
        one += 1
    elif rcut == "2":
        two += 1
    elif rcut == "3":
        thr += 1
    elif rcut == "4":
        fou += 1
    elif rcut == "5":
        fiv += 1
    elif rcut == "6":
        six += 1
    elif rcut == "7":
        sev += 1
    elif rcut == "8":
        eig += 1
    else:
        nin += 1
numchart = [one, two, thr, fou, fiv, six, sev, eig, nin]
st.write("# 밴포드의 법칙 ")
st.bar_chart(numchart)
# print("1 : ", one)
# print("2 : ", two)
# print("3 : ", thr)
# print("4 : ", fou)
# print("5 : ", fiv)
# print("6 : ", six)
# print("7 : ", sev)
# print("8 : ", eig)
# print("9 : ", nin)

# def chart(num):
#     global bar
#     if num < 1000:
#         bar = "|"
#     elif num < 1100:
#         bar = "||"
#     elif num < 1200:
#         bar = "|||"
#     elif num < 1300:
#         bar = "||||"
#     elif num < 1400:
#         bar = "|||||"
#     elif num < 1500:
#         bar = "||||||"
#     elif num < 1600:
#         bar = "|||||||"
#     elif num < 1700:
#         bar = "||||||||"
#     print(bar)
# chart(one)
# chart(two)
# chart(thr)
# chart(fou)
# chart(fiv)
# chart(six)
# chart(sev)
# chart(eig)
# chart(nin)
