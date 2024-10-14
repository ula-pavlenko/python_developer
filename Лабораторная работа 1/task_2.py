"""
Расчет количества книг на дискете
"""

# TODO Найдите количество книг, которое можно разместить на дискете
floppy_capacity = 1.44 * 1024 ** 2
number_of_pages = 100
number_of_strings = 50
number_of_symbols = 25
book_capacity = number_of_pages * number_of_strings * number_of_symbols * 4
books_count = int(floppy_capacity // book_capacity)

print("Количество книг, помещающихся на дискету:", books_count)
