#import
import syllables

#variable input
para = input('Enter a paragraph => ')
print(para)
para1 = para
para = para.split()
length = len(para)
hard = []
syll = 0

#while loop (count hard words and syllables
i = 0
while i < length:
    ln = syllables.find_num_syllables(para[i])
    syll = syll + ln
    if ln > 2:
        if not '-' in para[i] or para[i].endswith(('es', 'ed')):
            hard.append(para[i])
    i += 1
    
#data processing
ASL = length / para1.count('.')
PHW = (len(hard) / length) * 100
ASYL = syll / length
GFRI = 0.4*(ASL + PHW)
FKRI = 206.835-1.015*ASL-86.4*ASYL

#printing results
print('Here are the hard words in this paragraph:\n', hard, sep="")
print('Statistics: ASL:{0:.2f} PHW:{1:.2f}% ASYL:{2:.2f}'.format(ASL, PHW, ASYL))
print('Readability index (GFRI): {0:.2f}'.format(GFRI))
print('Readability index (FKRI): {0:.2f}'.format(FKRI))





