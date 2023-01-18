# function - *
#놀이공원 ver.1
# import random
# def calculate_fee(args)->list:  #*args일 땐 튜플형식이라 리스트로 입력 받고 정수와 비교할 수 없다.
#     ## ->list : 오류 안남, return 형식 보여주는 것
#     """
#     놀이공원 요금 계산 프로그램
#     :param args:ages in list
#     :return:[전체 인원 수, 어른 수, 아이 수, 총 입장료]
#     """
#     total=0
#     adults=0
#     kids=0
#     for age in args:
#         if 19<=age: #adult
#             total=total+10000
#             adults+=1
#         else:
#             total=total+3000
#             kids+=1
#
#     return [len(args), adults, kids, total]
#
# # print(calculate_fee(20,20,25))
# # print(calculate_fee(45,43,10,7))
#
# no_of_visitor = int(input(('몇 분이세요? ')))
# ages = [random.randint(1, 60) for age in range(no_of_visitor)]
# print(ages)
# print(calculate_fee(ages))
# #
# # 5q분 방문하셨고 어른 2명 아이 3명 총 요금은 ~입니다.
# result = calculate_fee(ages)
# print(f'{result[0]}명, 어른{result[1]}명, 아이{result[2]}명, 총 요금{result[-1]}원')

#ver.2 dictionary로 리턴
import random
def calculate_fee(args)->dict:  #*args일 땐 튜플형식이라 리스트로 입력 받고 정수와 비교할 수 없다.
    ## ->list : 오류 안남, return 형식 보여주는 것
    """
    놀이공원 요금 계산 프로그램
    :param args:ages in list
    :return:[전체 인원 수, 어른 수, 아이 수, 총 입장료]
    """
    total=0
    adults=0
    kids=0
    for age in args:
        if 19<=age: #adult
            total=total+10000
            adults+=1
        else:
            total=total+3000
            kids+=1

    return {'no_of_people': len(args), 'no_of_adult': adults, 'no_of_kid':kids, 'total_fee': total}
# print(calculate_fee(20,20,25))
# print(calculate_fee(45,43,10,7))

no_of_visitor = int(input(('몇 분이세요? ')))
ages = [random.randint(1, 60) for age in range(no_of_visitor)]
print(ages)
print(calculate_fee(ages))
#
# 5q분 방문하셨고 어른 2명 아이 3명 총 요금은 ~입니다.
result = calculate_fee(ages)
print(f"전체 {result['no_of_people']}명, 어른{result['no_of_adult']}명, 아이{result['no_of_kid']}명, 총 요금{result['total_fee']}원")