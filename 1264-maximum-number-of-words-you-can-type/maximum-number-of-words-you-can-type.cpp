class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        string word;
        stringstream ss(text); // stream the string(Make the String into Pieces )
        int count=0;

        while (ss >> word) {
            bool canType = true;
            for (char c : brokenLetters) {
                // String::npos Means It is Not found
                if (word.find(c) != string::npos) { // broken letter found
                    canType = false;
                    break;
                }
            }
            if (canType)
                count++;
        }
        return count;
    }
};
