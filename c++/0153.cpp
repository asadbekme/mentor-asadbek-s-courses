// * 1-st way
// #include <bits/stdc++.h>
// using namespace std;
// int main() {
//     string text;
//     getline(cin, text);

//     string word;
//     stringstream ss(text);
//     vector<string> words;
//     while (getline(ss, word, ' ')) {
//         words.push_back(word);
//     }
    
//     for (int i = 0; i < words.size(); i++) {
//         cout << words[i] << " " << words[i].length() << endl;
//     }
// }

// * 2-nd way
#include <bits/stdc++.h>
using namespace std;
int main() {
    string text;
    getline(cin, text);

    stringstream ss(text);
    string word;

    while (ss >> word) {
        cout << word << " " << word.length() << endl;
    }
    return 0;
}