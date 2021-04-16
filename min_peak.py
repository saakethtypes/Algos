def min_peak(arr):
    a = []
    for i in range(0,len(arr)-2):
        if arr[i]<arr[i+1]>arr[i+2]:
            a.append(arr[i+1])
        else:
            continue
    return min(a)

arr= [1,10,1,4,6,9,6] 
print(min_peak(arr))