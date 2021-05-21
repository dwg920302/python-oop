import random


class AdvAccount(object):
    def __init__(self, name, number, balance):
        self.BANK = 'SC은행'
        self.name = name
        self.number = number
        self.balance = balance
    '''
    계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
    '''

    @staticmethod
    def rannum(cnt):
        return (str(random.randint(0, 9)) for i in range(cnt))

    @staticmethod
    def create_account_number():
        ls = [str(random.randint(0, 9)) for i in range(3)]
        ls += '-'
        ls += (AdvAccount.rannum(2))
        ls += '-'
        ls += (AdvAccount.rannum(6))
        return "".join(ls)

    def to_string(self):
        return f'Bank Name : {self.BANK},' \
               f'Name : {self.name},' \
               f'Number : {self.number},' \
               f'Balance : {self.balance}'

    @staticmethod
    def del_elem(ls, number):
        for i, j in enumerate(ls):
            if j.number == number:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('1 = 계좌개설  2 = 계좌목록  3 = 입금  4 = 출금  5 = 계좌탈퇴  0 = 종료 ]]')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(AdvAccount(input('예금주명 입력 -> '), AdvAccount.create_account_number(), input('잔액 입력 -> ')))
            elif menu == '2':
                for i in ls:
                    print(i.to_string())
            elif menu == '3':
                number = input("입금할 계좌번호 입력 -> ")
                money = input("입금할 금액 -> ")
                for i, j in enumerate(ls):
                    if j.number == number:
                        replace = AdvAccount(j.number. j.name, int(j.money)+int(money))
                        AdvAccount.del_elem(ls, number)
                        ls.append(replace)
            elif menu == '4':
                number = input("출금할 계좌번호 입력 -> ")
                money = input("출금할 금액 -> ")
                AdvAccount.del_elem(ls, number)
                if j.number == number:
                    replace = AdvAccount(j.number.j.name, int(j.money) - int(money))
                    AdvAccount.del_elem(ls, number)
                    ls.append(replace)
            elif menu == '5':
                number = input('삭제할 계좌번호 입력')
                AdvAccount.del_elem(ls, number)
            else:
                print('Error')


AdvAccount.main()
