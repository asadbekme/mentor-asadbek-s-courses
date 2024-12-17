#include <bits/stdc++.h>
using namespace std;
int main() {
    string text;
    getline(cin, text);

    string word;
    stringstream ss(text);
    vector<string> words;
    while (getline(ss, word, ' ')) {
        words.push_back(word);
    }
    
    int count = 0;
    for (int i = 0; i < words.size(); i++) {
        if (isupper(words[i][0])) {
            count += 1;
        }
    }
    cout << count << endl;
    return 0;
    
}