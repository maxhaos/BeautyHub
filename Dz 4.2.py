# Вхідний масив
arr = [0, 1, 7, 2, 4, 8, 5, 6]

# Якщо масив порожній, результат - 0
if not arr:
    result = 0
else:
    # Знаходимо суму елементів із парними індексами
    sum_of_even_indices = sum(arr[::2])

    # Перемножуємо суму на останній елемент масиву
    result = sum_of_even_indices * arr[-1]

# Виводимо результат
print(result)