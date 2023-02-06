# #연습문제 10.1
# class Thing():
#     pass
#
# print(Thing)
#
# example = Thing()
# print(example)  #출력값이 다르다
#
# #연습문제 10.2
# class Thing2():
#     letters = 'abc'
#
# print(Thing2.letters)
#
# #10.3
# # class Thing3():
# #     pass
# # instance=Thing3
# # instance.letters='xyz'
# # print(instance.letters)  #뭔소리지?
#
# class Thing3():
#     def __init__(self):
#         self.letters = 'xyz'  #letters 속성은 클래스x, 클래스로부터 생성된 객체에 해당함
#
# #10.4
# class Element():
#     def __init__(self, name, symbol, number):
#         self.private_name = name
#         self.private_symbol =symbol
#         self.private_number=number
#
#     def dump(self):
#         print(f'name {self.name}, symbol {self.symbol}, number {self.number}')
#
#     def get
#
# hh = Element('Hydrogen', 'H', '1')
#
#
# #10.5
# el_dict = {'name':'Hydrogen', 'symbol':'H', 'number':1}
# hydrogen = Element(**el_dict)
# print(hydrogen.name)
#
# #10.6
# hydrogen.dump()
#
# #10.7  뭔소리지
# print(hydrogen)

#10.8

#프로퍼티
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2*self.radius

c=Circle(5)
print(c. diameter)

def mult_two(a: int, b: int) -> int:
    # your code here
    a=int(input())
    b=int(input())
    print(a*b)

    return 0


print("Example")
print(mult_two(1, 2))
