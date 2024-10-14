"""
Замена пропущенного элемента средним арифметическим
"""

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

none_index = numbers.index(None)
numbers[none_index] = 0
average_of_numbers = sum(numbers) / len(numbers)
numbers[none_index] = average_of_numbers


# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
