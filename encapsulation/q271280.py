import random


def rannum():
    return f'{random.randint(0, 999)}-{random.randint(0, 99)}-{random.randint(0, 999999)}'


def display_info_all(acl):
    for i in acl:
       i.display_info()


def display_millionaire(lst):
    for i in lst:
        if i.balance >= 1000000:
            print(f'{i.bname} {i.client} {i.accnum} {i.balance}')


class Account(object):
    def __init__(self, bname, client, accnum, balance):
        self.bname = bname
        self.client = client
        self.accnum = accnum
        self.balance = balance
        Account.account_stacked += 1
        deposit_count = 0

    def deposit(self, money, interest):
        if money > 0:
            self.balance += money
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance = self.balance * (100+interest) / 100
                print('[Interest]')
            # 여기에 입금 절차 넣기

    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
            # 여기에 출금 절차 넣기

    def display_info(self):
        print(f'{self.bname} {self.client} {self.accnum} {self.balance}')

    @classmethod
    def get_account_num(cls):
        return cls.account_stacked

    account_stacked = 0

    @staticmethod
    def main():

        aclist = []
        interest = 1.0
        menu = None

        while 1:
            print('[Menu] 0 to exit')
            if menu == 1:
                # 여기에 등록 기능
                aclist.append(Account("SC은행", input('예금주님의 이름 = '), rannum(), int(input('현재 잔액 = '))))
            elif menu == 2:
                pass
            else:
                pass
            display_info_all(aclist)
            print(Account.get_account_num())
            display_millionaire(aclist)


Account.main()

# 271 계좌번호 자리수가 일정치 않은 문제가 있음
# 276 잔고 단위표시 안함
# 280 아직 시도 못함
