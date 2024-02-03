my_dict_1 = {1: 1, 2: 2, 3: 3, 5: 5}
my_dict_2 = {11: 11, 2: 22, 4: 4, 5: 5}

#  Ключі, які є в обох словниках
common_keys = [key for key in my_dict_1.keys() if key in my_dict_2]

#  Ключі, які є у першому, але немає у другому словнику
unique_keys_first = [key for key in my_dict_1.keys() if key not in my_dict_2]

#  Новий словник для ключів, які є в першому, але немає в другому словнику
new_dict = {key: my_dict_1[key] for key in unique_keys_first}

#  Об'єднання двох словників
merged_dict = {}
for key, value in my_dict_1.items():
    if key in my_dict_2:
        merged_dict[key] = [value, my_dict_2[key]]
    else:
        merged_dict[key] = value

for key, value in my_dict_2.items():
    if key not in my_dict_1:
        merged_dict[key] = value

print("a) Ключі, які є в обох словниках:", common_keys)
print("б) Ключі, які є у першому, але немає у другому словнику:", unique_keys_first)
print("в) Новий словник для ключів, які є в першому, але немає в другому словнику:", new_dict)
print("г) Об'єднаний словник:", merged_dict)