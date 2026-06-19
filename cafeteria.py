A = int(input())
B = int(input())
C = int(input())
D = int(input())

start = C - B
end = C - A

quoS = start // D
quoE = end // D

if start % D == 0 or end % D == 0 or abs(quoS - quoE):
    print("S")
else:
    print("N")
    
 