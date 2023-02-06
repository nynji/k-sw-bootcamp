#Lambda

#이전거 질문 해결
def calculate():
    x=1
    y=2
    temp=0
    def add_sub(n):
        nonlocal temp  #지역변수 아니다, 외부함수에 영향 끼침 (변경 가능)

        #x=11  #지역변수(local variable): 외부함수 (calculate)의 x와 다름, 변경 못함,
                #add_sub 내에서만 쓰임
        temp=temp + x+ n -y
        return temp
  #  print(x)

    return add_sub

c1 = calculate()
#calculate()의 리턴값이 add_sub이므로 c1 = add_sub()가 됨, 따라서 i값이 n에 들어감
for i in range(5):
    print(c1(i))  ##왜 i가 n으로 가는거임?

print(type(c1))
print(c1)

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


