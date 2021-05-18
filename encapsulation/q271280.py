import random


def accnum_gen():
    num = ""
    num1 = random.randint(0, 999)
    num2 = random.randint(0, 99)
    num3 = random.randint(0, 999999)
    num += (num1)
    return num


class Account(object):

    account_stacked = 0
    interest = 1.0

    def __init__(self, bname, client, accnum, balance):
        self.bname = bname
        self.client = client
        self.accnum = accnum
        self.balance = balance
        deposit_count = 0

    def deposit(self, money, interest):
        if(money > 0):
            self.balance += money
            self.deposit_count += 1
            if(self.deposit_count % 5 == 0):
                self.balance = self.balance * (100+interest) / 100
            #입금 절차 넣기

    def withdraw(self, money):
        if(money <= self.balance):
            self.balance -= money
            #출금 절차 넣기

    def display_info(self):
        print(f'{self.bname} {self.client} {self.accnum} {self.balance}')


    @classmethod
    def get_account_num(cls):
        return cls.account_stacked

    @staticmethod
    def main():
        ac = Account("SC은행", input('예금주님의 이름 = '), None, int(input('현재 잔액 = ')))
        print(ac.change)
        print(ac.accnum)


Account.main()

# 271 계좌번호 만드는 거에서 막힘 qnpfr..
# 276 계좌번호 안만듬, 잔고 단위표시 안함
# 278 279 280은 아직 때가 아닌거 같음;