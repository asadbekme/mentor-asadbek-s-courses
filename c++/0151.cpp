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
    string vowels = "AaOoIiUuEe";
    int count = 0;
    for (int i = 0; i < words.size(); i++) {
        for (int j = 0; j < words[i].length(); j++) {
            if (vowels.find(words[i][j]) != string::npos) {
                count += 1;
            }
        }
    }
    cout << count << endl;
    return 0;
}