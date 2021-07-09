# 1. 리스트 생성
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)

movie_rank = ['닥터 스트레인지', '스플릿', '럭키']

# 2. movie_rank 리스트에 "배트맨"을 추가하라.
print(movie_rank.append("배트맨"))


#3. movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 4. movie_rank 리스트에서 '럭키'를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
movie_rank.remove("럭키")
print(movie_rank)

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]

print(movie_rank)


# 5. movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2:]
print(movie_rank)

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
movie_rank.pop()
movie_rank.pop()
print(movie_rank)

# 6. price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)

price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

li = []
for i in range(1, len(price)):
    li.append(price[i])
print(li)

# 7.슬라이싱을 사용해서 홀수만 출력하라.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(nums[::2])

num = []
for i in range(len(nums)):
    if nums[i] % 2 == 1:
        num.append(nums[i])
        
print(num)

# 8.슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.

nums = [1, 2, 3, 4, 5]

print(nums[::-1])

num = []
for i in range(4,-1,-1):
    num.append(nums[i])

print(num)


# 9.interest 리스트에는 아래의 데이터가 저장되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver']

interest.remove('LG전자')

print(" ".join(interest))

# 10. interest 리스트에는 아래의 데이터가 바인딩되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest[0]+interest[1]+interest[2]+interest[3]+interest[4])

result = "".join(interest)
print(result)

# 11. interest 리스트에는 아래의 데이터가 바인딩되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

print("\n".join(interest))

for i in range(len(interest)):
    print(interest[i])

# 12. 리스트에 있는 값을 오름차순으로 정렬하세요.
data = [2, 4, 3, 1, 5, 10, 9]

data.sort()
print(data)
print(sorted(data))


# 13. 
# 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
a = '881120-1068234'
print(a[:6], a[7:])


b,c =a.split('-')
print(b, c)


# 14 (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
a = (1,2,3)
a=list(a)
a.append(4)
a = tuple(a)
a


# 15. 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.
a = {'A':90, 'B':80, 'C':70}
print(a.pop('B'))

#16
a = input("단어입력 : ")

if a == a[::-1]:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")