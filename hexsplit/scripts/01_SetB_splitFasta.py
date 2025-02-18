#read __ lines from gene pruned tree file and use to create windows
import sys, os

inputFasta=open(sys.argv[1], "r")
#print(inputFasta)
inputLines = inputFasta.read()
lines = inputLines.split("\n") #list of ids followed by alignment
#print(lines)

# when length not written in file --> use biopython alignment length
length = len(str(lines[1]))
#print(length)

#print(f'length of alignment: {length}')
#print(f'number of lines in lines: {len(lines)}')

sixth_1 = int(length/6)
sixth_2 = sixth_1*2
sixth_3 = sixth_1*3
sixth_4 = sixth_1*4
sixth_5 = sixth_1*5
sixth_6 = sixth_1*6

output_dir = sys.argv[2]

window1 = os.path.join(output_dir, 'window1')
window2 = os.path.join(output_dir, 'window2')
window3 = os.path.join(output_dir, 'window3')

'''
print(sixth_1)
print(sixth_2)
print(sixth_3)
print(sixth_4)
print(sixth_5)
print(sixth_6)
'''

with open(window1,'w') as w1, open(window2,'w') as w2, open(window3,'w') as w3:
    for line in range(1, len(lines), 2):
        #ignore non alignment aka id lines (alignments of size 1000)
        seq=lines[line]
        id=lines[line-1]
        if id[0]==">":
            pass
        else:
            id=">"+id #not on similuated data sets
        offset = str(seq[0:int(sixth_1)])
        end = str(seq[int(sixth_5):])
        s1=str(seq[int(sixth_1):int(sixth_3)])
        s2=str(seq[int(sixth_3):int(sixth_5)])
        s3= str("".join([end, offset]))
        w1.write(id+"\n")
        w1.write(s1+"\n")
        w2.write(id+"\n")
        w2.write(s2+"\n")
        w3.write(id+"\n")
        w3.write(s3+"\n")

#print('Set B generated')