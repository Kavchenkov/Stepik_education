print(2 ** 0)
print(2 ** 1)
print(2 ** 2)
print(2 ** 3)
print(2 ** (-1))

x = int(input())
print(f'{x}\n{x+1}\n{x+2}')


b, q, n = int(input()), int(input()), int(input())
print(b*q**(n-1))

x = int(input())
print(x // 100)

x, y = int(input()), int(input())
print(y // x, y % x, sep='\n')

x = int(input())
print((-x // 2)*-1)

x = int(input()) # вариант 1
print((-x // 4)* - 1)

a = int(input()) # вариант 2
print((a-1) // 4 + 1)

x = int(input())
print(x, 'мин - это',x // 60,'час', x % 60, 'минут.')

num = int(input())
x = (num // 10) % 10
y = num // 100
z = num % 10
print('Сумма цифр =', x+y+z)
print('Произведение цифр =', x*y*z)

num=int(input())
a=num // 100
b=(num // 10) % 10
c=num % 10
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')

  # e = (num // n) % 10, где n число 1, 10, 100, 1000 (для поиска нужной цифры в строке)

a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 10
print('Цифра в позиции тысяч равна', a)
print('Цифра в позиции сотен равна', b)
print('Цифра в позиции десятков равна', c)
print('Цифра в позиции единиц равна', d)

n = int(input())
print(n+(10*n+n)+((100*n))+(10*n+n))

  # второй вариант n = input()
  # второй вариант print(int(n)+int(n+n)+int(n+n+n))

a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(a**b)


a, b = int(input()), int(input())
print('Квадрат суммы', a, 'и', b, 'равен', (a+b)**2)
print('Сумма квадратов', a, 'и', b, 'равна', (a**2)+(b**2))