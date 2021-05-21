import random


def rannum():
    return "{0:0>3}".format(f'{random.randint(0, 999)}')+'-'+"{0:0>2}".format(f'{random.randint(0, 99)}')+'-'+"{0:0>6}".format(f'{random.randint(0, 999999)}')


def display_info(client):
    print(f'은행명:{client.bname} / 예금주:{client.cname} / 계좌번호:{client.accnum} / 잔고:{format(client.balance, ",")}')


def display_info_all(ls):
    for i in ls:
        display_info(i)


def display_millionaire(ls):
    for i in ls:
        if i.balance >= 1000000:
            display_info(i)


def deposit(client, money, interestp):
    if money > 0:
        client.balance += money
        client.deposit_count += 1
        client.deposit_list.append(money)
        print(f'[System] {money}원이 입금되었습니다.')
        if client.deposit_count % 5 == 0:
            interest = int(client.balance * (100+interestp) / 100 - client.balance)
            client.balance += interest
            client.deposit_list.append(interest)
            print(f'[System] 이자가 들어왔습니다. 이자율은 {interestp}%이며 {interest}원입니다.')


def withdraw(client, money):
    if money <= client.balance:
        client.balance -= money
        client.withdraw_list.append(-money)
        print(f'[System] {money}원이 출금되었습니다.')
    else:
        print('[Error] 예금 잔액 부족')


def deposit_history(client):
    print('[입금내역]')
    for i in client.deposit_list:
        print(f'{i}')


def withdraw_history(client):
    print('[출금내역]')
    for i in client.withdraw_list:
        print(f'{i}')


class Account(object):
    def __init__(self, cname, balance):
        self.bname = 'SC은행'
        self.cname = cname
        self.accnum = rannum()
        self.balance = balance
        Account.account_stacked += 1
        self.deposit_count = 0
        self.deposit_list = []
        self.withdraw_list = []

    account_stacked = 0

    @classmethod
    def get_account_num(cls):
        return cls.account_stacked

    @staticmethod
    def main():

        interest = 1.0
        ls = []

        while 1:
            menu = input('[Menu] 1 = 등록 / 2 = 이름으로 조회 / 3 = 전부 조회 / 4 = 입금 / 5 = 출금 \n 6 = 100만원 이상 예금자 출력 / 7 = 출금 내역 / 8 = 출금 내역 / 0 = 종료] ')
            if menu == '0':
                print('[System] Bye Bye')
                break
            if menu == '1':
                # 여기에 등록 기능
                ls.append(Account(input('예금주님의 이름 = '), int(input('현재 잔액 = '))))
            elif menu == '2':
                client = input('[System] 예금주님의 이름 입력 -> ')
                for i, j in enumerate(ls):
                    if j.cname == client:
                        display_info(ls[i])
            elif menu == '3':
                display_info_all(ls)
                print(f'[System] 현재 계좌 수는 전부 [{Account.get_account_num()}]개 입니다.')
            elif menu == '4':
                client = input('[System] 예금주님의 이름 입력 -> ')
                for i, j in enumerate(ls):
                    if j.cname == client:
                        deposit(ls[i], int(input('입금할 금액 입력')), interest)
            elif menu == '5':
                client = input('[System] 예금주님의 이름 입력 -> ')
                for i, j in enumerate(ls):
                    if j.cname == client:
                        withdraw(ls[i], int(input('출금할 금액 입력')))
            elif menu == '6':
                display_millionaire(ls)
            elif menu == '7':
                client = input('[System] 예금주님의 이름 입력 -> ')
                for i, j in enumerate(ls):
                    if j.cname == client:
                        deposit_history(ls[i])
            elif menu == '8':
                client = input('[System] 예금주님의 이름 입력 -> ')
                for i, j in enumerate(ls):
                    if j.cname == client:
                        withdraw_history(ls[i])
            else:
                print('[Error] 올바른 기능에 해당하는 숫자를 입력하십시오. ')


Account.main()
