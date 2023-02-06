#6장 응용예제 "헨젤과 그레텔의 집으로 돌아가기"
import random


def is_full():
    global SIZE, stack, top
    if(top>=SIZE-1):
        return True
    else:
        return False

def is_empty():
    global SIZE, stack, top
    if(top==-1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if is_full():
        print("full")
    else:
        stack[top]=data
        top+=1

def pop():
    global SIZE, stack, top
    if is_empty():
        print("empty")
    else:
        data = stack[top]
        stack[top]=None
        top-=1
        return data


top= -1
SIZE = int(input("돌 개수 : "))
stack = [None for _ in range(SIZE)]

if __name__ == '__main__':
    stones = list()
    for i in range(SIZE):
        color=input("돌 색 : ")
        stones.append(color)

    random.shuffle(stones)

    for i in range(SIZE):
        push(stones[i])

    print('과자집 가는 길 : ', end='')
    for i in range(SIZE):
        print(stack[i] + ' ', end='')


    print('\n우리집 오는 길 : ', end='')
    for i in range(SIZE):
        print(pop() + ' ', end='')

