# #데코레이터
#
#
# #decorator
# def document_info(func):
#     def new_function(*args, **kwargs):
#         print('실행 중인 함수: ', func.__name__)
#         print('위치 기반 인수: ', args)
#         print('키워드 기반 인수들: ', kwargs)
#         result = func(*args, **kwargs)
#         print('실행 결과: ', result)
#         return result
#     return new_function
#
# @document_info
# def sub_int(x, y):
#     return x-y
#
# @document_info
# def squares(n):
#     return n*n
#
#
# print(sub_int(7,3))
# print(squares(5))
# # info_sub_int = document_info(sub_int)
# # r = info_sub_int(7,3)
# # print(r)

g=1  #<-전역변수, 얘 있으면 함수 밖에서 g를 알 수 있음.
def print_global():
    #g= 1  #지역변수
    print(g)

def change_print_global():
    global g #<-전역변수 됨
    print(g)
    g = 2
    print(g)

change_print_global()
print_global()
print(g)  #여기서 g를 알 수 없음
print(globals())
print(__name__)