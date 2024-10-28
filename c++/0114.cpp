#include<bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[n+1];
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    
    double p = 1, x;
    for (int i = 1; i <= n; i++) {
        if (a[i] % 2 == 0 || a[i] % 5 == 0) {
            p *= a[i];
        }
        x = sin(p);
    }
    printf("%.2f ", x);
}