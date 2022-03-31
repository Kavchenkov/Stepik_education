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