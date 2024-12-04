#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int array[n];
    for (int i = 0; i < n; i++) {   
        cin >> array[i];
    }
    int sorted_array[n];
    for (int i = 0; i < n; i++) {
        sorted_array[i] = array[i];
    }
    sort(sorted_array, sorted_array + n);
    for (int element : sorted_array) {
        cout << element << " ";
    }
}