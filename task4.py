
x = 15
y = 9

if x != y:
    if x < y:
        x = (x + y) / 2
        y = 2 * x
    else:
        y = (x + y) / 2
        x = 2 * y

    print("Після заміни:")
    print("x =", x)
    print("y =", y)
else:
    print("Числа x та y повинні бути різними.")
