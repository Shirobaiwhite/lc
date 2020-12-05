class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        // map to keep track
        map<int, int> map1;
        vector<int> result;
        // loop through nums
        for (int i = 0; i < nums.size(); i++) {
            // if map1 does not have nums[i]
            if (map1.find(nums[i]) == map1.end()) {
                map1[nums[i]] = 1;
            } else {
                // if maps1 does have nums[i]
                map1[nums[i]]++;
            }
            
            // condition check if occurrences is larger than n/3
            if (map1[nums[i]] > nums.size() / 3) {
                // filtering out duplicates
                if (!(find(result.begin(), result.end(), nums[i]) != result.end())) {
                    result.push_back(nums[i]);
                }
                
            }
        }
        return result;
    }
};
