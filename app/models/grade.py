# 클래스에 학생 이름을 입력하면
# 해당 학생이 얻은 국어, 영어, 수학 3과목의 평균점수에 따라
# 학점을 A-F까지 출력하시오


class Grade(object):
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
        self.avg = 0.0 # 초기화 (메모리 공간 확보)
        
    def set_avg(self):
        self.avg = (self.korean + self.english + self.math)/3
        
    def get_avg(self):
        return self.avg
        
    
    # 두 메서드가 공유하는 변수(전역변수)로! 공유하려면 전역변수로 만들어야한다. self!
    
