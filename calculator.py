print("\nЭто программа калькулятор!!!")
a = input("Введите первое число: ")
b = input("Введите второе число: ")
op = input("Какую операцию хотите сделать? (+, -, *, /): ")
if op == "*":
    e = int(a) * int(b)
    print(f"Результат: {e}")
elif op == "-":
    f = int(a) - int(b)
    print(f"Результат: {f}")
elif op == "/":
    g = int(a) / int(b)
    print(f"Результат: {int(g)}")
elif op == "+":
    c = int(a) + int(b)
    print(f"Результат: {c}")
else:
    print("Нет такой операции!")