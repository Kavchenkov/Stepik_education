  # Три города
n1,n2, n3 = input(), input(), input()
a, b, c = len(n1), len(n2), len(n3)
if a <= b <= c or a <= c <= b:
    print(n1)
elif b <= a <= c or b <= c <= a:
    print(n2)
elif c <= a <= b or c <= b <= a:
    print(n3)
if a >= b >= c or a >= c >= b:
    print(n1)
elif b >= a >= c or b >= c >= a:
    print(n2)
elif c >= a >= b or c >= b >= a:
    print(n3)