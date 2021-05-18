class Car(object):
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

    def show_info(self):
        print(f'바퀴 수 = {self.wheel} \n가격 {self.price}')

    @staticmethod
    def main():
        ca1 = Car(4, 1200)
        bi1 = Bike(3, 50, "시마노")
        ca1.show_info()
        bi1.show_info()


class Bike(Car):
    def __init__(self, wheel, price, gudong):
        self.wheel = wheel
        self.price = price
        self.gudong = gudong

    def show_info(self):
        print(f'바퀴 수 = {self.wheel} \n가격 {self.price} \n구동계 {self.gudong}')


Car.main()
