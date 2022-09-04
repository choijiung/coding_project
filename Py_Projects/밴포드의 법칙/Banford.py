from random import *
one = 0
two = 0
thr = 0
fou = 0
fiv = 0
six = 0
sev = 0
eig = 0
nin = 0


for i in range(1, 10000):
    random = str(randrange(1, 10000))
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
# print("1 : ", one)
# print("2 : ", two)
# print("3 : ", thr)
# print("4 : ", fou)
# print("5 : ", fiv)
# print("6 : ", six)
# print("7 : ", sev)
# print("8 : ", eig)
# print("9 : ", nin)

def chart(num):
    global bar
    if num < 800:
        bar = "|"
    elif num < 850:
        bar = "||"
    elif num < 900:
        bar = "|||"
    elif num < 1000:
        bar = "||||"
    elif num < 1110:
        bar = "|||||"
    elif num < 1120:
        bar = "||||||"
    elif num < 1130:
        bar = "|||||||"
    elif num < 1140:
        bar = "||||||||"
    print(bar)
chart(one)
chart(two)
chart(thr)
chart(fou)
chart(fiv)
chart(six)
chart(sev)
chart(eig)
chart(nin)