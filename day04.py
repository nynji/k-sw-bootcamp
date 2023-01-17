#list

# scores=('B+', 'A+', 'C+')
# print(scores[1], scores[2])
# temp=list(scores)
# temp[1]='C+'
# temp[2]='A+'
# scores=tuple(temp)
# print(scores[1], scores[2])

big_bang = ['GD','태양','TOP','대성','승리']
exo = ['백현','첸']
#big_bang.append('인하')  #append는 뒤에 추가
big_bang.insert(1, '인하')  #추가할 인덱스 -> 나머지 뒤로 밀림
print(big_bang*3)
exo.append(big_bang)  #append :리스트 안에 리스트[]가 들어감
# exo.extend(big_bang)  #extend :결합
# print(exo)
# print(exo[2][2])  #exo[2]에는 리스트가 있음. 내부 리스트의 [2]
# print(exo[3])
#
# exo[-8]='시우민'  #교체됨
print(exo)

#항목 삭제하기

#print(exo.pop()) #빅뱅 pop
print(exo[2].pop()) #승리 pop
print(exo)
print(exo[2].pop(-2))  #탑 pop
print(exo)

del exo[2][-1]  #대성 delete
print(exo)

exo[2].remove('인하')  #인하 remove /exo[2]까지 가서 지워야함/ (이름 두 개 일땐 앞에것만 지움)
print(exo)