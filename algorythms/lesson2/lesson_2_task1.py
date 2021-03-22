"""
Написать программу, которая будет складывать, вычитать, умножать
или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не завершается, а запрашивает
новые данные для вычислений. Завершение программы должно выполняться
при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна
сообщать об ошибке и снова запрашивать знак операции. Также она
должна сообщать пользователю о невозможности деления на ноль, если
он ввел его в качестве делителя.
"""

while True:
    op = input("Введите один из операторов +,-,*,/ или 0 для выхода: ")

    if op == '0':
        break

    x = float(input("Введите число x: "))
    y = float(input("Введите число y: "))

    if op == '+':
        res = x + y
    elif op == '-':
        res = x - y
    elif op == '*':
        res = x * y
    elif op == '/':
        if y == 0:
            print("деление на ноль запрещено")
            continue

        res = x / y
    else:
        print("операция не поддерживается")
        continue

    print(f"{x} {op} {y} = {res}")