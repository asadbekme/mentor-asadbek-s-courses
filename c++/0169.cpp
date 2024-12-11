#include <iostream>
using namespace std;

double max_value(double a, double b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

double min_value(double a, double b) {
    if (a < b) {
        return a;
    } else {
        return b;
    }
}

int main() {
    double a, b;
    cin >> a >> b;
    double u = min_value(a, b);
    double v = min_value(a * b, max_value(a, b));
    double s = min_value(u + v, 3.14);
    printf("%.2f %.2f %.2f", u, v, s);
}