#include <iostream>
#include <vector>
using namespace std;
 
int main() {
    int n, sum = 0;
    cin >> n;
    vector<int> v(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> v[i];
    }

    for (int i = 1; i <= n; i++) {
        if (i % 2 == 1) {
            sum += v[i];
        }
    }
    cout << sum;
}