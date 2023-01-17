# #dictionary
#
# students = {'name': 'kiminha', 'age':23, 'eyes':[0.9, 1.1] }
# #for k in students.keys():
# #for k in students.values():
# for k, v in students.items():
#     #print(k)
#     print(f'{k} : {v}')
#
# print(f'이름은 {students["name"]}, 나이는 {students["age"]}', end=', ')
# print(f'시력은 좌: {students["eyes"][0]} 우: {students["eyes"][1]}')
# import random
#
# #안주 추천 (dictionary)
import random
alcohol_foods = {
    '맥주': ['카스', '테라'],
    '소주': '골뱅이소면',
    '와인': '치즈',
    '고량주': '짬뽕'
}
alcohol_list = list(alcohol_foods) #키 값만 추출 extract keys
food_list = [food for food in alcohol_foods.values()]
print(alcohol_list, food_list)
while True:
    alcohol = input(f'술을 선택하세요 1) {alcohol_list[0]} 2){alcohol_list[1]} 3){alcohol_list[2]} 4){alcohol_list[3]} 5) 계산 :  6) 아무거나 ')
    if alcohol == '5':
        print('끝')
        break
    elif alcohol == '1':
        print(f'안주 {alcohol_foods[alcohol_list[0]][random.randint(0,1)]}')
    elif alcohol == '2':
        print(f'안주 {alcohol_foods[alcohol_list[1]]}')
    elif alcohol == '3':
        print(f'안주 {alcohol_foods[alcohol_list[2]]}')
    elif alcohol == '4':
        print(f'안주 {alcohol_foods[alcohol_list[3]]}')
    elif alcohol == '6':
        #print(f'술 {alcohol_list[random.randint(0,3)]} 안주 {alcohol_foods[alcohol_list[random.randint(0,3)]]}')
        print(f'술 {random.choice(alcohol_list)}, 안주 {random.choice(food_list)}')
    else:
        print('1-5 선택')
        pass

print('\n\n\n')
import random

number = [random.randint(0,200) for i in range(10)]

print(number)