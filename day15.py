

def add_data(pokemon):
    pokemons.append(None)

    #pokemons[len(pokemons) - 1] = pokemon
    pokemons[-1] = pokemon


def delete_data(idx):
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    len_pokemons = len(pokemons)
    pokemons[idx] = None  # 데이터 삭제

    for i in range(idx + 1, len(pokemons)):
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None  # 배열의 맨 마지막 위치 삭제

    del (pokemons[len(pokemons) - 1])





if __name__ == "__main__":
    pokemons = ["피카츄", "라이츄", "파이리", "꼬부기", "이상해"]

    print(pokemons)
    #pokemons.insert(3, '어니부기')
    delete_data(1)
    print(pokemons)
    #pokemons.insert(6, '어니부기')
    delete_data(3)
    print(pokemons)



# pokemons = list()  # 빈 배열
#
#
# def add_data(pokemon):
#     pokemons.append(None)
#
#     #pokemons[len(pokemons) - 1] = pokemon
#     pokemons[-1] = pokemon
#
#
# add_data('피카츄')
# add_data('라이츄')
# add_data('파이리')
# add_data('꼬부기')
# add_data('이상해')
#
# print(pokemons)