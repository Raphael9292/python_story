# 구조 설계 후 class, instance로 재사용성 증가

# dict 구조
# car_dicts = [
#     {'car_company': 'ferrari', 'car_detail': {'color': 'white', 'power': 500, 'price': 5000}},
#     {'car_company': 'bmw', 'car_detail': {'color': 'blue', 'power': 300, 'price': 3000}},
#     {'car_company': 'hyundae', 'car_detail': {'color': 'red', 'power': 200, 'price': 2000}}
# ]
#
# print(car_dicts)


# class 구조
# self는 인스턴스를 받는다는 약속
class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # magic method를 이용하여 원하는 방식으로 속성을 볼 수 있다
    # str: ferrari - {'color': 'red', 'power': 500, 'price': 5000}
    def __str__(self):
        return 'str: {} - {}'.format(self._company, self._details)

    # str과 차이점은 print문으로 사용자 입장에서 원하는 출력을 볼 때는 str method
    # 객체이고 자료형 타입에 따라 보고싶을땐 representation method
    # repr: ferrari - {'color': 'red', 'power': 500, 'price': 5000}
    def __repr__(self):
        return 'repr: {} - {}'.format(self._company, self._details)


# instance
car1 = Car('ferrari', {'color': 'red', 'power': 500, 'price': 5000})
car2 = Car('benz', {'color': 'black', 'power': 300, 'price': 3000})
car3 = Car('bmw', {'color': 'white', 'power': 100, 'price': 1000})

# 아무런 method 미사용 시 / car object: <__main__.Car object at 0x10967ffa0>
# 생성한 인스턴스에 대한 정보
# print(car1)


# list
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

# metadata
print(dir(car_list))