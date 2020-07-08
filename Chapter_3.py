def collatz(Number):
    if Number % 2 == 0:
        return Number // 2
    else:
        return 3 * Number + 1


i = 0
c = int(input("Введите любое число : "))

while c != 1:
    i += 1
    c = collatz(c)
    print(f"{i}-й шаг число {c}")

print("Цикл закончился")