# class Human:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = Human('아무개', 40,'남자')

# print(areum.age)


# class a:
#     def ab(self):
    
# print()
# 이런식으로 셀프 집어넣을 것.


# class Student:
#     def start(self):
#         print('안녕하세요')
#     def printName(self,name):
#         print('이름은 {0} 입니다'.format(name))

# stu = Student()
# Student.start(stu)
# stu.printName('홍길동')

# class Student:
#     schoolName = '123456'

# stu1 = Student()
# stu2 = Student()

# print('stu1의 주소: {0}'.format(id(stu1)))
# print('stu2의 주소: {0}'.format(id(stu2)))

#Student.schoolName='Seoul' 이거는 덮어씌우는 것

# print('\nStudent의 학교', Student.schoolName)
# print('\nstu1의 학교', stu1.schoolName)
# print('\nstu의 학교', stu2.schoolName)


# +- 연산 기억 계산기
# class Calculator:
#     def __init__(self):
#         self.result = 0

#     def add(self, num):
#         self.result += num
#         return self.result
#     def sub(self,num):
#         self.result -= num
#         return self.result

# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal1.sub(7))
# print(cal2.add(3))
# print(cal2.add(7))   

# 구구단 계산기
# class gugu:    
#     def gu(n):
#         for i in range(1,10):
#             print(f'{n}*{i}={n*i}')
# b = int(input())
# gugu.gu(b)


# class FourCal():
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second

# a = FourCal()
# print(type(a))

# a.setdata(4,2)
# print(a.first)
# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())

class a:
    def jak(b,c):
        if b%2==0 and c%2 == 0:
            print("짝수입니다.")
        elif b%2==1 and c%2 == 1:
            print("홀수입니다.")
        else:
            print("두 인수 짝수 홀수 다름")
    def ave(b,c):
        return (b+c)/2
    def sagak(b,c):
        i = 0
        j = 0
        for i in range (b):
            for j in range(c):
                print("*",end="")
            print("")

x,y = map(int, input('숫자두개').split(','))
a.jak(x,y)
print(a.ave(x,y))
a.sagak(x,y)