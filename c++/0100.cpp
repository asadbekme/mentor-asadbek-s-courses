#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int x, y, c, d;
    cin >> x >> y >> c >> d;
    double s = 0, p = 1, p1 = 1, sp = 1;

    int a = 1;
    while (a <= x) {
        s += 1.0 * (a * x + 4) / (sqrt(a + log(6)));
        a += 1;
    }

    int b = 1;
    while (b <= y) {
        p *= 1.0 * (b * pow(x, 2) + 6) / (sin(b * x));
        b += 1;
    }

    int i = 1;
    while (i <= c) {
        int j = 1;
        while (j <= d) {
            p1 *= 1.0 * (i * j + y * x) / pow(j * x + y, i / 2.0);
            j += 1;
        }
        sp *= p1;
        p1 = 1;
        i += 1;
    }

    printf("%.2f %.2f %.2f", s, p, sp);
}