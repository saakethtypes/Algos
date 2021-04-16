hts = [1,8,6,2,5,4,8,3,7,4,3,2,1,4]
class Sol:
    def max_area(self,hts):
        maxa = 0
        l = 0
        r = len(hts) - 1
        while l<r:
            maxa = max(maxa, min(hts[l]*(r-l),hts[r]*(r-l)))
            if hts[l] >= hts[r]:
                r-=1
            else:
                l+=1
        return maxa
    
s = Sol()
d = s.max_area(hts)
print(d)

       
           