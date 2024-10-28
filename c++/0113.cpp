#include <iostream>
#include <vector>
using namespace std;  

int main() {
    int n, sum = 0, count = 0;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }
    
    for (int element : v) {
        if (element < 0) {
            sum += element;
            count += 1;
        }
    }
    double average = 1.0 * sum / count;
    if (count > 0) {
        printf("%.2f", average);
    } else {
        cout << "0.00";
    }
}