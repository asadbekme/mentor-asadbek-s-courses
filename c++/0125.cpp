#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n, k, l;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    cin >> k >> l;
    
    int sum = 0;
    for (int i = k - 1; i < l; i++) {
        sum += pow(a[i], 3);
    }
    cout << sum;
}
