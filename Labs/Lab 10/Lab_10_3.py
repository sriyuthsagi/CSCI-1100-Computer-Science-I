
"""
N^2
N log(N)
"""

import time
import random


def closest1(L):
    if len(L) < 2:
        tup = (None, None)
    else:
        differences = []
        for i in range(len(L)):
            for j in range(len(L)):
                diff = L[j] - L[i]
                if diff != 0:
                    differences.append([abs(diff), L[i], L[j]])
        mn = differences.index(min(differences))
        tup = (differences[mn][1], differences[mn][2])
    return tup



def closest2(L):
    L1 = sorted(L)
    diff = []
    for i in range(len(L)-1):
        diff.append(abs(L1[i+1] - L1[i]))
    mn = diff.index(min(diff))
    tup = (L1[mn], L1[mn+1])
    return tup



if __name__ == '__main__':
    case1 = []
    while len(case1) < 100:
        case1.append(random.uniform(0.0, 1000.0))
    case2 = []
    while len(case2) < 1000:
        case2.append(random.uniform(0.0, 1000.0))
    case3 = []
    while len(case3) < 10000:
        case3.append(random.uniform(0.0, 1000.0))
    
    timei1 = time.time()
    closest1(case1)
    timef1 = time.time()
    print(timef1 - timei1)
    timei2 = time.time()
    closest2(case1)
    timef2 = time.time()
    print(timef2 - timei2)  
    print('')
    print('')
    
    timei3 = time.time()
    closest1(case2)
    timef3 = time.time()
    print(timef3 - timei3)
    timei4 = time.time()
    closest2(case2)
    timef4 = time.time()
    print(timef4 - timei4)  
    print('')
    print('')
    
    timei5 = time.time()
    closest1(case3)
    timef5 = time.time()
    print(timef5 - timei5)
    timei6 = time.time()
    closest2(case3)
    timef6 = time.time()
    print(timef6 - timei6)  
    print('')
    print('')    