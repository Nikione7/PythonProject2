def find_pairs(n):
    pairs = []
    for i in range(1, 21):
        if i == n:
            break
        for j in range(i, n):
            if n % (i + j) == 0 and i != j:
                pairs.append(f"{i}{j}")
    return "".join(pairs)
n = int(input("Введите число от 3 до 20: "))
result = find_pairs(n)
print(f"Нужный пароль для числа {n}: {result}")