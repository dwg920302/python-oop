class Stock(object):
    def __init__(self, symbol, code):
        self.symbol = symbol
        self.code = code

    def to_string(self):
        return f'종목명 : {self.symbol} 종목코드 : {self.code}'

    @staticmethod
    def del_element(ls, code):
        for i, j in enumerate(ls):
            if j.code == code:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('[System] 주식 정보 입력 -> 1 / 조회 -> 2 / 정보 수정 -> 3 / 삭제 -> 4 / 종료 -> 0] ')
            if menu == '0':
                print('[System] By2By2')
                break
            elif menu == '1':
                ls.append(Stock(input('종목명 입력 -> '), input('종목코드 입력 -> ')))
            elif menu == '2':
                for i in ls:
                    print(i.to_string())
            elif menu == '3':
                code = input(f'종목명을 수정할 주식의 종목코드 입력 -> ')
                stock = Stock(input('수정할 종목명 입력 -> '), code)
                Stock.del_element(ls, code)
                ls.append(stock)
            elif menu == '4':
                Stock.del_element(ls, input('삭제할 주식의 종목코드 입력 -> '))
            else:
                print('[Error] 잘못된 접근')


Stock.main()
