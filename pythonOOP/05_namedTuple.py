"""
https://docs.python.org/ko/3/library/collections.html#collections.namedtuple
https://wikidocs.net/126315
객체: 데이터 추상화
객체는 id, type으로 확인 가능함 (value)
"""

# 일반적인 tuple
# 두 점 사이의 거리
dt1 = (1.0, 5.0)
dt2 = (3.0, 7.0)

from math import sqrt

l_leng1 = sqrt((dt1[0] - dt2[0]) **2 + (dt1[1] - dt2[1]) ** 2)
print(l_leng1)


# namedTuple
from collections import namedtuple

Point = namedtuple('Point', 'x y')

dt3 = Point(1.0, 5.0)
dt4 = Point(3.0, 7.0)

print(dt3)
print(dt3[0])
print(dt3.x)

"""
튜플형식으로 사용하고 있는데 
접근은 인덱스로도 가능하고
뒤에 key로도 가능하다
"""

# 인덱스로 해도 상관없으나 그냥 key로 해보고 싶었다
l_leng2 = sqrt((dt3.x - dt4.x) **2 + (dt3.y - dt4.y) ** 2)
print(l_leng2)

# Declare namedTuple
Point0 = namedtuple('Point', 'x y')
Point1 = namedtuple('Point', 'x, y')
Point2 = namedtuple('Point', ['x', 'y'])
Point3 = namedtuple('Point', 'x y x class', rename=True) # Default = False
print(Point0, Point1, Point2, Point3)

# Dict to Unpacking
dict = {'x': 100, 'y': 60}

# Make Instance
p0 = Point0(x=10, y=30)
p1 = Point1(20, 40)
p2 = Point2(30, 20)

# Point(x=10, y=20, _2=30, _3=40)
p3 = Point3(10, 20, 30, 40)

# Unpacking
print('Unpacking')
p4 = Point0(**dict)
print(p4)

print(p0)
print(p1)
print(p2)
print(p3)

# Usage
print(p0[0] + p1[1])
print(p0.x + p1.y)


# namedTuple Method
test_dict = [50, 30]
p4 = Point0._make(test_dict)
print(p4)

# _asdict(): OrderedDict 반환 // 정렬로 반환
print(p4._asdict())

# namedTuple example
# 각 클래스 당 20개, 4개 class

Classes = namedtuple('Classes', ['rank', 'number'])

numbers = [str(n) for n in range (1, 21)]
ranks = 'A B C D'.split()

# 한줄로 하기 위해 추상화
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))
for student in students:
    print(student)

# 직관적
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
                for number in [str(n)
                    for n in range(1, 21)]]
print(len(students2))
for student in students2:
    print(student)
