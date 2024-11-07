#include<bits/stdc++.h>
using namespace std;

int main() {
    int x, y, a, b;
    cin >> x >> y >> a >> b;

    double s = 0, p = 1, sp = 0, p1 = 1;

    for (int k = 1; k <= x; k++) {
        s += 1.0 * (pow(k, 2) + sin(k) + 5) / pow(pow(k, 7) + 1, 1.0 / 5);
    }

    for (int n = 1; n <= y; n++) {
        p *= 1.0 * (n + sqrt(n)) / (n - pow(n + 1, 1 / 5.0));
    }

    for (int k = 1; k <= a; k++) {
        for (int i = 1; i <= b; i++) {
            p1 *= 1.0 * (pow(i, 2) + pow(k, 2.0 / i)) / ((sin(i) + cos(k)) * pow(i, k));
        }
        sp += p1;
        p1 = 1;
    }

    printf("%.2f %.2f %.2f", s, p, sp);
}