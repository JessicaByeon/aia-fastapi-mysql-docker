class Calculator(object): # 클래스
    def __init__(self, first, second):
        self.first = first # 속성(property) 등록
        self.second = second
        
    def sum(self): # 메소드(method) 등록
        return self.first + self.second
    
    def subtract(self):
        return self.first - self.second

    def multi(self):
        return self.first * self.second
    
    def divide(self):
        return self.first / self.second