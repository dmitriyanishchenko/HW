#  В конец существующего текстовога файла
#  записать три новые строки текста


def main():
    with open('test_10_1.txt', 'a') as my_file:
        for i in range(3):
            my_file.write(input('enter line -->') + '\n')

    my_file.close()


if __name__ == '__main__':
    main()
