class StaticCalculator(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    @staticmethod
    def do_the_math(first, menu):
        second = int(input('두 번째 수 입력 ->'))
        result = None
        symbol = ''
        if menu == 1:
            result = first + second
            symbol = '+'
        elif menu == 2:
            result = first - second
            symbol = '-'
        elif menu == 3:
            result = first * second
            symbol = '*'
        elif menu == 4:
            result = first / second
            symbol = '/'
        return f'{first} {symbol} {second} = {result}'

    @staticmethod
    def main():
        while 1:
            menu = input('[계산기 프로그램] 0 = 종료]')
            if menu == '0':
                print('[System] Shutdown')
                break
            else:
                first = int(input('첫 번째 수 입력 ->'))
                while 1:
                    menu = int(input('더하기는 1, 빼기는 2, 곱하기는 3, 나누기는 4 입력'))
                    if menu == 1 | 2 | 3 | 4:
                        print(StaticCalculator.do_the_math(first, menu))
                        break
                    else:
                        print('[Error] 올바른 수를 입력하십시오.')


StaticCalculator.main()
