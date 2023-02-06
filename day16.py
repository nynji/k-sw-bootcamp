## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def print_nodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()

def insert_nodes(findData, insertData) :
	global memory, head, current, pre

	if head.data == findData :      # 첫 번째 노드 삽입
		node = Node()
		node.data = insertData
		node.link = head
		head = node
		return

	current = head
	while current.link != None :    # 중간 노드 삽입
		pre = current
		current = current.link
		if current.data == findData :
			node = Node()
			node.data = insertData
			node.link = current
			pre.link = node
			return

	node = Node()                   # 마지막 노드 삽입
	node.data = insertData
	current.link = node

def delete_nodes(delete_data):
    global memory, head, current, pre

    if head.data == delete_data:
        print("첫번째 노드가 삭제됨")
        current = head
        head = head.link
        del current
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == delete_data:
            print('중간 노드 삭제됨')
            pre.link = current.link
            del current
            return

    print('삭제할 노드 찾지 못함')
    #삭제할 데이터를 못찾은 경우 함수 종료


def find_nodes(find_data):
	global memory, head, current, pre

	current = head
	if current.data == find_data:
		return current

	while current.link != None:
		current = current.link
		if current.data == find_data:
			return current

	return Node()

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]

## 메인 코드 부분 ##
if __name__ == "__main__" :
    node = Node()  # 첫 번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:  # 두 번째 노드부터
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)


print_nodes(head)
insert_nodes("피카츄", "잠만보")

print_nodes(head)
insert_nodes("파이리", "어니부기")

print_nodes(head)
insert_nodes("ㄴㅇㄹ", "거북왕")
print_nodes(head)

delete_nodes("잠만보")
print_nodes(head)

print(find_nodes("파이리").data)
print(find_nodes("rkd").data)

