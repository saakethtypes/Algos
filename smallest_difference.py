import numpy as np
arr1 = [-1,5,10,20,28,3]
arr2 = [15,17,26,134,135]

def smallest_diff(arr1,arr2):
    p1 = 0
    p2 = 0
    ans = []
    pairs = []
    arr1.sort()
    arr2.sort()
    while p1<len(arr1) and p2 < len(arr2):
        if arr1[p1] == arr2[p2]:
            ans.append(arr1[p1]-arr2[p2])
            break
        elif arr1[p1] < arr2[p2]:
            ans.append(np.abs(arr1[p1]-arr2[p2]))
            pairs.append([p1,p2])
            p1 += 1
            
        elif arr1[p1] > arr2[p2]:
            ans.append(np.abs(arr1[p1]-arr2[p2]))
            pairs.append([p1,p2])
            p2 += 1
    return min(ans)

print(smallest_diff(arr1,arr2))