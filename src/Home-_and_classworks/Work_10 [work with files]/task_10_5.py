# Создать матрицу случайных чисел и сохранить её в   файл.
# После прочесть ееБ обнулить все четные элементы и сохранить в другой файл


from random import randint
import json


def main():
    with open('test_10_5.json', 'w') as my_file:
        n = 3
        matrix = []

        for i in range(n):
            row = []
            for j in range(n):
                elem = str(randint(0, 9))
                row.append(elem)
            print(row)
            matrix.append(row)
            my_file.writelines(row)
            my_file.write('\n')

    my_file.close()

    with open('test_10_5.json') as my_file:
        with open('test_10_5_res.json', 'w') as new_my_file:
            for i in range(n):
                line = str(my_file.readline().strip())
                new_line = list(line)
                new_line2 = []
                for elem in new_line:
                    if not (int(elem)) % 2:
                        elem = '0'

                    new_line2.append(elem)

                new_my_file.writelines(new_line2)
                new_my_file.write('\n')
                print(new_line2)
        new_my_file.close()
    my_file.close()


if __name__ == '__main__':
    main()
