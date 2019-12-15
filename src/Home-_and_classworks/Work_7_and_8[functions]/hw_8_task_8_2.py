# Даны три слова. Выяснить, является ли хоть одно из них палиндромом ("перевертышем"),
# т. е. таким, которое читается одинаково слева направо и справа налево. (Определить функцию,
# позволяющую распознавать слова палиндромы.)

def is_palindrom(*args):
    for word in args:
        print(f'{word} is palindrome' if word == word[::-1] or )


some_list = ['abc', 'aaa', 'def']
is_palindrom(*some_list)
