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

    int highest_element = array[0];
    for (int i = 0; i < n; i++) {
        if (array[i] > highest_element) {
            highest_element = array[i];
        }
    }

    for (int element : array) {
        printf("%.2f ", 1.0 * element / highest_element);
    }
}