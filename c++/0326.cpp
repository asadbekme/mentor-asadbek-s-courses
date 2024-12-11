#include <bits/stdc++.h>
using namespace std;

int main() {
    int x, y, c, d;
    cin >> x >> y >> c >> d;
    double s = 0, p = 1, p1 = 1, sp = 0;
    int i = 1;
    while (i <= x) {
        s += sqrt(c * i + d);
        i += 1;
    }
    int k = 1;
    while (k <= y) {
        p *= 1.0 * (sin(c + d) + 3 * c) / (cos(c * k) + 2.78 * d);
        k += 1;
    }
    int j = 1;
    while (j <= c) {
        int t = 1;
        while (t <= d) {
            p1 *= 1.0 * (c * pow(x, t) + j * t) / (d * j + c * t);
            t += 1;
        }
        sp += p1;
        p1 = 1;
        j += 1;
    }
    printf("%.2f %.2f %.2f", s, p, sp);
    return 0;
}