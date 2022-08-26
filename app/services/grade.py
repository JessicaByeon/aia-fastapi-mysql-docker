from app.models.grade import Grade
class GradeService(object):
    def __init__(self) -> None:
        self.credit = 0 # 전역 변수
    
    def set_score(self, name, korean, english, math):
        grade = Grade(name, korean, english, math)
        grade.set_avg() # 실행하고
        avg = grade.get_avg() # 읽어온다
        
        if avg >= 90:
            self.credit = 'A'
        elif avg >= 80:
            self.credit = 'B'
        elif avg >= 70:
            self.credit = 'C'
        elif avg >= 60:
            self.credit = 'D'
        elif avg >= 50:
            self.credit = 'E'
        else :
            self.credit = 'F'

        
    def get_grade(self, name, korean, english, math): # parameter
        self.set_score(name, korean, english, math) # arguments
        return self.credit