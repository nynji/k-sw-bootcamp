# ch11 insert sort
import random

def find_idx(ary, dat):
    findidx = -1
    for i in range(0, len(ary)):
        if ary[i][1] > dat:
            findidx = i
            break
    if findidx == -1:
        return len(ary)
    else:
        return findidx


Array = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]
after = []
print(f'정렬 전 --> {Array}')

for i in range(6):
    data = Array[i][1]
    after.insert(find_idx(after, data), Array[i])

print(f'정렬 후 --> {after}')

for i in range(3):
    print(f'{after[i][0]} : {after[5-i][0]}')

