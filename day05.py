#함수의 매개변수로 함수 이름 사용 가능
def inha():
    """
    숫자 출력 함수
    :return:
    """
    print(60)
def call_function(f):
    """
    매개변수로 함수를 넘겨 받아 실행
    :param f: 매개변수가 함수
    :return:
    """
    f()  # 넘겨 받은 함수 실행
call_function(inha)

print(type(call_function))

#

def subtract(n1, n2):
    print(n1 - n2)


def run_func(f, arg1, arg2):
    """
    함수를 매개 변수로 받아 함수 안에서 해당 함수를 실행
    :param f: 첫번째 인수는 함수
    :param arg1: 정수 값
    :param arg2: 정수 값
    :return:
    """
    f(arg1, arg2)

run_func(subtract, 99, 88)

