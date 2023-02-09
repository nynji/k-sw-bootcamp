import random
## 함수 선언 부분 ##
def quickSort(ary):
    global count
    count=count+1
    n = len(ary)
    if n <= 1:  # 정렬할 리스트의 개수가 1개 이하면
        return ary

    pivot = ary[n // 2]  # 기준값을 중간값으로 지정
    leftAry, rightAry = [], []

    for num in ary:
        if num > pivot:
            leftAry.append(num)
        elif num < pivot:
            rightAry.append(num)

    return quickSort(leftAry) + [pivot] + quickSort(rightAry)

count = 0
## 전역 변수 선언 부분 ##
dataAry = [random.randint(1, 200) for _ in range(20)]

## 메인 코드 부분 ##
print('정렬 전 -->', dataAry)
dataAry = quickSort(dataAry)
print('정렬 후 -->', dataAry)
print(f'{count}회로 정렬 완료')
