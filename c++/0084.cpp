#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    double x = -1.0, h = 0.25, y = 0;

    while (x <= 1.0) {
        y += pow((sin(a * x) + pow(b, c)) / (pow(b, 2) + pow(cos(x), 2)), 1/3.0) - 1.0 * sin(pow(x, 2)) / (a * b);
        x += h;
    }
    printf("%.2f", y);
}