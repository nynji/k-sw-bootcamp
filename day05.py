#Lambda

# 그냥 하면 다음과 같다(함수를 매개변수로 사용)
# 함수 만들어두고 여기저기 쓸 땐 이 방법이 좋지만 그렇지 않을 경우 람다가 간단
# import random
#
# def process(no_lists, f):
#     for no in no_lists:
#         print(f(no))
#
# def squares(n):
#     """
#     제곱 함수
#     :param n: integer
#     :return: integer
#     """
#     return n * n
#
# numbers = [random.randint(1, 100) for i in range(5)]
# print(numbers)
#
# process(numbers, squares)


#람다함수 사용
import random

def process(no_lists, f):
    for no in no_lists:
        print(f(no))

numbers = [random.randint(1, 100) for i in range(5)]
print(numbers)

process(numbers, lambda x: x*x)


