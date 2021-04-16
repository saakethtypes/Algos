def slide(arr,k):
    maxia = []
    for i in range(0,len(arr)-k+1):
        maxi = 0
        for j in range(k):
            maxi += arr[i+j]
            maxia.append(maxi)
    return max(maxia)

print(slide([1, 4, 2, 10, 23, 3, 1, 0, 20],4))
