#include <iostream>
#include <cmath>
using namespace std;

int sum_of_array(int array[], int start, int end) {
    int sum = 0;
    for (int index = start - 1; index < end; index++) {
        sum += array[index];
    }
    return sum;
}

int main() {
    int n, k, m;
    cin >> n;
    int array[n];
    for (int i = 0; i < n; i++) {
        cin >> array[i];
    }
    cin >> k >> m;
    double result = 1.0 * (sum_of_array(array, 1, m - k) + sum_of_array(array, 1, k)) / pow(sum_of_array(array, 1, m) - sum_of_array(array, 1, 4), 2);
    printf("%.2f", result);
}