class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> ans;
        vector<int> :: iterator maxElement = max_element(candies.begin(), candies.end());
        
        for(vector<int> :: iterator it = candies.begin(); it!=candies.end(); it++){
            if (*it+extraCandies>=*maxElement){
                ans.push_back(true);
            }
            else{
                ans.push_back(false);
            }
        }
        
        return ans;
    }
};