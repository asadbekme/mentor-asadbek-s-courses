#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int a, b, h;
    cin >> a >> b >> h;
    double S = M_PI * (a + b) / 2.0 * sqrt(pow(h, 2) + pow((a - b) / 2.0, 2)) + M_PI * (pow(a, 2) + pow(b, 2)) / 4.0;
    printf("%.2f", S);
}