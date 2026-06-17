N = int(input())
Is = list(map(int, input().split()))

idosos = list(filter(lambda i: i > 60, Is))
n = len(idosos)
if n == 0:
    print(0)
else:
    old = idosos[-1]

    sec = Is.index(old) - n + 1
    
    print(sec)
