import traceback


def print_term(degree, factor):
    """
    :param degree: int, 항의 계수
    :param factor: int, 항의 차수
    :return: str
    """
    return '7x^2'    # if degree == 2 and factor == 7


def print_equation(terms):
    """
    :param terms: dict (key=degree, value=factor)
    :return: str
    """
    return '1 + 5x^2'    # if terms == {0: 1, 2: 5}


def parse_term(term_str):
    """
    :param term_str: str
    :return: 2-tuple (degree: int, factor: int)
    """
    return 2, 5    # if term_str == '5x^2'


def parse_equation(equation):
    """
    :param equation: str
    :return: dict (key=degree, value=factor)
    """
    return {1: -7, 2: 3}    # if equation == '-7x + 3x^2'


def d_dx_as_terms(terms):
    """
    :param terms: dict (key=degree, value=factor)
    :return: terms와 동일한 형식이되,
    그 값이 terms의 미분인 것
    """
    return {0: 3, 2: 6}    # if terms == {1: 3, 3: 2}


def d_dx(equation):
    """
    :param equation: str
    :return: str
    """
    return '2 + 6x'    # if equation == '2x + 3x^2'


def integral_as_terms(terms, constant):
    """
    :param terms: dict (key=degree, value=factor)
    :param constant: int
    :return: terms와 동일한 형식이되,
    그 값이 terms의 적분인 것
    """
    return {0: 6, 1: -2, 2: 5}    # if terms == {0: -2, 1: 10} and constant == 6


def integral(equation, constant):
    """
    :param equation: str
    :param constant: str
    """
    return '5 + 3x + 5x^5'    # if equation == '3 + 25x^4' and constant == 5


def compute_as_terms(terms, x):
    """
    :param terms: str
    :param constant: int
    :return: int
    """
    return 5    # if terms == {0: 5, 1: -3, 2: 1} and x = 3


def compute(equation, x):
    """
    :param equation: str
    :param x: int
    :return: str
    """
    return '5'    # if equation == '5 + -3x + x^2' and x == 3


def solve_query(line):
    """
    :param line: str
    :return: str
    """
    try:
        # 이 안에 코드를 작성해주세요!
        # solve_query() 함수에서 실행 도중 불가피한 오류가 발생하더라도,
        # 다음 쿼리를 받아들일 수 있게 도와줍니다.
        return '2x'    # if line == 'D,x^2'
    except:
        traceback.print_exc()
        return ''


def solve(input_path, output_path):
    """
    :param input_path: str
    :param output_path: str
    :return: None (파일 입출력으로 문제 해결)
    """
    return
