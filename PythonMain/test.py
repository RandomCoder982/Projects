from itertools import combinations
from itertools import product


def mul(list):
    ans = 1
    for num in list:
        ans *= num
    return ans

def leet(num, target):
    acceptable = []
    lis = [int(x) for x in num]
    
    if sum(lis) == target:
        acceptable.append("+".join([f"{str(x)}" for x in lis]))
        
    if mul(lis) == target:
        acceptable.append("*".join([f"{str(x)}" for x in lis]))
    
    return acceptable
        
    
for i in range(len([1, 2, 3])):
    for j in combinations([1, 2, 3], len([1, 2, 3])):
        if sum(j) == 6:
            print(f"Works, {j}")
        else:
            print(f"Doesn't work, {j}")
