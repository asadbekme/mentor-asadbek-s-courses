#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double a;
    cin >> a;

    if (a <= -1) {
        printf("%.2f", 1 / (pow(a, 2)));
    } else if (a >= -1 && a < 2) {
        printf("%.2f", pow(a, 2));
    } else {
        printf("%.2f", 4.0);
    }
}