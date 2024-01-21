def main():
    # Запитуємо у користувача число
    number = input("Введіть 4-хзначне число: ")

    # Перевіряємо, чи число є цілим
    try:
        number = int(number)
    except ValueError:
        print("Ви ввели не ціле число.")
        return

    # Ділимо число на 1000, щоб отримати першу цифру
    перше_число = number // 1000

    # Ділимо число на 100, щоб отримати другу цифру
    друге_число = (number % 1000) // 100

    # Ділимо число на 10, щоб отримати третю цифру
    третє_число = (number % 100) // 10

    # Ділимо число на 1, щоб отримати четверту цифру
    четверте_число = number % 10

    # Виводимо цифри числа в стовпчик
    print(перше_число)
    print(друге_число)
    print(третє_число)
    print(четверте_число)

if __name__ == "__main__":
    main()