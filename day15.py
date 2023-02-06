# katok = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]
# for i in range(len(katok)):0
#     pair = katok[i]
#     print(pair[1])
#

## 클래스와 함수 선언 부분 ##
class Node():
	def __init__ (self): #self, data로 해두고 self.data=data 로 해도 됨, 방식은 다양
		self.data = None
		self.link = None

	def __repr__(self):
		return f'포켓몬스터!'

def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.data, end = ' ')
    while current.link != None :
        current = current.link
        print(current.data, end = ' ')
    print()

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	node = Node()		# 첫 번째 노드
	node.data = dataArray[0]
	head = node
	memory.append(node)

	for data in dataArray[1:] :	# 두 번째 이후 노드
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		memory.append(node)

	print_nodes(head)
	print(memory)







# def insert_data(friend, count):
#
#
#
#
#
#  if __name__ == "__main__":
#     friend = input("추가할 친구 --> ")
#     count = int(input("카톡 횟수 --> "))
#     insert_data(friend, count)
#     print(katok[1])




# ## 함수 선언 부분 ##
# def print_poly(px, tx):
#     """
#     다항식을 포맷에 맞게 출력하는 함수
#     :param px: 계수를 원소로 가지고 있는 list
#     :param tx: 차수를 원소로 가지고 있는 list
#     :return: 다항식 문자열
#     """
#
#     poly_str = "P(x) = "
#
#     for i in range(len(px)):
#         term = tx[i]
#         coef = px[i]  # 계수
#
#         if coef >=0:
#
#             poly_str = poly_str + "+"
#
#         poly_str = poly_str + f'{coef}x^{term} '
#
#     return poly_str
#
#
# def calc_poly(x_val, px, tx):
#     """
#     다항식의 산술연산 계산
#     :param x_val: 계수를 원소로 가지고 있는 list
#     :param px: 다항식 계산 결과값 integer
#     :return:
#     """
#     retValue = 0
#     term = len(px) - 1  # 최고차항 숫자 = 배열길이-1
#
#     for i in range(len(px)):
#         coef = px[i]  # 계수
#         retValue += coef * x_val ** term
#         term -= 1
#
#     return retValue
#
#
# ## 전역 변수 선언 부분 ##
# px = [3, -4, 5]  # = 7x^3 -4x^2 +0x^1 +5x^0
# tx = [300,20,0]
#
# ## 메인 코드 부분 ##
# if __name__ == "__main__":
#
#     print(print_poly(px, tx))
#
#     x_value = int(input("X 값-->"))
#
#     px_value = calc_poly(x_value, px, tx)
#     print(px_value)


