x1 = 2
y1 = 3
x2 = -1
y2 = 5

distance_A = (x1 ** 2 + y1 ** 2) ** 0.5
distance_B = (x2 ** 2 + y2 ** 2) ** 0.5

if distance_A < distance_B:
    print("Точка A знаходиться ближче до початку координат.")
elif distance_A > distance_B:
    print("Точка B знаходиться ближче до початку координат.")
else:
    print("Точки A і B розташовані на однаковій відстані до початку координат.")
