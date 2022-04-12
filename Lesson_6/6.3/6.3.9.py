  # Арифметические строки
a, b, c = len(input()), len(input()), len(input())
if (2*b-c-a)==0 or (2*c-b-a)==0 or (2*a-b-c) == 0:
    print('YES')
else:
    print('NO')