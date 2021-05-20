class CoffeeVendor(object):
    def __init__(self):
        pass

    @staticmethod
    def main():
        coffee = 10
        while True:
            money = int(input('Insert Money ->'))
            if money >= 300:
                money -= 300
                print(f'[System] 커피 하나를 뽑았습니다.')
                coffee -= 1
                if money != 0:
                    print(f'거스름돈 {money}원 반환')
            else:
                print('[System] 커피값 부족, 돈 반환')
            print(f'남은 커피 수 -> {coffee}')
            if coffee == 0:
                print('[System] 커피가 전부 소진되어 판매 종료')
                break


CoffeeVendor.main()
