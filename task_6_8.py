# В заданой строке расположить в обратном порядке все слова.
# Разделителем  слов считаются пробелы.
string = input('enter the string')
string = string.split()

i = 0
k = int(len(string))
j = k -1
new_string = []
while i < k and j >= 0:
    new_string.append(string[j])
    i += 1
    j -= 1

result = ' '.join(new_string)
print(result)
