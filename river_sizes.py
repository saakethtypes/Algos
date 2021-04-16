ques = [[1,0,0,1,0],[1,0,1,0,0],[0,0,1,0,1],[1,0,1,0,1],[1,0,1,1,0]]

class Sol:
    def dfs(self,grid,r,c,size,ss):
        grid[r][c] = 0
        size += 1
        lst = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
        for r,c in lst:
            if r>=0 and c>=0 and r< len(grid) and c< len(grid[r]) and grid[r][c]==1:
                self.dfs(grid,r,c,size,ss)
        ss.append(size)
        return max(ss)

    def size_counts(self,grid):
        sizes = []
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]==1:
                    size = self.dfs(grid,r,c,1,[])
                    sizes.append(size)
        return sizes
    
s = Sol()
dd = s.size_counts(ques)
print(dd)