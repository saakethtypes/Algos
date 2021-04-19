#1513F

arr_size = int(input())
a = input().split(' ')
b = input().split(' ')
l = lambda x: int(x)
a = list(map(l,a))
b = list(map(l,b))

def eval_swap(a,b,i,j):
    b[i],b[j]=b[j],b[i]
    difference = []
    ab = zip(a, b)
    for ai, bi in ab:
        difference.append(abs(ai-bi))
    b[j],b[i]=b[i],b[j]
    return sum(difference)

def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

def closest_cross(a,b):
    crosses = []
    crs_ix = []
    for k in a:
        bn = closest(b,k)
        t1 = abs(bn-k)
        an = b.index(bn)
        t2 = abs(b[a.index(k)]- a[an])
        crosses.append(t1+t2)
        crs_ix.append([a.index(k),an])
    cixs = crs_ix[crosses.index(min(crosses))]
    crosses_check = sorted(crosses)
    if cixs[0]==cixs[1]:
        if crosses_check[0] == crosses_check[1]:
            crs_ix.remove(cixs)
            crosses.remove(min(crosses))
            cixs = crs_ix[crosses.index(min(crosses))]
            return cixs
        else:
            return cixs
    else:
        return cixs

def swap_min(a,b):
    hi = a.index(max(a))
    hj = b.index(max(b))
    highest_swap = eval_swap(a,b,hi,hj)
    ci = closest_cross(a,b)
    closest_cross_swap = eval_swap(a,b,ci[0],ci[1])
    if highest_swap<closest_cross_swap:
        print(highest_swap)
    else:
        print(closest_cross_swap)

swap_min(a,b)
