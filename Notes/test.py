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