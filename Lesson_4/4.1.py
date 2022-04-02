answer = input('Какой язык программирования мы изучаем?')
if answer == 'Python':
    print('Верно! Мы работаем в Python =)')
    print('Python- отличный язык!')
else:
    print('Не совсем так!')

num1 = int(input())
num2 = int(input())

if num1 < num2:
    print(num1, 'меньше чем', num2)
if num1 > num2:
    print(num1, 'больше чем', num2)
if num1 == num2:                      # используем двойное равенство
    print(num1, 'равно', num2)
if num1 != num2:
    print(num1, 'не равно', num2)

age = int(input())
if 3 <= age <= 6:
    print('Вы ребёнок')

age = int(input())
if 3 <= age <= 6:
    print('Вы ребёнок')

a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('числа равны')
else:
    print('числа не равны')

a, b, c = int(input()), int(input()), int(input())
if a != b != c:
    print('числа равны')
else:
    print('числа не равны')

word = input()
if word == 'Python':
    print('ДА')
else:
    print('НЕТ')

num = int(input())
last_digit = num % 10    # последняя цифра числа
first_digit = num // 10  # первая цифра числа

if last_digit == first_digit:
    print('ДА')
else:
    print('НЕТ')

num1, num2, num3 = int(input()), int(input()), int(input())
counter = 0  # переменная счётчик
if num1 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
print(counter)

i = int(input())
if i / 2:
    print(i, 'чётное')
else:
    print(i, 'нечётное')

if i / 2:
    print(i, 'чётное')
else:
    print(i, 'нечётное')

if i % 2 == 0:
    print(i, 'чётное')
else:
    print(i, 'нечётное')

if i // 2 == 0:
    print(i, 'чётное')
else:
    print(i, 'нечётное')

if i % 2 != 0:
    print(i, 'нечётное')
else:
    print(i, 'чётное')

if i // 2 != 0:
    print(i, 'нечётное')
else:
    print(i, 'чётное')

a, b = input(), input()
if a == b:
    print('Пароль принят')
else:
    print('Пароль не принят')

a = int(input())
if a % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

a = int(input())
if (a // 1000) + (a % 10) == ((a // 100) % 10) - ((a // 10) % 10):
    print('Да')
else:
    print('Нет')

  # Альтернативный вариант исполенения предыдущего задания

abcd = int(input())
a = (abcd % 10000) // 1000
b = (abcd % 1000) // 100
c = (abcd % 100) // 10
d = abcd % 10
if (a + d) == (b - c):
    print('ДА')
else:
    print('НЕТ')

  # Еще один рабочий вариант
s = input()
if int(s[0])+int(s[3])==int(s[1])-int(s[2]):
    print('ДА')


age = int(input())
if 18 <= age:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

print('Доступ разрешен' if  int(input()) >= 18 else 'Доступ запрещен')  # Альтернативный вариант

a, b, c = int(input()), int(input()), int(input())
if a == b - 1 == c - 2:
    print('YES')
else:
    print('NO')

if int(input()) == int(input()) - 1 == int(input()) - 2:
    print('YES')
else:
    print('NO')

a, b, c = int(input()), int(input()), int(input())
if b - a + b == c:
    print('YES')
else:
    print('NO')

a, b = int(input()), int(input())
if a > b:
    print(b)
else:
    print(a)

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a < b:
    x = a
else:
    x = b
if c < d:
    y = c
else:
    y = d
if x < y:
    print(x)
else:
    print(y)
  # второй вариант исполнения
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a > b:
    a = b
if c > d:
    c = d
if a > c:
    a = c
print(a)

age = int(input())
if 0 <= age <= 13:
    print('детство')
if 14 <= age <= 24:
    print('молодость')
if 25 <= age <= 59:
    print('зрелость')
if 60 <= age:
    print('старость')