#author:- Bhavya Joshi

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
            
    #z = list(reversed(y))
    dnacompliment = ''.join(y)
    return dnacompliment
 
print(dna_to_mrna('ATCGCGAT'))
