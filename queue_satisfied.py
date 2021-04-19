numOfPeople = int(input())
waitTimes = list(map(int, input().split()))
 
def numOfSatisfied(arr):
    arr.sort()
    dissapointed = 0
    suml = 0
    for i in range(1,len(arr)):
        if suml<=arr[i-1]:
            suml +=arr[i-1]
        bigger = max(suml,arr[i])
        if(arr[i]!=bigger):
            dissapointed += 1
    ans = len(arr) - dissapointed
    return ans
 
print(numOfSatisfied(waitTimes))