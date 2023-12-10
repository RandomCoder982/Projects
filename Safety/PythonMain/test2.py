def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123

    # Convert the iterable into a tuple for immutability
    pool = tuple(iterable)
    # Get the length of the tuple
    n = len(pool)

    # Check if the desired combination size is greater than the length of the iterable
    if r > n:
        return

    # Initialize indices with the first r integers
    indices = list(range(r))
    # Yield the first combination
    yield tuple(pool[i] for i in indices)

    # Infinite loop to generate all combinations
    while True:
        # Find the rightmost index i such that indices[i] is not at its maximum allowed value
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            # If the loop completes without breaking, all combinations have been generated
            return

        # Increment the value at index i in the indices list
        indices[i] += 1

        # Update subsequent indices to form a valid combination
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1

        # Yield the next combination based on the updated indices
        yield tuple(pool[i] for i in indices)

        
def Test(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
        
nums = [1, 2, 3, 4, 5]
    
ResultComb = [j for i in range(len(nums)) for j in combinations(nums, i) if sum(j) == 5]
print(ResultComb)
ResultTest = [j for i in range(len(nums)) for j in Test(nums, i) if sum(j) == 5]
print(ResultTest)

##################################################################
from itertools import combinations

nums = [1, 2, -1, -2,]

def example1(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
        
def example2(curr, result, used):
    if len(curr) == l:
        result.add(tuple(sorted(curr))) #Modify this line to change it into itertools.permutations
        return
    else:
        for i in arr:
            if len(curr) == 0:
                check_set = set()
            else:
                check_set = used
            if i not in used:
                temp = curr + [i]
                check_set.add(i)
                combinations(temp, result, check_set)
            
        
def testv1(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return "Not enough numbers in iterable"
    
    idx = list(range(r))
    yield 


for i in range(len(nums)):
    for j in example2(nums, i, 1):
        if sum(j) == 2:
            print(j)
    
