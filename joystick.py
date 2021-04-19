#651A
import math
ab = input()
ab = ab.split(' ')
a,b = int(ab[0]),int(ab[1])
time_played = 0

while a >= 1 and b >= 1:
    if a+b == 2:
        break
    if((math.ceil(a/2) == math.ceil(b/2))):
        if a%2==0:
            a+=1
            b-=2
            time_played+=1
        else:
            a-=2
            b+=1
            time_played+=1
    elif (math.ceil(a/2) > math.ceil(b/2)):
        b+=1
        a-=2
        time_played+=1
    elif (math.ceil(a/2) < math.ceil(b/2)):
        b-=2
        a+=1
        time_played+=1
print(time_played)



