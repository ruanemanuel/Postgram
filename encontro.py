A1 = int(input())
A2 = int(input())
B1 = int(input())
B2 = int(input())
C1 = int(input())
C2 = int(input())

start = max(A1, B1, C1)
end = min(A2, B2, C2)
if end <= start:
  print(0)
else:
  quantidade = end - start + 1
  print(quantidade)
