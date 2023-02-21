# def sa(a,b):
#     print(f'{a}더하기{b}={a+b}\n')
#     print(f'{a}빼기{b}={a-b}\n')
#     print(f'{a}곱하기{b}={a*b}\n')
#     print(f'{a}나누기{b}={a/b}\n')

# sa(5,10)


# b = int(input())
# def gugu(a):
#     for n in range(1, 10):
#         print(f'{a}*{n} = {a*n:2d}')
# gugu(b)


# a = int(input())
# b = int(input())
# def gugu(a,b):
#     for x in range(a, b+1):
#         for y in range(1, 10):
#             print(f'{x}*{y} = {x*y:2d}')
# gugu(a,b)
#간단한 구구단


# import pyautogui
# import keyboard
# import time

# while 1:
#     position = pyautogui.position()
#     if keyboard.is_pressed('enter'):
#         print(position)
#         time.sleep(0.01)
#         if position==500:
#             break
#마우스 포인트 위치 표시


# a = 8
# for i in range(0, a):
#     print('*' * (i+1))
#왼쪽으로 쏠린 삼각형



# b = 8
# for x in range(0,b):
#     print(' ' * (b - (x+1)), end = '')
#     print('*' * (x+1))
# 오른쪽으로 쏠린 삼각형

# c = 5
# for x in range(0, c):
#     print(' ' * (c-x), end='')
#     print('*' * (1+(2*x)))
#삼각형


# c = 5
# for x in range(0, c):
#     print(" " * (c-x), end= "")
#     print("*" * (1+(2*x)))
# for y in range(0, c):
#     print(" " * (y+2), end ="")
#     print("*" * (1+(2*x)-(2*y)-2))  
#마름모 for 문 두개

# a = 9
# for x in range(0,a):
#     if x <= (a//2):
#         print(" " * (a//2-x), end ="")
#         print("*" * (1+(2*x)))
#     else:
#         print(" " * (x - a//2), end="")
#         print("*" * (a-(2*x-a)-1))
# 마름모 for 문 한개

# a = int(input("행:"))
# for x in range(0,a):
#     if x < a//2:
#         print(" " * (a - x), end ="")
#         print("*" * (1+2*x))
#     else:
#         print(" " * (a-x), end ="")
#         print("*" * ((x-a//2+1)+x-a//2), end="")
#         print(" " * ((2*x-1)-(4*(x-a//2))),end = "")
#         print("*" * ((x-a//2+1)+x-a//2))
# 가운데 빈 삼각형 있는 큰 삼각형


# h = 100
# b = 2/5
# i = 1
# while i<=10:
#     h = h * b
#     print(i, round(h,4))
#     i+=1
# 2/5만큼 튀는 공 while문




# print ("배열 수 입력")
# l = int(input())
# arr = list(0 for i in range(0,l))

# print("배열 요소 입력")
# for a in range(0,l):
#     arr[a] = [input("입력")]

# for a in range (0,l):
#     print(arr[a], end="")


# a = [1,2,3]
# b = [44,55,66]
# c = [7,8,9]
# l = len(a)
# st = [a,b,c]
# for sc in st:
#     t = 0
#     for s in sc:
#         t = t + s
#     ave = t/l
#     print(sc, t, ave)



# print ("분을 입력하세요")
# a = int(input())
# b = a//60
# c = a - (b*60)
# print (f"{b}시{c}분")

# from dataclasses import replace


# f = 75
# c = (f-32)/1.8
# print(int(c))

# mile = 5
# km = mile/0.62137
# m = km*1000
# km = round(km,5)
# m = round(m,2)
# print(f"{mile}\n마일\n{km}\n킬로미터\n{m}\n미터")
# print("%.4f"%km)

# a = "Eat Work Play Sleep repeat"
# a = a.replace("Eat Work Play Sleep repeat","Working Playing")
# print(a)

# replace
# count
#stack over flow


# a = float(input("숫자를 입력해주세요."))

# def pan(x):
#     if x > 0:
#         print("양수입니다.")
#     elif x == 0:
#         print("0입니다.")
#     else:
#         print("음수입니다.")

# pan(a)


# h = 50

# print("당신은 무인도에 있습니다. 구조 될때까지 노력하세요!!")
# print("사용할 수 있는 행동은 대괄호 안에 있는 숫자를 입력해주시면 됩니다.")
# print("당신의 행동 하나하나가 체력에 영향을 줍니다. 그리고 혹은 바로 게임오버일지도?\n.....................................")

# print("당신은 정신을 차리고 주변을 돌아봅니다...... \n")
# d = input("1. 당신의 행동은?     1.가만히 생각한다. 2.앞에 보이는 숲으로 일단 향한다.\n")
# if d =="1":
#     h = h+30
#     print(f".....................................\n당신은 자기자신의 상황을 되돌아봅니다. 체력+30  현재체력은 {h}\n\n")

#     print("당신은 곰곰히 생각해보니 핸드폰을 가지고 있던것이 기억났습니다.")
#     d = input("2-1. 당신의 행동은?     1.핸드폰으로 119 연락해보기   2.영화처럼 되지도 않을텐데 시도도안해본다.\n")
#     if d=="1":
#         print(".....................................\n핸드폰은 방수였기에 신호가 갔고 당신은 구조되었습니다.\n")
#         print("  축하 축하")
#     elif d=="2":
#         print(".....................................\n시도도 안하시는 것 보면 탈출할 생각이 없으시군요?\n")
#         h = h-100
#         if (h<=0):
#             print("\n///GAME OVER///\n")

# elif d =="2":
#     h = h-30
#     print(f"\n당신은 일단 숲으로 go 했습니다. 상남자이시네요!!   체력-30   현재체력은{h}\n\n")
#     print("당신은 정신을 차리고 주변을 돌아봅니다......")
#     d = input("2-2. 당신의 행동은?   1.나무를 타서 무인도를 살펴본다.. 2.무리하지 말고 불피울 나무가지나 찾는다.\n")
#     if d=="1":
#         h = h-20
#         print(f"\n당신은 너무 단기간에 무리해 돌아가셨습니다 ^^ 체력 -20 현재체력은{h}\n")
#         if (h<=0):
#             print("\n///GAME OVER///\n")
#     elif d=="2":
#         h = h-10
#         print(f"\n당신은 불 피울 수 있는 나무가지를 찾았습니다. 체력-10   현재체력은{h}\n")
#         d = input("3. 이후 행동은?   1.나무가지를 찾았으니 불을 피우자   2.먹을 것을 찾자\n")
#         if d=="1":
#             h = h-10
#             print(f"\n당신은 불을 피웠고 힘들어서 죽었습니다 ^^ 체력-10   현재체력은{h}\n")
#             if (h<=0):
#                 print("\n///GAME OVER///\n")
#                 print("모두들 빨리 탈출하는게 최고입니다. 괜히 무인도 찾아보지 마세요^^")
#         elif d=="2":
#             h = h-10
#             print(f"\n먹을 것을 찾다 힘들어서 돌아가셨습니다.^^ 체력-10   현재체력은{h}\n")
#             if (h<=0):
#                 print("\n///GAME OVER///\n")
#                 print("모두들 빨리 탈출하는게 최고입니다. 괜히 무인도 살펴보지 마세요^^")


# a = 0
# c = 0
# for a in range (1,100):
#     if a%2 == 0:
#         if a%6 == 0:
#             c = c+1
# print (c)

# s = "aa,bb,cc,dd,ee"
# r = s.split(",",3)
# print(r)
# 스플릿 함수는 문자열은 잘라서 리스트로 만들어주는 것이다.

# n = int(input())
# for n in range(n,0,-1):
#     print(f"파이썬 책 {n}권이 들어 있는 책장에 파이썬 책이 {n}권")
#     print(f"책을 한 권 꺼내 돌려 보고 나니 {n-1}권남았네.\n")

# a = 1
# b = 100
# while a<=5:
#     b = b*(3/5)
#     print(f"{a}, {round(b,4)}")
#     a += 1

# print("") 
# 위에것은 라운드를 써서 뒤에 0으로 자리수를 안맞추는데 밑에것은 포맷변경으로 해서 0으로 자리수 맞춤

# a = 1
# b = 100
# while a<=5:
#     b = b*(3/5)
#     print("%d, %.4f" % (a, b))
#     a += 1


# a = input("공백으로 이름들을 구분해 입력해주세요")
# b = a.split()
# c = len(b)
# d = 0

# for d in range(0,c):
#     print("안녕 ",b[d])


# numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# b = len(numbers)
# a = 0
# for a in range (0,b):
#     if numbers[a]%2 == 0:
#         print(numbers[a],"는 짝수입니다.")
#     elif numbers[a]%2 == 1:
#         print(numbers[a],"는 홀수입니다.")
    
# print("")
# for a in range (0,b):
#     c = str(numbers[a])
#     print(c,f"는 {len(c)} 자릿수 입니다.")
 

# print("")

# list_of_list = [[1,2,3],[4,5,6,7],[8,9]]
# a = len(list_of_list)
# for b in range(0,a):
#     x = len(list_of_list[b])
#     for c in range(0,x):
#         print(list_of_list[b][c])

# number = 358
# rem = rev = 0
# while number >= 1:
#     rem = number % 10
#     rev = rev * 10 + rem
#     number = number//10
# print(rev)
# 숫자 거꾸로 하는 코드

# max = 138
# while 1:
#     num = int(input())
#     if num > max:
#         print(num, "is too big!")
#         break


# character = {
#     "이름":"기사",
#     "레벨":12,
#     "아이템": {
#         "무기":"불꽃의 검",
#         "방어구":"풀플레이트"
#     },
#     "스킬":["베기","세게 배기","아주 세게 배기"]
# }

# for key in character:
#     if type(character[key]) is dict:
#         for item in character[key]:
#             print(f"{item} : {character[key][item]}") 
#     elif type(character[key]) is list:
#         for skill in character[key]:
#             print(f"{key} : {skill}")
#     elif type(character[key]) is str:
#         print(f"{key} : {character[key]}")
#     elif type(character[key]) is int:
#         print(f"{key} : {character[key]}")


# def power(item):
#     return item*item
# def under_3(item):
#     return item<3

# list_input_a = [1,2,3,4,5]

# output_a = map(power,list_input_a)
# print("# map() 함수의 실행결과")
# print("map(power, list_input_a):", output_a)
# print("map(power, list_input_a):", list(output_a))
# print()

# output_b = filter(under_3, list_input_a)
# print("# filter() 함수의 실행결과")
# print("filter(under_3, list_input_a):", output_b)
# print("filter(under_3, list_input_a):", list(output_b))


# class Student:
#     def std(self):
#         return "gongbu"

# students = Student()
# print(students.std())


# a = (lambda x,y: 10+20)(10,20)
# print(a)



# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_pybo():
#     return 'hello world!'


a,b = input().split()
a = int(a)
b = int(b)
def sa(x, y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
sa(a,b)

