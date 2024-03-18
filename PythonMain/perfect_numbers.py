def perfect(num):
    divisbles = []

    for i in range(1, num):
        if num/i == num//i:
            divisbles.append(i)

    return sum(divisbles) == num

for i in range(1, 10**10):
    if perfect(i):
        print(i)
