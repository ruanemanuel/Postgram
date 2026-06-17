A1 = int(input())
A2 = int(input())
B1 = int(input())
B2 = int(input())
C1 = int(input())
C2 = int(input())

start = max(A1, B1, C1)
end = min(A2, B2, C2)
quantidade = end - start + 1
if A1 == A2 or B1 == B2 or C1 == C2:
  print(0)
else:
  print(quantidade)
