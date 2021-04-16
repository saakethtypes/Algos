arr = [141,1,17,-7,-17,-27,18,541,8,7,7]
ans = [None,None,None]
def find_three_largest():
    for i in arr:
        update_largest(ans,i)
    return ans

def update_largest(tla,i):
    if tla[2] is None or i > tla[2]:
        tla[0] = tla[1]
        tla[1] = tla[2]
        tla[2] = i
    elif tla[1] is None or i > tla[1]:
        tla[0] = tla[1]
        tla[1] =  i
    elif tla[0] is None or i > tla[0]:
        tla[0] = i
    

find_three_largest()
print(ans)