class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(start : int ,arr : List[int])->None:
            if len(arr)==k:
                res.append(arr[:])
                return
            if start>n:
                return
            arr.append(start)
            dfs(start+1,arr)
            arr.pop()
            dfs(start+1,arr)
        res: List[List[int]]=[]
        ar:List[int]=[]
        dfs(1,ar)
        return res