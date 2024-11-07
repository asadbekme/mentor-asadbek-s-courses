#include<bits/stdc++.h>
using namespace std;

int main() {
    double x, y;
    cin >> x >> y;
    
    if ((y >= -2 and x >= -1 and x <= 1 and y <= 0) or (x >= -1 and x <= 1 and y <= abs(x))) {
        cout << "yes";
    } else {
        cout << "no";
    }
}