
def closest2(L):
    """
    >>> closest2([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (4.3, 5.4)
    >>> closest2([ 15.1, 14.3])
    (14.3, 15.1)
    >>> closest2([ 15.1, -12.1, 5.4,  17.4,  ])
    (15.1, 17.4)
    >>> closest2([-12.1, - 11.5,  5.4, 11.8, 17.4, 4.3, 6.9 ])
    (-12.1, -11.5)
    
    """
    L1 = sorted(L)
    diff = []
    for i in range(len(L)-1):
        diff.append(abs(L1[i+1] - L1[i]))
    mn = diff.index(min(diff))
    tup = (L1[mn], L1[mn+1])
    return tup





L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
(x,y) = closest2(L1)
print((x, y))

L2 = [ 15.1, 14.3]
(x,y) = closest2(L2)
print((x, y))

L3 = [ 15.1, -12.1, 5.4,  17.4,  ]
(x,y) = closest2(L3)
print((x, y))

L1 = [-12.1, - 11.5,  5.4, 11.8, 17.4, 4.3, 6.9 ]
(x,y) = closest2(L1)
print((x, y))

L1 = [ 15.1, -12.1, - 12.1,  5.4, 11.8, 17.4, 4.9, 6.9 ]
(x,y) = closest2(L1)
print((x, y))