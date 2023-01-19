#예외


# def div_calc(a, b):
#     """
#     나누기 함수
#     :param a: 분자
#     :param b: 분모
#     :return: 계산결과
#     """
#     return a / b
#
# print(div_calc(15, 3))


try:
    raise Exception("쉬는 시간")
    expr = input('분자 분모 입력 : ').split()
    print(int(expr[0])/int(expr[1]))
#vALUEeRROR
#ZeroDivisionError
except ValueError:
    print('숫자 입력')
except ZeroDivisionError as err:  #as err 하면 시스템 오류 문구 출력 가능
    print(err)
    print('분모에 0')
except IndexError as err:
    print('입력 값 범위')
except Exception as err:
    print(err)
    print('무언가 문제가 발생했습니다!')

else:  #예외 발생하지 않았을 때
    print('프로그램 정상 종료', end=' ')
finally:  #예외 발생 여부와 상관 없이 무조건 실행
    print('종료')