#include <iostream>
#include <cmath>
using namespace std;

long long factorial(int n) {
    long long p = 1;
    for (int i = 1; i <= n; i++) {
        p *= i;
    }
    return p;
}

double t(double x) {
    double s1 = 0, s2 = 0;
    for (int k = 0; k <= 10; k++) {
        s1 += pow(x, 2 * k + 1) / factorial(2 * k + 1);
    }
    for (int i = 0; i <= 10; i++) {
        s2 += pow(x, 2 * i) / factorial(2 * i);
    }
    double result = s1 / s2;
    return result;
}

int main() {
    double y;
    cin >> y;
    double value = (1.7 * t(0.25) + 2 * t(y + 1)) / (6 - t(pow(y, 2) - 1));
    printf("%.2f", value);
}