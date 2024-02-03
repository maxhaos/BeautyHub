import string
import keyword

# Отримання рядка від користувача
user_input = input("Введіть ім'я змінної: ")

# Перевірка на початок з цифри
if user_input[0].isdigit():
    print(False)
else:
    # Перевірка на складання тільки з цифр
    if user_input.isdigit():
        print(False)
    else:
        # Перевірка на наявність великих літер, пробілів і знаків пунктуації (окрім нижнього підкреслення)
        if any(char.isupper() for char in user_input):
            print(False)
        else:
            allowed_characters = string.ascii_letters + string.digits + '_'
            if any(char not in allowed_characters for char in user_input):
                print(False)
            else:
                # Перевірка на наявність в списку ключових слів
                if user_input.lower() in keyword.kwlist:
                    print(False)
                else:
                    # Виведення True, якщо всі перевірки пройдено
                    print(True)