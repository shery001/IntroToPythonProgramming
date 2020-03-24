#Author : Bhavya Joshi

dna= "AATCTCTACGGAAGTAGGTCAGTACTGATCGATCAGTCGATCGGGCGGCGATTTCGATCTGATTGTACGGCGGGCTAG"
# function below convert dna to rna.
def dna_to_mrna(x):
    #print (x)
    y = list(x)
    z = len(x)
    #print (y)
    #print (z)
    for i in range(0,len(y)):
        c = y[i]
        if c=='T':
            y[i]='U'            
        else: 
            y[i]=c
            
    mrna0 = ''.join(y)
    return mrna0
 
mrna=(dna_to_mrna(dna))

#print mrna

#function below split mran into condons.
def split_by_n( seq, n ):
    #A generator to divide a sequence into chunks of n units.
    while seq:
        yield seq[:n]
        seq = seq[n:]
s =  list(split_by_n(mrna,3))

#print s

#main function for the problem.
def dna_to_protein(dna):
    f= open('/home/bhavya/Documents/AA/PythonProgramming/Day_2/problem_1_codons.txt','r')
    lines = f.read().splitlines()
    #lines=f.readlines.strip()
    #for line in f:
     #   line = line.strip()
          #  print(repr(line))
    mrna=[]
    pro=[]
    #print lines
    for x in lines:
        mrna.append(x.split(' ')[0])
        pro.append(x.split(' ')[1])
    #print mrna
    #print pro
    seq = []
    #print len(mrna) 
    #print (len(s))
    
    for j in range(len(s)):
        for i in range(len(mrna)):
            if s[j]==mrna[i]:
                if pro[i]=='Stop':
                    break
                else:
                    seq.append(pro[i])
    seq1 = ''.join(seq)
    return seq1

print dna_to_protein(dna)
