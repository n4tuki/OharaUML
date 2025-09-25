from app_logic import setFirstValue, setSecondValue, getAddition
from utils import render_template, parse_post
from urllib.parse import parse_qs


def add_numbers(environ):
    method = environ["REQUEST_METHOD"]
    if method == "POST":
        data = parse_post(environ)
        first_value = data.get("first_value", [0])[0]
        second_value = data.get("second_value", [0])[0]

    setFirstValue(first_value)
    setSecondValue(second_value)
    addition = getAddition()

    return render_template("boundaries/add_numbers_data.html",
        first_value=first_value,
        second_value=second_value,
        addition=addition
    )