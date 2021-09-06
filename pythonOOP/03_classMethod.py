class Car():
    """
    Car class
    Author: raphael
    Description: Class, Static, Instance Method
    """

    # class variables (share value all instances)
    price_variability_ratio = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str: {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr: {} - {}'.format(self._company, self._details)

    # Instance Methods
    # self: 객체의 고유한 속성값을 사용
    def detail_info(self):
        print('my ID : {}'.format(id(self)))
        print('Car Detail Info: {} {}'.format(self._company, self._details.get('price')))

    # Making Get Instance Method
    def get_price(self):
        return 'Before Price, Company: {}, {}'.format(self._company, self._details.get('price'))

    # Making Get Instance Method
    def get_price_after(self):
        return 'After Price, Company: {}, {}'.format(self._company, self._details.get('price') * Car.price_variability_ratio)

    # Class Method
    # python에선 주석을 Decorator라고 명명함
    @classmethod
    def raise_price(cls, ratio):
        # cls.price_variability_ratio
        if ratio <= 1:
            print('It is meaningless because it is less than 100')
            return
        cls.price_variability_ratio = ratio
        print('The price has gone up')
        return

    # Static Method
    @staticmethod
    def check_car(inst):
        if inst._company == 'benz':
            return 'YES This car is {}'.format(inst._company)
        else:
            return 'Nope!'


car1 = Car('ferrari', {'color': 'red', 'power': 500, 'price': 5000})
car2 = Car('benz', {'color': 'black', 'power': 300, 'price': 3000})
car3 = Car('bmw', {'color': 'white', 'power': 100, 'price': 1000})


# check value of car
# 직접 접근
print(car1._details.get('price'))
print(car2._details['price'])


print(car1.get_price())
print(car2.get_price())

# 직접 접근
Car.price_variability_ratio = 1.4

print(car1.get_price_after())
print(car2.get_price_after())

# class method 사용
Car.raise_price(1.8)
print(car2.get_price_after())

# static method
# 인스턴스 호출
print(car2.check_car(car2))

# 클래스로 호출
print(Car.check_car(car1))
