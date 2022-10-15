import time


text = "가나"
isright = False

start = input("1초 미만 = 1성, 2초 미만 = 2성, 3초 미만 = 3성, 4초 미만 = 4성, 5초 미만 = 5성, 5초 이하 = 순위 x")
begin = time.time()

inputstart = input("입력:")
if inputstart == text:
    isright = True
    end = time.time()
else:
    isright = False
    end = time.time()

if isright == True:
    result = end-begin
    result = round(result, 3)
    if result < 1:
        print("1성")
    elif result < 2:
        print("2성")
    elif result < 3:
        print("3성")
    elif result < 4:
        print("4성")
    elif result < 5:
        print("5성")
    else:
        print("6성")
    print("{}초".format(result))
    print("성공!")
else:
    print("실패")
