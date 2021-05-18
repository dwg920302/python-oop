class StaticCalculator(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

    @staticmethod
    def main():
        sc = StaticCalculator(int(input('첫번째 수 입력')), int(input('두번째 수 입력')))
        print(f'{sc.first} + {sc.second} = {sc.add()}')
        print(f'{sc.first} - {sc.second} = {sc.sub()}')
        print(f'{sc.first} * {sc.second} = {sc.mul()}')
        print(f'{sc.first} / {sc.second} = {sc.div()}')


StaticCalculator.main()
