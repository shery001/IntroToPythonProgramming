# author:- Bhavya Joshi

def reverse_compliment(x):
    
    y = list(x)
    z = len(x)
    
    for i in range(0,len(y)):
        c = y[i]
        if c=='A':
            y[i]='T'
            
        elif c=='T':
            
            y[i]='A'
            
        elif c =='G':
            
            y[i]='C'
            
        else:
            
            y[i]='G'
            
    z = list(reversed(y))
    dnacompliment = ''.join(z)
    return dnacompliment

print(reverse_compliment('ATGCGGC'))

print(reverse_compliment('ATGCGCGGATCGTACCTAATCGATGGCATTAGCCGAGCCCGATTACGC'))

#reverse_compliment()
