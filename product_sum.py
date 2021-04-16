arr = [5,2,[7,-1],3,[6,[-13,8],4]]

def product_sum(arr,m):
    summ = 0
    for ele in arr:
        if type(ele) is list:
            summ += product_sum(ele,m+1)
        else:
            summ += ele
    return summ * m    

print(product_sum(arr,1))