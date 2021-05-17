class BmiCalculator():
    def getdata(self, height, weight):
        self.height = height
        self.weight = weight

    def getbmi(self):
        return b.weight/(b.height/100)/(b.height/100)


if __name__ == '__main__':
    b = BmiCalculator()
    b.getdata(160, 65)
    print('BMI = ', b.getbmi())
