#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double a;
    cin >> a;
    
    if (a < 0) {
        printf("%.2f", -a);
    } else if (a == 0) {
        printf("%.2f", 0.0);
    } else {
        printf("%.2f", -pow(a, 2));
    }
}