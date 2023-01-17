#튜플 : ,
a='harry',
b=('harry',)
c=()  ##empty 상태의 tuple
d='harry','ron'  #packing
e=('hermione')  #얜 튜플 아님(string)
f=('harry','ron')  #packing
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print(b+d)
print(f[1])
x,y=format(print(y))  #unpacking