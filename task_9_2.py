old_dict = {'abc':5, 'dd':2, 'ccc':1}
new_dict = {key + key: value for key, value in old_dict.items()}
print(new_dict)

# result = ((lambda key + key  for key, value in kvargs.items())({'abc':5}))
# print(result)