def normalize_numeric_input(value):
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)

    text = str(value).strip().replace(",", "").replace("$", "")
    if text == "":
        return None

    try:
        return float(text)
    except ValueError:
        return None


def is_close_answer(user_value, correct_value, tolerance=0.01):
    user_num = normalize_numeric_input(user_value)
    if user_num is None:
        return False
    return abs(user_num - float(correct_value)) <= tolerance