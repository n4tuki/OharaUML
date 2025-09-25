from app_logic import setFirstValue, setSecondValue, getAddition
from utils import render_template


def add_numbers(first: int, second: int):
    """2つの数値を保存し、加算結果をテンプレートに渡す"""
    setFirstValue(first)
    setSecondValue(second)
    result = getAddition()

    return render_template("boundaries/add_numbers_date.html", result=result)