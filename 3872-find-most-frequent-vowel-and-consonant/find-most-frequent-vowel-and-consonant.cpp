class Solution {
public:
    int maxFreqSum(string s) {
        unordered_map<char, int> chars;
        string vowel = "aeiou";
        int v_max_count = 0;
        int c_max_count = 0;
        for(auto i: s) {
            ++chars[i];

            if(vowel.find(i) == std::string::npos) {
                c_max_count = max(chars[i], c_max_count);
            } else {
                v_max_count = max(v_max_count, chars[i]);
            }
        }
        return v_max_count + c_max_count;
    }
};