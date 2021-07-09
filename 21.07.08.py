# 1. a 리스트에서 중복 숫자를 제거해 보자.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(list(set(a)))

# 2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수이면서 7의 배수인 수의 합을 구해 보자.
i = 1
result = 0
while i <1000:
    i = i +1
    if i % 3 == 0 and i % 7 == 0:
        result += i
    else:
        pass
    
print(result)

while True:
    if i == 1001:
        break
    if i % 3 == 0 and i % 7 == 0:
        result += i
    else:
        pass

# 3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
# *
# **
# ***
# ****
# *****
i = 1
while True:
    if i == 6:
        break
    print('*' * i)
    i += 1

# 4. for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
for i in range(1, 101):
    print(i)


# 5. A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.

score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
result = 0
for i in score:
    result += i
    if i==score[-1]:
        print(result / len(score))    



# 6. 자판기(pro, 커피 한 잔에 300원이라 가정, 초기 커피는 10개)
# 돈을 넣어 주세요: 500
# 거스름돈 200를 주고 커피를 줍니다.
# 돈을 넣어 주세요: 300
# 커피를 줍니다.
# 돈을 넣어 주세요: 100
# 돈을 다시 돌려주고 커피를 주지 않습니다.
# 남은 커피의 양은 8개입니다.
# 돈을 넣어 주세요: 0
# 종료합니다

coffee = 10

while True:
    a = int(input('돈을 넣어 주세요 : '))
    if a >= 300:
        print("거스름돈 %d원을 주고 커피를 줍니다" % (a-300))
        coffee = coffee - 1
    elif a == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    else:
        if a == 0:
            print("종료합니다.")
            break
        else:
            print("돈을 다시 돌려주고 커피를 주지 않습니다.")
            print("남은 커피의 양은 %d개입니다." % coffee)

    
    