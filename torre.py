N = int(input())

from itertools import permutations as perm

def find_min_max(combinations):
    nums = []

    for i in range(len(combinations)):
        num = int("".join(combinations[i]))
        nums.append(num)
    return max(nums), min(nums)

N0 = int(N)
numbers = []
numbers.append(N0)
for _ in range(1000):
    combs = list(perm(str(N0)))
    high, low = find_min_max(combs)
    number = high - low

    if number in numbers:
        break
    numbers.append(number)

    N0 = number

for n in numbers:
    print(n)



