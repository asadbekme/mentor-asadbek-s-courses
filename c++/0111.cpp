#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> array(n);
    for (int i = 0; i < n; i++) {
        cin >> array[i];
    }
    
    int s = 0;
    double p = 1;
    for (int i = 0; i < n; i++) {
        if ((i + 1) % 2 != 0) {
            p *= array[i];
        } else {
            s += array[i];
        }
    }
    double result = p / s;
    printf("%.2f", result);
}