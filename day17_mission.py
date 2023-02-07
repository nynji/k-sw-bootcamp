import random


class treenode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def is_queue_full():
    global SIZE, front, rear, queue
    if rear != SIZE-1:
        return False
    if rear == SIZE-1 and front == -1:
        return True
    else:
        for i in range(front+1, SIZE):
            queue[i-1]=queue[i]
            queue[i]=None
        front -= 1
        rear -= 1
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
    rear+=1
    queue[rear]=data

def de_queue():
    global SIZE, front, rear, queue
    if is_queue_empty():
        print('empty')
        return
    front+=1
    data = queue[front]
    queue[front]=None
    return data

def peek():
    if is_queue_empty():
        print('empty')
        return
    return queue[front+1]



front = rear = -1
SIZE = 5
queue=['정국', '뷔','지민','진','슈가']

if __name__ == '__main__':
    random.shuffle(queue)
    print(f'대기 줄 상태 : {queue}')
    for data in queue:
        en_queue(data)
    for i in range(SIZE):
        print(f'{de_queue()}님 식당에 들어감')
        is_queue_full()
        rear +=1
        print(f'대기 줄 상태 : {queue}')

    print('식당 영업 종료')

