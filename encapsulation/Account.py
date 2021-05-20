import random


def rannum():
    return f'{random.randint(0, 999)}-{random.randint(0, 99)}-{random.randint(0, 999999)}'
    # 자리수가 줄어들면 길이가 줄어듬;


def rannum2(count):
    ran = random.randint(0, pow(10, count)-1)
    num = ''
    if count>1:
        while count>1:
            num += '0'
    num += ran
    return ran


def ran_num():



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
