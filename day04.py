# #list

import copy
a=[1,2,[5,-9]]
b=copy.deepcopy(a)
a[2][1]=7 #mutable, deepcopy(별도의 메모리 공간 할당, 각방. 명확히 복제본을 분리. 단, 메모리 많이 든다)
print(a,b)




# a=[1,2,[5,-9]]  #mutable, b/c/d affects
# b=a.copy()
# c=list(a)
# d=a[:]
# a[2][1]=7
# print(a,b,c,d)  ##이떈 list라 불변 아님, 따라서 a만 바꿔도 b,c,d에서도 바뀜 -> deepcopy라고 하기 어려움


# a=[1,2,3]
# b=a.copy()
# c=list(a)
# d=a[:]
# a[2]='sw'   #immutable
# print(a,b,c,d)  #얜 안바뀜



# mixed = [6, 4, 5, 'A', 7, '트와이스', 'B', 'b','마마무']
# mixed.sort()
# print(mixed)
# mixed.sort(reverse==Tu=rue)
# lfj gu[primes;p01;1
#


# primes = [2, 19, 3.0, 5, 7, 11]
# primes_sorted = sorted(primes)
# print(primes)
# print(primes_sorted)
# primes.sort()
# print(primes)