def add_function(first, second):
    return first + second


def sub_function(first, second):
    return first - second


def mul_function(first, second):
    return first * second


def div_function(first, second):
    return first / second


class CalculatorConstructor:
    def __init__(self):
        first = 0
        second = 0

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second


if __name__ == '__main__':
    c = CalculatorConstructor(9, 4)
    '''
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())
    '''
    print(add_function(4, 5))
    print(sub_function(6, 3))
    print(mul_function(4, 3))
    print(div_function(10, 3))


