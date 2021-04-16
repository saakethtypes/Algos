arr = [0,1,21,33,45,45,61,71,72,73]
arr.sort()

def bin_search(x,m,l,r):
    if l > r :
        return -1
    m = ( l + r )//2
    if x == arr[m]:
        return m
    elif x > arr[m]:
        l = m + 1
        return bin_search(x,m,l,r)
    else:
        r = m-1
        return bin_search(x,m,l,r)

l = 0 
r = len(arr) -1
m = (l+r)//2
ix = bin_search(61,m,l,r)
print(ix)