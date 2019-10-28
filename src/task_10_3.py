# Имеется текстовый файл. Все четные строки записать
# во второй файл, а нечетные - в третий файл.
# Порядок следования строк сохраняется


def main():
    with open('task_10_3_old.txt') as my_file:
        with open('task_10_3_even.txt', 'w') as even_lines:
            with open('task_10_3_not_even.txt', 'w') as not_even:

                while True:
                    lines = my_file.readlines()

                    if not lines:
                        break
                    s_line = len(lines)
                    print(s_line)
                    print(lines)
                    for i in range(1, s_line, 2):  # чет
                        even_lines.writelines('\n')
                        even_lines.writelines(lines[i])
                        print(lines[i])

                    for i in range(0, s_line, 2):  # нечет
                        not_even.writelines(lines[i])
                        not_even.writelines('\n')
                        print(lines[i])

            not_even.close()
        even_lines.close()
    my_file.close()


if __name__ == '__main__':
    main()
