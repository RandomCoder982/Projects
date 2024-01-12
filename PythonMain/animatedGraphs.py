import time
import numpy as np


list1 = list(range(200000000))
nplist = np.array(range(200000000))

def wrapper(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)

@wrapper
def arraySquared():
    for number in list1:
        number **= 2
        
print("\n")

@wrapper
def npArraySquared():
    for number in nplist:
        number **= 2

