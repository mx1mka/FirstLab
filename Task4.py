my_dict = {'a': 111, 'b': 122, 'c': 566, 'd': 405, 'e':21, 'f':266}
p_my_dict = my_dict
max_key = max(p_my_dict, key=p_my_dict.get)
print('1-й максимальный -', max_key)
p_my_dict.pop(max_key)
max_key = max(p_my_dict, key=p_my_dict.get)
print('2-й максимальный -', max_key)
p_my_dict.pop(max_key)
max_key = max(p_my_dict, key=p_my_dict.get)
print('3-й максимальный -', max_key)
