#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> array(n);
    for (int i = 0; i < n; i++) {
        cin >> array[i];
    }

    int min_value = *min_element(array.begin(), array.end());
    vector<int> new_array;
    for (int element : array) {
        if (element < 0) {
            new_array.push_back(pow(min_value, 2));
        } else {
            new_array.push_back(element);
        }
    }

    for (int i = 0; i < n; i++) {
        cout << new_array[i] << " ";
    }
}
