import random


def rannum():
    return "{0:0>3}".format(f'{random.randint(0, 999)}')+'-'+"{0:0>2}".format(f'{random.randint(0, 99)}')+'-'+"{0:0>6}".format(f'{random.randint(0, 999999)}')


class Account(object):
    def __init__(self, client, balance):
        self.bank = 'SC은행'
        self.client = client
        self.number = rannum()
        self.balance = balance

    def get_account(self):
        return f'은행={self.bank} / 예금주={self.client} / 계좌번호={self.number} / 잔액={self.balance}'

    @staticmethod
    def main():
        while 1:
            menu = input('[Menu]')
            if menu == '0':
                print('[System] Shut Down')
                break
            elif menu == '1':
                a = Account(input('이름 입력 -> '), input('잔액 입력 -> '))
            elif menu == '2':
                print(a.get_account())
            else:
                print('[Error] 잘못된 접근')


Account.main()
