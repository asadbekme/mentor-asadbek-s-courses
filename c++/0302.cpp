#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double x;
    cin >> x;

    double S = exp(2) + exp(x) / 12 + pow(2, x + 1) + log(pow(x, x + 20)) / log(x);
    printf("%.2f", S);
}
