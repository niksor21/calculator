a = int(input('Введите первое целое число: '))
action = str(input('Выберите арифметическое действие (+ - * /): '))
b = int(input('Введите второе целое число: '))
if action == '+':
    print(a+b)
elif action == '-':
    print(a-b)
elif action == '*':
    print(a*b)
elif action == '/':
    print(a/b)