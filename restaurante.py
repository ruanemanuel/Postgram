G1, G2, G3, G4 = map(int, input().split())

total = G1*1 + G2*2 + G3*3 + G4*4

quantidade = (total // 4) + 1 if total != 0 else 0

print(quantidade)