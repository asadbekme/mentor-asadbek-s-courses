#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int x, y, c, d;
    cin >> x >> y >> c >> d;
    double s = 0, p = 1, sp = 0, p1 = 1;

    for (int n = 1; n <= x; n++) {
        s += 1.0 / (5 - 17 * n + pow(n, 3));
    }

    for (int m = 1; m <= y; m++) {
        p *= 1.0 * sqrt(abs(m - 5) + 1) / (pow(m, 2) + 4 * m - 1);
    }

    for (int i = 1; i <= c; i++) {
        for (int k = 1; k <= d; k++) {
            p1 *= pow(-1, i) * 1.0 * pow(abs(sin(k) + exp(k)), 1 / 7.0) / (2 * abs(4 * pow(i, 3) - pow(k, 4)));
        }
        sp += p1;
        p1 = 1;
    }
    printf("%.2f %.2f %.2f", s, p, sp);
}