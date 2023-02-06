#class

class Pokemon:
    def __init__(self, name, owner, skills):  #객체 생성 시 동작
        self.name = name
        self.owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 {name} 객체 생성됨")

    def info(self):
        print(f'{self.owner}의 포켓몬 {self.name}')
        for skill in self.skills:
            print(skill)


# p1=Pokemon('피카츄', '한지우', '50만 볼트/100만 볼트/번개')
# p2=Pokemon('꼬부기', '오바람', '고속스핀/거품/몸통박치기/하이드로펌프')

class Pikachu(Pokemon):  #상속 Imheritance : 부모 포켓몬 자식 피카츄
    pass

pi1 = Pikachu('피카츄','덴트','번개')
pi1.info()

# p2.info()
# p1.info()
# print(p2.skills)
# print(p1,p2)  #메모리 주소 다름 -> 다른 두 개의 객체

