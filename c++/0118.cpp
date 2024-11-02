#include <iostream>
#include <vector>
using namespace std;
 
int main() {
    int n, sum = 0, count = 0;
    cin >> n;
    vector<int> array(n);
    for (int i = 0; i < n; i++) {
        cin >> array[i];
    }
    
    for (int element : array) {
        if (element % 2 == 1) {
            sum += element;
            count += 1;
        }
    }
    if (count > 0) {
        printf("%.2f", 1.0 * sum / count);
    } else {
        cout << "0.00";
    }
}