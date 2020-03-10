# Имеется два текстовых файла с одинаковым числом строк.
# Выяснить, совпадают ли строки.
# Если нет  - то получить номер первой строки, в которой
# эти файлы отличаются друг от друга.


def main():
    with open('test_10_4_1.txt') as f1:
        with open('test_10_4_2.txt') as f2:
            count = 1
            while True:
                line_f1 = f1.readline()
                line_f2 = f2.readline()

                if not line_f1:
                    break
                if line_f1 != line_f2:
                    print(f'line {count}')
                    break
                count += 1
        f2.close()
    f1.close()


if __name__ == '__main__':
    main()
