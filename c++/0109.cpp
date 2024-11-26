#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n;
    vector<int> array(n);
    for (int i = 0; i < n; i++) {
        cin >> array[i];
    }
    cin >> m;
    
    double p = 1;
    for (int i = 0; i < n; i++) {
        if (array[i] > m) {
            p *= array[i];
        }
    }
    printf("%.2f", log(p));
}