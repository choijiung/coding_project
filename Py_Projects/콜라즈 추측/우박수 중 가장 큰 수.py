maximum = 0 # 계산 횟수를 저장할 변수
result = 0  # 최대 계산 횟수일 경우 어떤 수에서 발생했는지 저장하는 변수

for i in range(1, 100000):
    counter = 1 # 카운터는 매번 반복문이 다시 실행될 때 초기화 되어야 한다.

    j = i # i각 계속 연산되어야 하므로 따로 변수 j를 주어 i는 보존
    while True:
        if j == 1: # 계산 결과가 1이 되면 다음 숫자로 넘어가야 해서 while문 종료
            if maximum < counter: # 최댓값일 때 변수에 기록
                maximum = counter
                result = i

            break # while 문 종료

        counter += 1

        if j % 2 == 0:
            j = j / 2
        else:
            j = 3 * j + 1


print(result, maximum)  # 525회 계산을 하는 837799