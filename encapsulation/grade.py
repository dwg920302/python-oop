def get_average(kor, eng, math):
    return (kor+eng+math)/3


class Grade(object):
    def __init__(self):
        kor = 0
        eng = 0
        math = 0

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor+self.eng+self.math

    def avg(self):
        return round(self.sum() / 3, 2)

    def get_grade(self):
        score = int(self.avg())
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'

        return grade

    @staticmethod
    def main():
        g = Grade(int(input('국어 점수 입력')), int(input('영어 점수 입력')), int(input('수학 점수 입력')))
        print(f'총점 = {g.sum()}')
        print(f'평균 점수 = {g.avg()}')
        print(f'학점 = {g.get_grade()}')


Grade.main()
