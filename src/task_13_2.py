# Создать класс  .АтрибутыЖ количество страниц, год издания, автор, цена.
# Добавить валидацию в конструкторе на ввод корректных данных.
# Создать иерархию ошибок
#

class Book:

    def __init__(self, side, year):
        if side < 0:
            raise Exception
        self.side = side
        if year > 2019:
            raise Exception
        self.year = year


def main():
    try:
        book_1 = Book(250, 2019)

    except Exception:
        print('something is wrong !!!!')

    print('End program')
    # print(book_1.side, book_1.year)


if __name__ == '__main__':
    main()
