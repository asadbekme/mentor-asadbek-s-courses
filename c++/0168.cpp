#include <iostream>
using namespace std;

double max_value(double a, double b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

int main() {
    double a, b, c;
    cin >> a >> b >> c;
    double result = (max_value(a, a + b) + max_value(a, b + c)) / (1 + max_value(a + b * c, 1.15));
    printf("%.2f", result);
}