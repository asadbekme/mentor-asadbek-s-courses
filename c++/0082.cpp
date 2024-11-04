#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int x = 1, h = 3;
    double y = 0;

    while (x <= 10) {
        y += 1.0 * a * pow(x, 2) / b + 1.0 * x / c;
        x += h;
    }
    printf("%.2f", y);
}