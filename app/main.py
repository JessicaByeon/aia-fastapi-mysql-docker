import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))
from app.api.endpoints.url import Url
from app.constants.menus import LOGIN, LOGOUT, CALCULATOR, GRADE, QUIZ_1, QUIZ_2, QUIZ_3, QUIZ_4, DDARUNG, TITANIC

def print_menu():
    print('####################')
    print(f'로그인 : {LOGIN}')
    print(f'로그아웃 : {LOGOUT}')
    print(f'계산기 : {CALCULATOR}')
    print(f'성적표 : {GRADE}')
    print(f'따릉이 : {DDARUNG}')
    print(f'타이타닉 : {TITANIC}')
    print(f'퀴즈1 : {QUIZ_1}')
    print(f'퀴즈2 : {QUIZ_2}')
    print(f'퀴즈3 : {QUIZ_3}')
    print(f'퀴즈4 : {QUIZ_4}')
    menu = input('메뉴에서 URL을 카피해서 입력하시오\n')
    print('####################')
    return menu

def main():
    url = Url()
    while 1:
        menu = print_menu()
        if menu == f'{LOGOUT}':
            break
        else : url.router(menu)
                         
            
if __name__ == '__main__' :
    main()
    

'''
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService
from app.services.user import UserService
from app.services.grade import GradeService
from app.services.quiz import PandasQuiz

def print_menu():
    print("0. 전체프로그램 종료")
    print("1. 계산기 프로그램")
    print("2. 로그인 프로그램") # 입력받은 아이디와 비번 콘솔에 출력하기
    print("3. 성적표 프로그램")
    print("4. 판다스 퀴즈풀기")
    menu = input('메뉴 선택')
    return menu

def main():
    
    while 1:
        menu = print_menu()
        if menu == '0':
            print('전체 프로그램을 종료합니다.')
            break
        elif menu == '1':
            calculatorService = CalculatorService()
            first = int(input('첫번째 값 입력 : '))
            second = int(input('두번째 값 입력 : '))
            calculatorService.calculate(first, second)
        elif menu == '2':
            userService = UserService()
            id = input('ID : ')
            password = input('PASSWORD : ')
            userService.user(id, password)
        elif menu == '3':
            gradeService = GradeService()
            name = input('이름 : ')
            korean = int(input('국어 : '))
            english = int(input('영어 : '))
            math = int(input('수학 : '))
            grade = gradeService.get_grade(name, korean, english, math)
            print(f'이름: {name}, 학점: {grade}')
        elif menu == '4':
            quiz = PandasQuiz()
            while 1:
                quiz_number = input('퀴즈번호 선택. 종료는 0 : ')
                if quiz_number == '0':
                    break
                elif quiz_number == '1':
                    quiz.quiz_01()
                elif quiz_number == '2':
                    quiz.quiz_02()
                elif quiz_number == '3':
                    quiz.quiz_03()
                elif quiz_number == '4':
                    quiz.quiz_04()


if __name__ == '__main__':
    main()
'''