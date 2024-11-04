// * 1-st way
// #include <iostream>
// #include <cmath>
// using namespace std;

// int main() {
//     int a, b, c;
//     cin >> a >> b >> c;
//     double x = 5.0, h = 0.5, y = 0;

//     while (x <= 10) {
//         y += (pow(a, 2) + b * x + pow(x, c)) / (pow(a, 2) + pow(b, 2) + pow(x, 2));
//         x += h;
//     }
//     printf("%.2f", y);
// }

// * 2-nd way
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    double h = 0.5, y = 0;

    for (double x = 5.0; x <= 10; x += h) {
        y += (pow(a, 2) + b * x + pow(x, c)) / (pow(a, 2) + pow(b, 2) + pow(x, 2));
    }
    printf("%.2f", y);
}