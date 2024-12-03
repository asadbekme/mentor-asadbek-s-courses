#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    getline(cin, s);

    // variable to store token obtained from the original string
    string word;

    // constructing stream from the string
    stringstream ss(s);
 
    // declaring vector to store the string after split
    vector<string> words;
 
    // using while loop until the getline condition is satisfied
    // ' ' represent split the string whenever a space is
    // found in the original string
    while (getline(ss, word, ' ')) {
        // store token string in the vector
        words.push_back(word);
    }

    for (int i = 0; i < words.size(); i++) {
        if (words[i][0] == 'A') {
            cout << words[i] << endl;
        }
    }
    return 0;
}