input_list = [0, 1, 0, 12, 3, 5, 6, 0, 3, 0, 4]

# Розділити список на дві частини: ненульові та нульові елементи
non_zero_elements = [i for i in input_list if i != 0]
zero_elements = [i for i in input_list if i == 0]

# Злити обидві частини, де ненульові елементи йдуть спочатку
result = non_zero_elements + zero_elements

# Вивести результат
print(result)