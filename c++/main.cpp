#include <iostream> 
#include <string>
using namespace std;

int main() {
    string s1, s2, result;
    getline(cin, s1);
    getline(cin, s2);
    
    int maxLength = max(s1.size(), s2.size());
    for (int i = 0; i < maxLength; i++) {
        if (i < s1.size()) {
            result += s1[i];
        }
        if (i < s2.size()) {
            result += s2[i];
        }
    }
    cout << result;
}