#include <iostream>
#include <cmath>
using namespace std;

double G(double a, double b) {
    double result = (pow(a, 2) + pow(b, 2)) / (pow(a, 2) + 2 * a * b + 3 * pow(b, 2) + 4);
    return result;
}

int main() {
    double t, s;
    cin >> t >> s;
    double value = G(1.2, s) + G(t, s) + G(2 * s - 1, s * t);
    printf("%.2f", value);
}