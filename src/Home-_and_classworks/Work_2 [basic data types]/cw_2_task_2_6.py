# 1. Создать список из двух элементов.
# 2. Создать кортеж из двух элементов.
# 3. Создать словарь с одной парой. Ключ - кортеж, значение - список
# 4. Создать словарь с одной парой. Ключ - список, значение - кортеж

some_listing = ['elem_1', 'elem_2']
some_tuple = ('elem_1', 'elem_2')
some_dict_1 = {('teacher_age', 'student_age'): [25, 18]}
some_dict_2 = {"['teacher_age', 'student_age']": (25, 18)}
print(f'1. listing:      {some_listing}')
print(f'2. tuple:        {some_tuple}')
print(f'3. dictionary 1: {some_dict_1}')
print(f'4. dictionary 2: {some_dict_2}')
