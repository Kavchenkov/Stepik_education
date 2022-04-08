print('Мы изучаем язык Python')
print("Мы изучаем язык Python")

a = 'a'
a1 = "a"

print(a == a1)
print(f"Some lorient text {a=}. Don't")
for i in range(0, 10):
    print(f'{i=}')

name1 = input()
name2 = input()
name3 = input()

print(name3)
print(name2)
print(name1)

x = int(input())
y = x + 1
z = y + 1
print(x)
print(y)
print(z)

x = int(input())
y = x + 1
z = y + 1
print(x, y, z, sep = "\n")

a, b, c = int(input()), int(input()), input()
if b == 0 and c == '/':
    print('На ноль делить нельзя!')
elif c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
else:
    print('Неверная операция')

n = 1
if n == 1:
    n += 1
elif n == 2:
    n += 2
print(n)

x = 1
y = 2
if x == 1:
    if y == 2:
        print('qqq')
    else:
        print('www')
elif x == 3:
    print(x)
else:
    pass

if x == 1 and y == 2:
    print('qqq')
elif x == 1 and y != 2:
    print('www')
else:
    pass


x = 1
if x == 1:
    print('YES')
pass