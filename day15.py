## 함수 선언 부분 ##
def print_poly(px):
    """
    다항식을 포맷에 맞게 출력하는 함수
    :param px: 계수를 원소로 가지고 있는 list
    :return: 다항식 문자열
    """
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1
    poly_str = "P(x) = "

    for i in range(len(px)):
        coef = px[i]  # 계수

        if coef > 0:
            if i!=0:
                poly_str += "+"
        if coef == 0:
            term-=1
            continue
        poly_str = poly_str + f' {coef}x^{term} '
        term = term - 1

    return poly_str


def calc_poly(x_val, px):
    """
    다항식의 산술연산 계산
    :param x_val: 계수를 원소로 가지고 있는 list
    :param px: 다항식 계산 결과값 integer
    :return:
    """
    retValue = 0
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(px)):
        coef = px[i]  # 계수
        retValue += coef * x_val ** term
        term -= 1

    return retValue


## 전역 변수 선언 부분 ##
px = [7, -4, 0, 6]  # = 7x^3 -4x^2 +0x^1 +5x^0

## 메인 코드 부분 ##
if __name__ == "__main__":

    print(print_poly(px))

    x_value = int(input("X 값-->"))

    px_value = calc_poly(x_value, px)
    print(px_value)


