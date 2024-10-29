#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, a, b;
    cin >> n;
    vector<int> v(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> v[i];
    }
    cin >> a >> b;

    int minValue = v[1];
    for (int i = 1; i <= n; i++) {
        if (minValue > v[i]) {
            minValue = v[i];
        }
    }
    for (int i = 1; i <= n; i++) {
        if (i >= a && i <= b) {
            printf("%.1f" , 1.0 * v[i] / minValue);
        } else {
            printf("%.1f" , 1.0 * v[i]);
        }
    }
    cout << endl;
}