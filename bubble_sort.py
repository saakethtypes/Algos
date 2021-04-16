def bubble_sort(arr):
    Sorted = False
    ctr = 0
    while not Sorted:
        Sorted = True
        for i in range(len(arr)-ctr-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1] , arr[i]
                Sorted = False
        ctr += 1
    print(arr)
    return arr

arrr = [8,5,2,9,5,6,3]
bubble_sort(arrr)
            