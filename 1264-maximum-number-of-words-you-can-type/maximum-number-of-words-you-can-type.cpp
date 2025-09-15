class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        int count = 0;
        bool check = true;
        for(auto i: text) {
            if(i == ' ') {
                if(check) ++count;
                check =true;
            } else if(brokenLetters.find(i) != string::npos) {
                check = false;
            }
        }
        if(check) ++count;
        return count;
    }
};