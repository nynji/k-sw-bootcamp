#연습문제 10.1
class Thing():
    pass

example = Thing()
print(Thing)
print(example)  #두 출력값은 다르다

#10.2
class Thing2():
    letters='abc'

print(Thing2.letters)

#10.3
class Thing3():
    def __init__(self):
        self.letters = 'xyz'

example2 = Thing3()
print(example2.letters)

#10.4
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(f'{self.name}, {self.symbol}, {self.number}')

example3 = Element('Hydrogen', 'H', 1)
example3.dump()

#10.5/10.6
el_dict = {'name':'Hydrogen', 'symbol':'H', 'number':1}
hydrogen= Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
hydrogen.dump()

