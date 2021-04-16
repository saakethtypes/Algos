def selection_sort(arr):
    for j in range(len(arr)-1): 
        minm = 10
        mix = 0
        for i in range(j,len(arr)):
            if arr[i] < minm:
                minm = arr[i]
                mix = i
                
        arr[mix],arr[j] = arr[j],arr[mix]
        print(arr)
    return arr


arrr = [8,5,2,9,5,6,3]
print(selection_sort(arrr))