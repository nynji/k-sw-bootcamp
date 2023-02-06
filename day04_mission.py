#연습문제 8.1
e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
print(e2f)

#8.2
print(e2f['walrus'])

#8.3
# f2e=list(e2f.items())
# print(f2e) 오답
f2e={}
for english, french in e2f.items():
    f2e[french]=english
print(f2e)
#items()가 key, value 두 개로 이루어져 있음 k,v의 명을 english, french로 내가 정한거임


#8.4 ??
# e2f_keys=list(e2f.keys())
# print(e2f_keys[0])
print(f2e['chien'])

#8.5
e2f_keys=list(e2f.keys())
print(e2f_keys)

#8.6
life={'animals':{'cats':'Henri', 'octopi':'Grumpy', 'emus':'Lucy'}, 'plants':' ' , 'other':'' }

#8.7
print(f'life 최상위 키 {list(life.keys())}')

#8.8
print(f"life['animals']으 모든 키 {list(life['animals'].keys())}")

#8.9
print(f"life['animals']['cats']의 모든 값 {(life['animals']['cats'])}")

#8.10
squares={i:i*i for i in range(10)}
print(squares)
