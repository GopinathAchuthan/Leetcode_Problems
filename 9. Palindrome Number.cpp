class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0){
            return false;
        }
        int y = 0;
        int temp = x;
        while(x){
            if(y> (pow(2,31)-1)/10){
                return false;
            }
            y*=10;
            y+=x%10;
            x/=10;
        }
        
        if(temp == y){
            return true;
        }
        else{
            return false;
        }
    }
};