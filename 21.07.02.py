# 1.다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
ticker = "btc_krw"

print(ticker.upper())


# 2.다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
ticker = "BTC_KRW"

print(ticker.lower())


# 3.다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
a = "hello world"

print(a.split())


# 4.다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
ticker = "btc_krw"

print(ticker.split('_'))

#5.다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
date = "2020-12-30"
year, month, day = date.split('-')

print(year)
print(month)
print(day)


#6.문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
data = "039490     "

data.rstrip()

# 7.변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print('이름: %s 나이: %d' % (name1, age1))
print('이름: %s 나이: %d'% (name2, age2))


# 8. 문자열의 format( ) 메서드를 사용해서 7번 문제를 다시 풀어보세요.

print('이름 : {0} 나이: {1}'.format(name1, age1))
print('이름 : {0} 나이: {1}'.format(name2, age2))


#9. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
price = "5,969,782,550"

price = price.replace(',','')

price = int(price)
print(price)
print(type(price))

#10. 다음과 같은 문자열에서 '2020/12'만 출력하세요.
분기 = "2020/12(E) (IFRS연결)"

print(분기[:7])

#11. 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'

print(string.replace('a','A'))

#12. 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보세요.
pin = "881120-1068234"

print(pin[7])

#13.다음과 같은 문자열 a:b:c:d가 있다. a#b#c#d로 바꿔서 출력해 보세요.
a = "a:b:c:d"
print(a.replace(':', "#"))

#14. ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보세요. (join 활용)
a = ['Life', 'is', 'too', 'short']
print(" ".join(a))
