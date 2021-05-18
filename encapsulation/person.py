'''
이름, 출생년도, 주소를 입력받아서
회원가입한 사람의 이름, 나이(만), 주로를 출력하시오
'''


class Person(object):
    def __init__(self, name, birth, adr):
        self.name = name
        self.birth = birth
        self.adr = adr

    def get_age(self, year):
        return year - self.birth

    @staticmethod
    def main():
        year = 2021
        p = Person(input('이름 = '), int(input('출생년도 = ')), input('주소 = '))
        print(f'이름 = {p.name} 나이 = {p.get_age(year)} 주소 = {p.adr}')


Person.main()
