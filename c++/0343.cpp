#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    getline(cin, s);
    string upper_letters = "";

    for (char letter : s) {
        if (isupper(letter)) {
            upper_letters += letter;
        }
    }

    if (!upper_letters.empty()) {
        cout << upper_letters << endl;
    } else {
        cout << -1 << endl;
    }

    return 0;
}
