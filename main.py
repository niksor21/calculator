a = float(input('Введите первое число: '))
action = str(input('Выберите арифметическое действие (+ - * /): '))
b = float(input('Введите второе число: '))
if action == '+':
    result = (a+b)
    if result % 1 == 0:
        print(int(result))
    else:
        print(float(result))
elif action == '-':
    result = (a-b)
    if result % 1 == 0:
        print(int(result))
    else:
        print(float(result))
elif action == '*':
    result = (a*b)
    if result % 1 == 0:
        print(int(result))
    else:
        print(float(result))
elif action == '/':
    result = (a/b)
    if result % 1 == 0:
        print(int(result))
    else:
        print(float(result))