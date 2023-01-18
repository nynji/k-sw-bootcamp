#Closures

def calculate():
    x=1
    y=2
    temp=0
    def add_sub(n):
        nonlocal temp  #지역변수 아니다, 외부함수에 영향 끼침 (변경 가능)

        #x=11  #지역변수(local variable): 외부함수 (calculate)의 x와 다름, 변경 못함,
                #add_sub 내에서만 쓰임
        temp=temp + x+ n -y
        return temp
  #  print(x)

    return add_sub

c1 = calculate()
for i in range(5):
    print(c1(i))  ##왜 i가 n으로 가는거임?

print(type(c1))
print(c1)

