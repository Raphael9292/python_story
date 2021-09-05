class Car():
    """
    Car class
    Author: raphael
    Property: gg
    """
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str: {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr: {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('my ID : {}'.format(id(self)))
        print('Car Detail Info: {} {}'.format(self._company, self._details.get('price')))


car1 = Car('ferrari', {'color': 'red', 'power': 500, 'price': 5000})
car2 = Car('benz', {'color': 'black', 'power': 300, 'price': 3000})
car3 = Car('bmw', {'color': 'white', 'power': 100, 'price': 1000})

# check instanceID
print(id(car1))
print(id(car2))
print(id(car3))

# check dir & __dict__
print(dir(car1))
print(dir(car2))

# 같은 key로 확인
print(car1.__dict__)
print(car2.__dict__)

# check Annotations
print(Car.__doc__)


# check detail_info()
car1.detail_info()

# comparison
# 생성할때 사용한 클래스는 같은 클래스다 (같은 부모다) // 인스턴스가 다른거지
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__))