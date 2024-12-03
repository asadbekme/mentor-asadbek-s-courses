#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    getline(cin, s);

    string word;
    stringstream ss(s);
    vector<string> words;
    while (getline(ss, word, ' ')) {
        words.push_back(word);
    }
    vector<string> info_words;
    for (int i = 0; i < words.size(); i++) {
        string w = words[i];
        transform(w.begin(), w.end(), w.begin(), ::tolower);
        if (w.find("info") != string::npos) {
            info_words.push_back(words[i]);
        }
    }
    for (string element : info_words) {
        cout << element << " ";
    }
    return 0;
}