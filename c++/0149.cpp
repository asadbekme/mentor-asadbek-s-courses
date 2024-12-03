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
    int count = 0;
    vector<string> na_words;
    for (int i = 0; i < words.size(); i++) {
        if (words[i][words[i].length() - 2] == 'N' && words[i][words[i].length() - 1] == 'A') {
            count += 1;
            na_words.push_back(words[i]);
        }
    }
    cout << count << endl;
    for (string element : na_words) {
        cout << element << " ";
    }
    return 0;
}