def fib(n,arr):
    if n ==2 :
        arr.append(1)
        return 1
    elif n ==1 :
        arr.append(0)
        return 0
    elif n in arr:
        return n
    else:
        nn = fib(n-1,arr) + fib(n-2,arr)
        arr.append(nn)
        return nn
arr = []
fib(8,arr)
print(arr)
