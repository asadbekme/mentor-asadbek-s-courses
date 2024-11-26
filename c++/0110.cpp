#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> array(n);
    for (int i = 0; i < n; i++) {
        cin >> array[i];
    }
    int m, s = 0;
    cin >> m;
    
    for (int i = 0; i < n; i++) {
        if (array[i] > m) {
            s += array[i];
        }
    }
    cout << s;
}