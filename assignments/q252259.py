class Human(object):
    def __init__(self):
        print('응애응애')

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print(f'이름 : {self.name} / 나이 : {self.age} / 성별 : {self.gender}')

    def __del__(self):
        print('나의 죽음을 알리지 말라')


if __name__ == '__main__':
    areum = Human("조아름", 25, "여자")
    areum.who()
    del areum
