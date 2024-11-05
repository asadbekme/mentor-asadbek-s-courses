#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double a;
    cin >> a;

    if (a <= 0) {
        printf("%.2f", abs(a + 1));
    } else {
        printf("%.2f", abs(a - 1));
    }
}