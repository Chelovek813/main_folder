a = int(input("Введите 1 число "))
b = int(input("Введите 2 число которое большем чем 1-ое"))
res = 0
if a >= b:
    print("a >= b >:( ")
else:
    for i in range(a, b + 1):
        if i % 2 == 0:
            res += i
            print(f"\nЧётное {i} ")
        else:
            print(f"\nНечётное {i}")
print(f"\nРезультат: {res}")

