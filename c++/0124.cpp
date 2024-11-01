#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, k;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    cin >> k;

    int max_element = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] > max_element) {
            max_element = a[i];
        }
    }
    vector<int> b;
    for (int i = 0; i < n; i++) {
        if (a[i] == max_element) {
            b.push_back(a[k - 1]);
        } else {
            b.push_back(a[i]);
        }
    }
    b[k - 1] = max_element;
    for (int i = 0; i < n; i++) {
        cout << b[i] << " ";
    }
    return 0;
}
