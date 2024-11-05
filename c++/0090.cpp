#include<bits/stdc++.h>
using namespace std;

int main() {
    double a, b, c;
    cin >> a >> b >> c;
    double x = -M_PI, h = M_PI / 10.0, y = 0;

    while (x <= M_PI) {
        y += (log(pow(a, 2 * sin(x))) + exp(2 * x)) / (atan(x) + b) + c;
        x += h;
    }
    printf("%.2f", y);
}