x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        print('Первая четверть')
    else:
        print('Четвертая четверть')
else:
    if y > 0:
        print('Вторая четверть')
    else:
        print('Третья четверть')

grade = int(input('Введите вашу отметку по 100-балльной системе: '))

if grade >= 90:
    print(5)
else:
    if grade >= 80:
        print(4)
    else:
        if grade >= 70:
            print(3)
        else:
            if grade >= 60:
                print(2)
            else:
                print(1)

grade = int(input('Введите вашу отметку: '))

if grade >= 90:
    print(5)
elif grade >= 80:
    print(4)
elif grade >= 70:
    print(3)
elif grade >= 60:
    print(2)
else:
    print(1)

a, b, c = int(input()), int(input()), int(input())
if a == b:
    if b == c:
        print(3)
    else:
        print(2)
else:
    if a == c:
        print(2)
    else:
        if b == c:
            print(2)
        else:
            print(0)

a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b != c:
    print(2)
elif a != b == c:
    print(2)
elif a == c != b:
    print(2)
else:
    print(0)

a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b != c or a != b == c or a == c != b:
    print(2)
else:
    print(0)

  # первая задача пункат 3.1 в моих двух вариациях
n, k = int(input()), int(input())
if n > k:
    print('NO')
else:
    if k > n:
        print('YES')
    else:
        if k == n:
            print("Don't know")

n, k = int(input()), int(input())
if n > k:
    print('NO')
elif k > n:
    print('YES')
elif k == n:
    print("Don't know")

a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif a == b != c or a != b == c or c == a != b:
    print('Равнобедренный')
elif a != b != c != a:
    print('Разносторонний')

a, b, c = int(input()), int(input()), int(input())
if c > a > b or b > a > c:
    print(a)
elif c > b > a or a > b > c:
    print(b)
elif b > c > a or a > c > b:
    print(c)

a = int(input())
if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
    print('31')
elif a == 4 or a == 6 or a == 9 or a == 11:
    print('30')
elif a == 2:
    print('28')

a = int(input())
if a == 4 or a == 6 or a == 9 or a == 11:
    print('30')
elif a == 2:
    print('28')
else:
    print('31')

a = int(input())
if a <= 59:
    print('Легкий вес')
elif 60 <= a <= 63:
    print('Первый полусредний вес')
elif 64 <= a <= 69:
    print('Полусредний вес')