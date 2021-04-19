# Unfinished

n = '675'
pos = [n]

for i in range(1,len(n)):
    l = n[:i]
    r = n[i:]

    if str(int(r[-1])-1) == l[-1]:
        if len(r)>1:
            
        else:
            return int(l)
        
    else:
        if len(r)>1:
            break
        else:
            if len(l)>1:
                if l[0]==r:
                    return int(l)+1 
                else:
                    break
            else:
                return int(l+r)+1


    print(l,r)  
