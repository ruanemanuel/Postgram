N = int(input())

from itertools import permutations as perm

def find_min_max(combinations):
    nums = []

    for i in range(len(combinations)):
        num = int("".join(combinations[i]))
        nums.append(num)
    return max(nums), min(nums)

numbers = []
numbers.append(N)
for _ in range(1000):
    combs = list(perm(str(N)))
    high, low = find_min_max(combs)
    number = high - low

    if number in numbers:
        break
    numbers.append(number)

    N = number

for n in numbers:
    print(n)



