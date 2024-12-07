#include<iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int main() {
    int a, b, c;
    vector<int> numbers(3);
    cin >> numbers[0] >> numbers[1] >> numbers[2];
    sort(numbers.begin(), numbers.end());
    a = numbers[0];
    b = numbers[1];
    c = numbers[2];

    if (pow(a, 2) + pow(b, 2) == pow(c, 2)) {
        cout << 1;
    } else if (a == b && b == c && a == c) {
        cout << 3;
    } else if (a == b || a == c || b == c) {
        cout << 2;
    } else {
        cout << 4;
    }
}