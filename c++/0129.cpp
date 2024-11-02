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

    int s = 0;
    for (int element : array) {
        if (element % 2 == 0 || element % 3 == 0 || element % 5 == 0) {
            s += element;
        }
    }
    cout << s;
}
