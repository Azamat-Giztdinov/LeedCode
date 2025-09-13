class Solution {
public:
    int maxFreqSum(string s) {
        map<char, int> chars;
        string vowel = "aeiou";
        int v_max_count = 0;
        int c_max_count = 0;
        for(auto i: s) {
            if(chars.find(i) == chars.end()) {
                chars[i] = 1;
            } else {
                chars[i] += 1;
            }
            if(vowel.find(i) == std::string::npos) {
                if(c_max_count < chars[i]) c_max_count = chars[i];
            } else {
                if (v_max_count < chars[i]) v_max_count = chars[i];
            }
        }
        return v_max_count + c_max_count;
    }
};