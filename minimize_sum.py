inp = input()
arr1 = input()
arr1 = arr1.split(" ")
arr = [int(i) for i in arr1]
arr_len, max_op = inp.split(" ")
max_op  = int(max_op)
i = 0
while i < max_op:
    arr = sorted(arr, reverse = True)
    arr[0] = arr[0]//2
    i+=1
print(sum(arr))
