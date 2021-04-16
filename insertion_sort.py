def insertion_sort(arr):
    for i in range(len(arr)-1):
        j = i + 1
        while j > 0:
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j] = arr[j] , arr[j-1]
            j -= 1
    return arr


arrr = [8,5,2,9,5,6,3]
print(insertion_sort(arrr))