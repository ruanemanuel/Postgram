N, M = map(int, input().split())
molecules = []
for _ in range(N):
    P, G, C = map(int, input().split())
    molecules.append([P, G, C])
   
tP, tG, tC = 0, 0, 0

for mole in molecules:
    tP += mole[0] * 4
    tG += mole[1] * 9
    tC += mole[2] * 4

amount = M - (tP + tG + tC)
print(amount)              