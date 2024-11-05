#include <iostream>
using namespace std;

int main() {
    double a;
    cin >> a;

    if (a <= 1) {
        printf("%.2f", abs(a));
    } else if (a > 1 && a <= 2) {
        printf("%.2f", 1.0);
    } else {
        printf("%.2f", -2 * a + 5);
    }
}