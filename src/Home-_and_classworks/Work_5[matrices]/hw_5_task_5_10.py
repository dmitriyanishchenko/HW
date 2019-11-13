# В заданной строке расположить в обратном порядке все слова. Разделителями слов считаются пробелы

string = input('Enter the string --->')
string = string.split()
string = string[::-1]
print(' '.join(string))
