#include<bits/stdc++.h>
using namespace std;

int main() {
    int x, y, a, b;
    cin >> x >> y >> a >> b;

    double s = 0, p = 1, sp = 0, p1 = 1;
    for (int a = 1; a <= x; a++) {
        s += 1.0 * (pow(a, 2) + 2 * a) / (pow(a, 3) + a * pow(cos(a), 2) + 1);
    }

    for (int i = 1; i <= y; i++) {
        p *= 1.0 * (pow(i, 2) + 1) / (pow(i, 3.0 / i) + 2);
    }

    for (int i = 1; i <= a; i++) {
        for (int k = 1; k <= b; k++) {
            p1 *= log(1.0 * (pow(k, i) + pow(k, 1.0 / i)) / (pow(k, 3) + pow(i, 1.0 / k)));
        }
        sp += p1;
        p1 = 1;
    }
    printf("%.2f %.2f %.2f", s, p, sp);
}