# Приклад списку
my_list = [1,5,6,7]

# Перевірка, чи список не порожній або не має одного елемента
if len(my_list) > 0:
    # Переміщення останнього елемента на початок
    last_element = my_list.pop()
    my_list.insert ( 0 , last_element)

# Виведення результату
print(my_list)