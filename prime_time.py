#incomplete code
import numpy as np

#util funcs
def prime_check(x):
    if(x <= 3):
        return x > 1
    if (x%2 == 0 or x%3 == 0):
        return False
    for i in range(5, 1 + int(np.sqrt(x))): 
        if x % i == 0:
            
            return False
        print(x) 
    return True

def get_primes(l):
    primes = []
    for i in range(0,l):
        if(prime_check(i)):
            primes.append(i)
    return primes

#algo
def get_last(x):
    if x < end:
        if(prime_check(x+interval)):
            #print(x, x+interval)
            return get_last(x+interval)
        else:
            return 0
    else:
        #print("possiblity - ",x - interval)
        return x

def run():
    fpp = get_primes(end)
    print(len(fpp))
    ans = []
    #print('d,i',end,interval)
    for sp in fpp:
        tempans = get_last(sp)
        if tempans not in ans:
            ans.append(tempans)
    print(len(ans) - 1)
    return len(ans) - 1,ans

#run
dp = input('').split(' ')
end,p,interval = int(dp[0]),int(dp[1]),int(int(dp[0])/int(dp[1]))
answer, ans = run()
ans = [x - interval for x in ans]

print(answer)