#generator

def a():  #generator
    yield 1  #값 반환해도 안끝남
    yield 2
    yield 3

def b():  #normal function
    return 1  #리턴하면 끝남
    return 2
    return 3

print(a(),b())
for i in a():
    print(i)