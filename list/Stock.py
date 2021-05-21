class Stock(object):
    def __init__(self, symbol, code):
        self.symbol = symbol
        self.code = code

    def get_stock_info(self):
        return f'종목명 : {self.symbol} 종목코드 : {self.code}'

    @staticmethod
    def main():
        while 1:
            menu = input('[System] 주식 정보 입력 -> 1 / 조회 -> 2 / 종료 -> 0] ')
            if menu == '0':
                print('[System] By2By2')
                break
            elif menu == '1':
                s = Stock(input('종목명 입력 -> '), input('종목코드 입력 -> '))
            elif menu == '2':
                print(s.get_stock_info())
            else:
                print('[Error] 잘못된 접근')


Stock.main()
