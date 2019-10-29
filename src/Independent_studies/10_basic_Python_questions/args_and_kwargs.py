def test_args(farg, *args):
    print("Первый известный аргумент: ", farg)
    for arg in args:
        print("Один из оставшихся аргументов: ", arg)


test_args(1, "two", 3)


# Первый известный аргумент: 1
# Один из оставшихся аргументов: two
# Один из оставшихся аргументов: 3

def test_kwargs(farg, **kwargs):
    print("Первый известный аргумент: ", farg)
    for key in kwargs:
        print("Один из оставшихся аргументов: %s: %s" % (key, kwargs[key]))


test_kwargs(farg=1, myarg2="two", myarg3=3)
# Первый известный аргумент: 1
# Один из оставшихся аргументов: myarg2: two
# Один из оставшихся аргументов: myarg3: 3
