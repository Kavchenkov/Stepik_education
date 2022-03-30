num1 = 7            # num1 - это число
num2 = 10           # num2 - это число
num3 = num1 + num2  # num3 - это число
print(num3, end='\n\n')

a = 3
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b, end='\n\n')

num1 = 2 + 3 * 4
num2 = (2 + 3) * 4
print(num1)
print(num2)

s = '1992'
year = int(s)
print(year)

num1 = input()
num2 = input()
print(num1 + num2)

num1 = int(input())
num2 = int(input())
print(num1 + num2)

num = 17
s = str(17)
print(s)

num1 = -6      # унарный минус
print(num1)
num2 = 17 - 7  # бинарный минус
print(num2)

x = int(input())  # первый вариант вывода на печать
y = x + 1
z = y + 1
print(x)
print(y)
print(z)

x = int(input())  # второй вариант вывода на печать
y = x + 1
z = y + 1
print(x, y, z, sep = "\n")

x, y, z = int(input()), int(input()), int(input())
print(x+y+z)

x = int(input())
print('Объем =', x**3)
print('Площадь полной поверхности =', 6*x**2)

a, b = int(input()), int(input())
print(3*(a+b)**3+275*b**2-127*a-41)

x = int(input())
print('Следующее за числом', x, 'число:', x+1)
print('Для числа', x, 'предыдущее число:', x-1)

x, y, z, f = int(input()), int(input()), int(input()), int(input())
print((x+y+z+f)*3)

x, y = int(input()), int(input())
print(x, '+', y, '=', x+y)
print(x, '-', y, '=', x-y)
print(x, '*', y, '=', x*y)

x, y, z = int(input()), int(input()), int(input())
print(x+y*(z-1))

x = int(input())
print(x, 2*x, 3*x, 4*x, 5*x, sep='---')
