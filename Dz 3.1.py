while True:
    try:
        num1 = int(input("Введіть перше число: "))
        operator = input("Введіть операцію (+, -, *, /): ")
        num2 = int(input("Введіть друге число: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num1 != 0:
                result = num1 / num2
            else:
                print("Помилка: Ділення на нуль недопустиме.")
                continue
            if num2 != 0:
                result = num1 / num2
            else:
                print("Помилка: Ділення на нуль недопустиме.")
                continue
        else:
            print("Помилка: Невідома операція.")
            continue

        print("Результат:", result)

    except ValueError:
        print("Помилка: Введені дані мають бути числами.")