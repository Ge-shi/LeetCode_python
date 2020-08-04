class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, dt, flags):
            if flags[i] == 1: return False
            if flags[i] == -1: return True
            flags[i] = 1
            for c in dt[i]:
                if not dfs(c, dt, flags): return False
            flags = -1
            return True
        flags = [0 for _ in range(numCourses)]
        dt = [[]for _ in range(numCourses)]
        for cur, pre in prerequisites:
            dt[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, dt, flags): return False
        return True