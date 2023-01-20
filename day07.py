#믹스인

# class PrettyMixin():
#     def dump(self):
#         import pprint
#         pprint.pprint(vars(self))
# class Thing(PrettyMixin):
#     pass
#
# t=Thing()
# t.name="Nyarlathotep"
# t.feature="ichor"
# t.age="eldritch"
# t.dump()

class Duck():
    color='white'
    def __init__(self, input_name):
        self.__hidden_name=input_name

    @staticmethod  #이거 하면 괄호에 self 안들어감
    def test():
        print('정적')

    @classmethod  #ㅇ거하면 cls가 들어감
    def ace(cls):
        print('클래스')

        ## static, class method는 클래스의 / 딴건 객체의 -> self

    @property
    def name(self):
        print('inside the getter')
        return self.__hidden_name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__hidden_name = input_name

    #name = property(get_name, set_name)

    # def get_name(self):
    #     print('inside the getter')
    #     return self.hidden_name
    # def set_name(self, input_name):
    #     print('inside the setter')
    #     self.hidden_name=input_name
    # name=property(get_name, set_name)





don=Duck('Donald')
print(Duck.ace(), Duck.test(), don.ace(), don.test())  #객체 없이 사용 가능한 것들


print(don.color, Duck.color)
don.color='blue'
print(don.color, Duck.color)  #객체만 색상 바뀜
Duck.color = 'green'  #클래스 속성 변경 (클래스 변수 값 변경)
print(don.color, Duck.color)   #Duck도 바뀜
d2= Duck('Induk')
print(don.color, Duck.color, d2.color)


#print(don.get_name())
print(don.name)
#don.set_name('Donna')
don.name='Donna'
#print(don.get_name())
don.__hidden_name='Kiminha'
print(don.name)
# print(don.get_name)
