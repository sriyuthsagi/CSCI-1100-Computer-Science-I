def bpop_next(b_pop, f_pop):
    bnext = ((10*b_pop)/(1+0.1*b_pop)) - (0.05*b_pop*f_pop) 
    return int(bnext)

def fpop_next(b_pop, f_pop):
    fnext = 0.4 * f_pop + 0.02 * f_pop * b_pop
    return int(fnext)
    
    
    

#data input + year 1
bpop = int(input('Number of bunnies ==> '))
print(bpop)
fpop = int(input('Number of foxes ==> '))
print(fpop)
print('Year 1: {:.0f} {:.0f}'.format(bpop, fpop))


#Year 2
bpop1 = bpop_next(bpop, fpop)
fpop1 = fpop_next(bpop, fpop)
print('Year 2: {:.0f} {:.0f}'.format(bpop1, fpop1))


#Year 3
bpop = bpop1
fpop = fpop1
bpop1 = bpop_next(bpop, fpop)
fpop1 = fpop_next(bpop, fpop)
print('Year 3: {:.0f} {:.0f}'.format(bpop1, fpop1))


#Year 4
bpop = bpop1
fpop = fpop1
bpop1 = bpop_next(bpop, fpop)
fpop1 = fpop_next(bpop, fpop)
print('Year 4: {:.0f} {:.0f}'.format(bpop1, fpop1))


#Year 5
bpop = bpop1
fpop = fpop1
bpop1 = bpop_next(bpop, fpop)
fpop1 = fpop_next(bpop, fpop)
print('Year 5: {:.0f} {:.0f}'.format(bpop1, fpop1))
