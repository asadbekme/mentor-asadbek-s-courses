#include <bits/stdc++.h>
using namespace std;

int main() {
    double x, y;
    cin >> x >> y;
    if (y >= -1 && y <= 2 - abs(3 * x)) {
        cout << "yes";
    } else {
        cout << "no";
    }
}