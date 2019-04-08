# Даны три слова. Выяснить, является ли хоть одно из них палиндромом("перевертышем"),
# т.е. таким, которое читается одинаково слева направо и справа налево. (Определить функцию,
# позволяющую распознавать слова палиндромы)

def reverse(s):
    return s[::-1]


def isPalindrome(s):
    rev = reverse(s)
    if s == rev:
        return True
    return False


s = ['abba', 'otto', 'mama']
print(s)

for word in s:
    ans = isPalindrome(word)
    if ans == 1:
        print(f'{word} Yes')
    else:
        print(f'{word} No')
