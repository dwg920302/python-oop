def bmi_function(height, weight):
    return weight/((height/100)**2)


class BmiCalculator(object):
    def __init__(self):
        height = 0
        weight = 0

    def __init__(self, height, weight):
        self.weight = weight
        self.height = height

    '''
    고도 비만 : 35 이상
    중도 비만 : 30 이상 35 미만
    경도 비만 : 25 이상 30 미만
    과체중 : 23 이상 25 미만
    정상 : 18.5 이상 23 미만
    저체중 : 18.5 미만
    '''

    def get_Bmi(self):
        return self.weight/((self.height/100)**2)

    def get_grade(self):
        bmi = self.get_Bmi()
        if(bmi <= 18.5):
            grade = '저체중'
        elif(bmi <= 23):
            grade = '정상'
        elif(bmi <= 25):
            grade = '과체중'
        elif(bmi <= 30):
            grade = '경도 비만'
        elif(bmi <= 35):
            grade = '중도 비만'
        else:
            grade = '고도 비만'
        return grade


    @staticmethod
    def main():
        b = BmiCalculator(int(input('신장 입력')), int(input('체중 입력')))
        # print(b.get_Bmi())
        # print(BmiCalculator(163, 67).get_Bmi())
        print(f'신장 {b.height} 체중 {b.weight} \n당신의 BMI 지수 = {round(b.get_Bmi(), 2)} 비만도 = {b.get_grade()}')


BmiCalculator.main()
