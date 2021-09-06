"""
Special Method(Magic Method)
파이썬 dive
Sequence, Iterator, Function, Class
class 안에 정의할 수 있는 특별한 Built in method
"""

# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 100

print(n+100)
# __add__
print(n.__add__(100))

# 클래스 생성자 타입을 호출
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))


# class 생성 및 method 구현
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info: {} {}'.format(self._name, self._price)

    def __add__(self, x):
        return self._price + x._price

    def __sub__(self, x):
        return self._price - x._price

    # rich comparison
    # https://docs.python.org/3/reference/datamodel.html#object.__le__
    def __le__(self, x):
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        if self._price >= x._price:
            return True
        else:
            return False


# 인스턴스 생성
a1 = Fruit('Apple', 10000)
a2 = Fruit('Banana', 3000)

print(a1 + a2)

# class가 아닌 일반적으로 한다면?
# print(a1._price + a2._price)

# check values
print(a1 >= a2)
print(a1 <= a2)
print(a1 - a2)
print(a2 - a1)
print(a1)
print(a2)
