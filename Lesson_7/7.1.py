for i in range(10):
    print('Привет')

for i in range(5):
    num = int(input())
    print('Квадрат вашего числа равен:', num * num)
print('Цикл завершен')

for i in range(10):
    print('Python is awesome!')

a, b = input(), int(input())
for i in range(b):
    print(a)

a, b, c, d, e = input(), input(), input(), input(), input()
for i in range(6):
    print(a)
for i in range(5):
    print(b)
print(c)
for i in range(9):
    print(d)
print(e)

for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')

a = int(input())
for i in range(a):
    print('*******************')

for i in range(10):
    print(i, '-- Привет')

for i in range(10):
    print(i + 1, '-- Привет')

a = input()
for i in range(10):
    print(i, a)

a = int(input())
for i in range(a + 1):
    print('Квадрат числа', i, 'равен', i*i)

a = int(input())
for i in range(a+1):
    print('*' * (a - i))

  # решение через жопу
m, p, n = float(input()), float(input()), int(input())
print('1', m)
for i in range(n-1):
    m = m + m * p / 100
    print(i + 2, m)