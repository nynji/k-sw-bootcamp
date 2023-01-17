#연습문제 7.4
things = ["mozzarella", "cinderella", "salmonela"]
things[-2]=things[-2].title()
print(things)
things[0]=things[0].upper()
print(things)
#things.remove("salmonela")
#pop은 리턴값이 있어서 먼저 할 수 없다. <<-졸아서 설명 못들은듯 다시 공부하기
print(f'{things.pop()}를 삭제 ')
print(things)

#for thing in things:
 #   print(thing[1].title())

