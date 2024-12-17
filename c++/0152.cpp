#include <iostream>
#include <string>
using namespace std;

int main() {
    string text;
    getline(cin, text);

    int length = text.length();
    for (int i = length - 1; i >= 0; i--) {
        cout << text[i];
    }
}