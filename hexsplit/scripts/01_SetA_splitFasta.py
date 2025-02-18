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

first_interval=int(length/3)
second_interval=first_interval*2
last_interval=first_interval*3

output_dir = sys.argv[2]

window1 = os.path.join(output_dir, 'window1')
window2 = os.path.join(output_dir, 'window2')
window3 = os.path.join(output_dir, 'window3')

with open(window1,'w') as w1, open(window2,'w') as w2, open(window3,'w') as w3:
    for line in range(1, len(lines), 2):
        #ignore non alignment aka id lines (alignments of size 1000)
        seq=lines[line]
        id=lines[line-1]
        if id[0]==">":
            pass
        else:
            id=">"+id #not on similuated data sets
        s1=str(seq[0:first_interval])
        s2=str(seq[first_interval:second_interval])
        s3=str(seq[second_interval:])
        w1.write(id+"\n")
        w1.write(s1+"\n")
        w2.write(id+"\n")
        w2.write(s2+"\n")
        w3.write(id+"\n")
        w3.write(s3+"\n")

#print('Set A generated')