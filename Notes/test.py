x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if x2 != x1 and y2 != y1 and (x2 - y2 == x1 - y1 or x2 + y2 == x1 + y1) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')




