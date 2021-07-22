class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        stack_R = []
        ans = ['.']*len(dominoes)
        for i,dir in enumerate(dominoes):
            if dir == 'R':
                stack_R.append(i)
            elif dir == 'L':
                if stack_R:
                    right = stack_R.pop()
                    left = i
                    while(right<left):
                        ans[right]='R'
                        ans[left]='L'
                        right+=1
                        left-=1
                    while(stack_R):
                        right=stack_R.pop()
                        while(right<len(dominoes) and ans[right]=='.'):
                            ans[right]='R'
                            right+=1
                else:
                    while(i>=0 and ans[i]=='.'):
                        ans[i]='L'
                        i-=1
        while(stack_R):
            right = stack_R.pop()
            while(right<len(dominoes) and ans[right]=='.'):
                ans[right]='R'
                right+=1
        
        return ''.join(ans)
            