a = input('Введите числа через пробел:')
a1 = [int(_) for _ in a.split()]
a2 = []
for i in range(len(a1)):
    if a1[i] in a2:
        print(a1[i], '- YES')
    else:
        print(a1[i], '- NO')
        a2 += [a1[i]]
      