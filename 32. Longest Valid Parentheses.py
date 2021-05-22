class Solution:
    def longestValidParentheses(self, s: str) -> int:
        track = []
        curr_pointer = 0
        # record the track of valid parentheses
        while(curr_pointer<len(s)):
            if s[curr_pointer] == ')':
                # print('check1')
                temp_pointer = curr_pointer-1
                while(0<=temp_pointer):
                    # print('check2')
                    if track[temp_pointer] == 1:
                        temp_pointer -=2
                    else:
                        break
                if temp_pointer<0 or s[temp_pointer]!='(':
                    track.append(0)
                else:
                    track[temp_pointer] = 1
                    track.append(1)
            else:
                track.append(0)
        
            curr_pointer+=1
            # print(track)
        
        
        # calculate longest valid parentheses
        temp = 0
        curr_max = 0
        
        for value in track:
            if value:
                temp+=1
            else:
                if temp>curr_max:
                    curr_max = temp
                temp = 0
        
        return max(temp, curr_max)
        