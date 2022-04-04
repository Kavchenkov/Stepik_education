age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
if age >= 12 and grade >= 7:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and city == 'Москва':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

city = input('В каком городе вы живете?: ')
if city == 'Москва' or city == 'Санкт-Петербург' or city == 'Екатеринбург':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and (city == 'Москва' or city == 'Санкт-Петербург'):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

    a = int(input())
    if a >= 1000:
        print('YES')
    else:
        print('NO')

a = int(input())
if (a % 4 ==0 and not a % 100 ==0) or a % 400 ==0:
    print('YES')
else:
    print('NO')

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a==c or b==d:
    print('YES')
else:
    print('NO')

  № альтернативный вариант
a= int(input()) ##x
b= int(input()) ##y
c= int(input())
d= int(input())
if a == c or b == d and (1<= a,b,c,d <= 8):
    print('YES')
else:
    print('NO')

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (1 <= a <= 8 and 1 <= b <= 8) and (-1 <= a - c <= 1) and (-1 <= b - d <= 1):
    print('YES')
else:
    print('NO')

  № альтернативный вариант
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a == c or a == c - 1 or a == c + 1) and (b == d or b == d + 1 or b == d - 1):
    print("YES")
else:
    print("NO")