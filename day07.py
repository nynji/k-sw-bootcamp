
class Pokemon:
    def __init__(self, owner, skills):  #객체 생성 시 동작
        # self.name = name
        self.owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 생성 : ", end=' ')

    def info(self):
        print(f'{self.owner}의 포켓몬이 사용 가능한 스킬')
        for skill in self.skills:
            print(skill)

    def attack(self, idx):  #공통으로 공격하니까 부모 클래스에, 단 각 특성은 자식클래스에서 오버라이드
        print(f'{self.skills[idx]} 공격 시전')


# p1=Pokemon('피카츄', '한지우', '50만 볼트/100만 볼트/번개')
# p2=Pokemon('꼬부기', '오바람', '고속스핀/거품/몸통박치기/하이드로펌프')

class Pikachu(Pokemon):  #상속 Imheritance : 부모 포켓몬 자식 피카츄
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "피카츄"
        print(f"{self.name}")

    def attack(self, idx):  #공통으로 공격하니까 부모 클래스에, 단 각 특성은 자식클래스에서 오버라이드
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격(전기) 시전')

class Ggoboogi(Pokemon):  #상속 Imheritance : 부모 포켓몬 자식 피카츄
    def __init__(self, owner, skills):
        super().__init__(owner, skills)  #super
        self.name = "꼬부기"
        print(f"{self.name}")

    def attack(self, idx):  # overide (부모클래스 메서드를 자식클래스에서 재정의)
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격(물) 시전')

    def swim(self):
        print(f'{self.name}가 수영합니다.')


p0 = Pokemon('아이리스','어떤공격')
p0.attack(0)  #얘는 부모 클래스의 attack만 사용 가능 (자식 클래스가 없으므로)
#p0.swim()  #꼬부기 클래스의 객체만 사용 가능

pi1 = Pikachu('한지우','번개/100만볼트')  #부모클래스 생성자 쓰고 그 후 자기 클래스 생성자 사용
#pi1.info()
ggo1= Ggoboogi('오바람','고속스핀/거품/몸통박치기')
#ggo1.info()
ggo1.attack(2)
ggo1.swim()
pi1.attack((1))


#print(ggo1.skills)

# pi1.info()