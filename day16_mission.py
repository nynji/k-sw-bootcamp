#5장 응용예제 '현재 위치부터 가까운 편의점 관리하기'
import math
import random

class Node():
    def __init__(self, data):
        self.data = data
        self.link = None

def sort_dis(stores):
    global head, pre, current
    dis = math.sqrt(stores[1] * stores[1] + stores[2] * stores[2])
    node = Node((stores[0], dis))
    # node.link = head
    if head==None:
        head = node
        last = node
        node.link = head
        return

    if head.data[1] >= node.data[1]:
        node.link = head
        last = head #임시
        while last.link != head:
            last = last.link
        # last가 진짜 last
        last.link = node
        head = node
        return
    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data[1] >= node.data[1]:
            node.link = current
            pre.link = node
            return

    # 끝까찌 왔을 떄
    # 원형을 만들어주는 코드
    # current : last
    current.link = node
    node.link = head

    return


def print_nodes(start):
    global current, head, pre
    current = start
    print(f'{current.data[0]}편의점, 거리 : {current.data[1]}')
    while current.link != start:
        current = current.link
        print(f'{current.data[0]}편의점, 거리 : {current.data[1]}')

head, pre, current = None, None, None

if __name__ == '__main__':
    for i in range(10):
        x = random.randint(1, 100)
        y = random.randint(1, 100)

        name = chr(ord('A') + i)
        stores = (name, x, y)
        sort_dis(stores)

    print_nodes(head)


