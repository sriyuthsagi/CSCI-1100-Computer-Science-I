#functions
def percentage_happy(sent):
    haplev = sent.lower().count('laugh') + sent.lower().count('happiness') + sent.lower().count('love') + sent.lower().count('excellent') + sent.lower().count('good')
    haplev = haplev / len(sent.split())
    return haplev

def percentage_sad(sent):
    sadlev = sent.lower().count('bad') + sent.lower().count('sad') + sent.lower().count('terrible') + sent.lower().count('horrible') + sent.lower().count('problem')
    sadlev = sadlev / len(sent.split())
    return sadlev


#input
string = input('Enter a sentence => ')
print(string)


#outputs
happy = percentage_happy(string)
sad = percentage_sad(string)
print('Percentages. happy: {0:.3f} sad: {1:.3f}'.format(happy, sad))

if(happy>sad):
    print('This is a happy sentence')
elif(happy<sad):
    print('This is a sad sentence')
elif(happy == sad):
    print('This is a neutral sentence')

