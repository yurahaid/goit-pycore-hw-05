import re


def generator_numbers(text: str):
    """
    Parse number from text
    """
    for number in re.finditer(r"((\d+)(\.\d*)*)", text):
        yield float(number[0])


def sum_profit(text: str, func: callable) -> float:
    """
    Calc sum all numbers extracted from callback
    """
    sum = 0
    for num in func(text):
        sum = sum + num

    return sum
