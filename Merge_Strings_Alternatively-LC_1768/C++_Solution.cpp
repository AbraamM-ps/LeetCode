class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string combinedWord = "";
        int len = std::max(word1.length(), word2.length());
        for (int i = 0; i < len; i++){
            if (i < word1.length()){
                combinedWord += word1[i];
            }
            if (i < word2.length()){
                combinedWord += word2[i];
            }
        }
        return combinedWord;

        // Space Complexity: O(T)
        // Time Complexity: O(T)
    }
};
