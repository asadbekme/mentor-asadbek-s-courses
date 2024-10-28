#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n, m, sum = 0;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }
    cin >> m;

    for (int element : v) {
        if (element < m) {
            sum += pow(element, 2);
        }
    }
    cout << sum;
}