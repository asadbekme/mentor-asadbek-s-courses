#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, x, y, count = 0;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }
    cin >> x >> y;

    for (int i = 0; i < n; i++) {
        if (!(v[i] >= x && v[i] <= y)) {
            count += 1;
        }
    }
    cout << count;
}