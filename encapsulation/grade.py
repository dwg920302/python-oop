class Grade:
    def setgrade(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor+self.eng+self.math

    def avg(self):
        return self.sum() / 3

    def addgrade(self, kor, eng, math):
        return kor+eng+math

    def addgrade(self):
        return g.kor+g.eng+g.math

if __name__ == '__main__':
    g = Grade()
    g.setgrade(76, 90, 80)
    print(g.sum())
    print(g.avg())