

def even_func(*args):
    for arg in args:
        print(arg)
        if  arg%2:
            continue
        else:
            def enum_func(*args):
                list_num = [args]
                return list_num
    return list_num
res = even_func(1, 3, 4, 6)
print(res)
