#include <iostream>
#include <string>
using namespace std;

int main() {
  string s;
  getline(cin, s);
  int s1 = 0, s2 = 0;

  for (int i = 0; i < s.size(); i++) {
    if (s[i] == 'A') {
        s1 += 1;
    }
    if (s[i] == 'Y') {
        s2 += 1;
    }
  }
  cout << s1 << endl;
  cout << s2;
}