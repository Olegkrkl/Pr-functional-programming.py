# Введення чисел a, b, c та числа k
a = 24
b = 36
c = 14
k = 3

# Ініціалізація списку для збереження чисел, які діляться на k
divisors = []

# Перевірка кожного числа на дільник k
if a % k == 0:
    divisors.append(a)
if b % k == 0:
    divisors.append(b)
if c % k == 0:
    divisors.append(c)

# Виведення результату
if divisors:
    print("Числа, які діляться на", k, ":", divisors)
else:
    print("Немає чисел, які діляться на", k)
