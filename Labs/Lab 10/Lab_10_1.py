
def closest1(L):
    """
    >>> closest1([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (4.3, 5.4)
    >>> closest1([ 15.1, 14.3])
    (14.3, 15.1)
    >>> closest1([ 15.1, -12.1, 5.4,  17.4,  ])
    (15.1, 17.4)
    >>> closest1([-12.1, - 11.5,  5.4, 11.8, 17.4, 4.3, 6.9 ])
    (-12.1, -11.5)
    """
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




L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
(x,y) = closest1(L1)
print((x, y))

L2 = [ 15.1]
(x,y) = closest1(L2)
print((x, y))

L3 = [ 15.1, -12.1, 5.4,  17.4,  ]
(x,y) = closest1(L3)
print((x, y))

L1 = [-12.1, - 11.5,  5.4, 11.8, 17.4, 4.3, 6.9 ]
(x,y) = closest1(L1)
print((x, y))

L1 = [ 15.1, -12.1, - 12.1,  5.4, 11.8, 17.4, 4.9, 6.9 ]
(x,y) = closest1(L1)
print((x, y))