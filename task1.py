def power_operations(number):
    if number >= 0:
        return number ** 2, number ** 4
    else:
        return number, number


num1 = 5
num2 = 10
num3 = -3

num1_square, num1_power4 = power_operations(num1)
num2_square, num2_power4 = power_operations(num2)
num3_square, num3_power4 = power_operations(num3)


print("Піднесення до квадрата та четвертої ступеня:")
print("Число 1: Квадрат =", num1_square, ", Четверта ступінь =", num1_power4)
print("Число 2: Квадрат =", num2_square, ", Четверта ступінь =", num2_power4)
print("Число 3: Квадрат =", num3_square, ", Четверта ступінь =", num3_power4)
