class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)
        
        for i in range(N//2):
            s[i],s[~i] = s[~i],s[i]
        
        start = 0
        for idx in range(N):
            if s[idx] == ' ':
                end = idx-1
                for i in range(start,(start+(end-start)//2)+1):
                    s[i],s[end] = s[end],s[i]
                    end-=1
                start = idx+1
        
        # Last word
        end = N-1
        for i in range(start,(start+(end-start)//2)+1):
                    s[i],s[end] = s[end],s[i]
                    end-=1