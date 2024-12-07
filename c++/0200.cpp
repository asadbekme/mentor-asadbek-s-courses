#include <iostream>
using namespace std;

int main() {
    int n, s = 0;
    cin >> n;
    int array[n];
    for (int i = 0; i < n; i++) {
        cin >> array[i];
    }
    
    for (int element : array) {
        s += element;
    }
    cout << s;
}