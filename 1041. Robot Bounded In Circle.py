class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        right = {'N':'E', 'E':'S', 'S':'W', 'W':'N'}
        left = {'N':'W', 'E':'N', 'S':'E', 'W':'S'}
        
        curr_dir = 'N'
        x,y = 0,0
        for inst in instructions:
            if inst == 'G':
                if curr_dir == 'N':
                    y += 1
                if curr_dir == 'S':
                    y -= 1
                if curr_dir == 'E':
                    x += 1
                if curr_dir == 'W':
                    x -= 1
            elif inst == 'R':
                curr_dir = right[curr_dir]
            elif inst == 'L':
                curr_dir = left[curr_dir]
        
        if curr_dir != 'N':
            return True
        if x == 0 and y == 0:
            return True
        
        return False