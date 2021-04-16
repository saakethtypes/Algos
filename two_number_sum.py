arr = [3,5,-4,8,11,1,-1,6]
target = 10

def HashApproach(arr,target):
    hasht = []
    for i in arr:
        y = target - i
        if y in hasht:
            return [i,y]
        else:
            hasht.append(i)

def TwoPointerApproach(arr,target):
    arr.sort()
    l = 0
    r = len(arr) - 1 
    while l < r:
        if arr[l]+arr[r] == target:
            return [arr[l],arr[r]]
        elif arr[l]+arr[r] < target:
            l += 1
        elif arr[l]+arr[r] > target:
            r -= 1

tpa = TwoPointerApproach(arr,target)
hta = HashApproach(arr,target)

print(tpa,hta)