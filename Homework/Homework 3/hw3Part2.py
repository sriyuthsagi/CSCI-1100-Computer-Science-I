import math
#function for bears and berries
def find_next(bears,berries,tourists):
    bears_next = berries/(50*(bears+1)) + bears*0.60 - (math.log(1+tourists,10)*0.1)
    berries_next = (berries*1.5) - (bears+1)*(berries/14) - (math.log(1+tourists,10)*0.05)
    tuply = (bears_next,berries_next)
    return tuply

#function for tourists
def find_tourists(bears):
    people = 0
    if(bears<4 or bears>15):
        people = 0    
    else:
        people = 10000*bears - max((bears-10),0)*10000 + max((bears-10),0)*20000
    return people

#variables
bears = int(input("Number of bears => "))
print(bears)
berries = int(input("Size of berry area => "))
print(berries)
tourists = 0
listBears=[]
listBerries=[]
listtourists=[]
i = 1
berries = float(berries)
print("Year\tBears\tBerries\tTourists")

#while loop
while(i<=10):
    tourists = find_tourists(bears)
    listBears.append(bears)
    listBerries.append(berries)
    listtourists.append(tourists)
    print(i,"\t",bears,"\t",round(berries,1),"\t",tourists,sep="")
    tupleNext = find_next(bears,berries,tourists)    
    bears = max(math.floor(tupleNext[0]),0)
    berries = max(tupleNext[1],0.0)
    i = i + 1
    
#finds max and min
print()
print("Min:\t",min(listBears),"\t{0:.1f}\t".format(min(listBerries)),min(listtourists),sep="")
print("Max:\t",max(listBears),"\t{0:.1f}\t".format(max(listBerries)),max(listtourists),sep="")

