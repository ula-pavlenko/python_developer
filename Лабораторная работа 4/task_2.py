# Конвертер из CSV в JSON формат

# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as input_:  # TODO считать содержимое csv файла
        reader = csv.DictReader(input_)
        data = list(reader)
        with open(OUTPUT_FILENAME, "w") as output_:
            json.dump(data, output_, indent=4)  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
