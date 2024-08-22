n = int(input('Введите число от 3 до 20: '))
k = 1
for i in range(1, 21):
    if n >= 3 and n <= 20:
        for j in range(1, 21):
            if n % (i + j) == 0 and i != j:
                result = (i, j)
                print(result)
                k = k + 1
    else:
        print('Введенное число выходит за рамки заданного диапазона')
