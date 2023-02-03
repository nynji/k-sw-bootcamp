katok = [['피카츄', 200], ['파이리', 150], ['꼬부기', 90],['어니부기', 30],['나룸퍼프', 15]]


def find_insert_data(friend, num):
    for i in range(len(katok)):
        if katok[i][1]<=num:
            position = i
            insert_data(position, friend, num)
            break

def insert_data(position, friend, num):
    katok.append(None)
    for i in range(len(katok), position, -1):
        katok[i-1]=katok[i-2]

    print(position)
    katok[position]=[friend, num]


if __name__ == "__main__":
    friend = input("추가할 포켓몬 --> ")
    num = int(input("체력 --> "))
    find_insert_data(friend, num)
    print(katok)
