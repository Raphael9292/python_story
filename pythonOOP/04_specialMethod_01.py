"""
(2,3) + (4,5) = (6,9)
(10,2) * 5 = (50,10)
Max((2,7)) = 7 // Max는 큰 값 출력
"""


class Vector(object):
    # def __init__(self, x, y):
    # packing을 하면 인자를 이렇게 받을 수 있음
    def __init__(self, *args):
        """
        Create a vector, example : v = Vector(2,3)
        """
        # Unpacking
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """
        Returns the vector info
        """
        # %r: raw data
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        """
        Returns the vector addition of self and other
        """
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))


# Vector Instance
v1 = Vector(4, 6)
v2 = Vector(123, 67)
v3 = Vector()

# 이건 클래스 docs
# print(Vector.__doc__)
# Magic Method
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)

# https://docs.python.org/3/library/functions.html#bool
# 값이 0 이라면 boolean에 따라 False로 출력
print(bool(v1), bool(v2))
print(bool(v3))
