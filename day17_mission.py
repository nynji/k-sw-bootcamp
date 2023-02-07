import random


class treenode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def is_queue_full():
    global SIZE, front, rear, queue
    if (rear+1)%SIZE == front:
        return True
    else:
        return False


def is_queue_empty():
    global SIZE, front, rear, queue
    if front == rear:
        return True
    else:
        return False

def en_queue(data):
    global SIZE, front, rear, queue
    if is_queue_full():
        print('full')
        return
    rear= (rear+1)%SIZE
    queue[rear]=data

def de_queue():
    global SIZE, front, rear, queue
    if is_queue_empty():
        print('empty')
        return
    front=(front+1)%SIZE
    data = queue[front]
    queue[front]=None
    return data

def peek():
    if is_queue_empty():
        print('empty')
        return
    return queue[(front+1)%SIZE]



front = rear = 0
SIZE = 6
queue=[None for _ in range(SIZE)]

if __name__ == '__main__':
    person = (('사용', 9), ('고장', 3), ('환불', 4), ('기타', 1))
    time = 0
    for i in range(SIZE-1):
        en_queue(person[random.randint(0,3)])
        time = time + queue[i+1][1]

        print(f'귀하의 대기 예상 시간은 {time}분 입니다')
        print(f'현재 대기 콜 --> {queue}\n')



