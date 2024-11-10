# Найти сумму произведений из списка словарей
import json

FILE = "input.json"


# TODO решите задачу
def task() -> float:
    with open(FILE) as file:
        data = json.load(file)
    return round(sum(dict_["score"] * dict_["weight"] for dict_ in data), 3)


print(task())
