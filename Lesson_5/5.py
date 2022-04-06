age = int(input())
male = input()
if 10 <= age <= 15  and male == 'f':
    print('YES')
else:
    print('NO')

a = int(input())
if a == 1 and 1 <= a <= 10:
    print('I')
elif a == 2 and 1 <= a <= 10:
    print('II')
elif a == 3 and 1 <= a <= 10:
    print('III')
elif a == 4 and 1 <= a <= 10:
    print('IV')
elif a == 5 and 1 <= a <= 10:
    print('V')
elif a == 6 and 1 <= a <= 10:
    print('VI')
elif a == 7 and 1 <= a <= 10:
    print('VII')
elif a == 8 and 1 <= a <= 10:
    print('VIII')
elif a == 9 and 1 <= a <= 10:
    print('IX')
elif a == 10 and 1 <= a <= 10:
    print('X')
else:
    print('ошибка')

a = int(input())
if (a % 2 == 0 and 2 <= a <= 5) or (a % 2 == 0 and a > 20):
    print('NO')
elif (a % 2 == 0 and 6 <= a <= 20):
    print('YES')
else:
    print('YES')

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if x2 != x1 and y2 != y1 and (x2 - y2 == x1 - y1 or x2 + y2 == x1 + y1):
    print('YES')
else:
    print('NO')

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if x2 != x1 and y2 != y1 and (x2 - y2 == x1 - y1 or x2 + y2 == x1 + y1) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')                                                                                  


