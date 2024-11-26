#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio> // printf uchun kerak
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> array(n);
    for (int i = 0; i < n; i++) {
        cin >> array[i];
    }
    int a, b;
    cin >> a >> b;

    // Eng kichik qiymatni topish
    int min_value = *min_element(array.begin(), array.end());

    // a dan b gacha bo'lgan elementlarni min_value ga bo'lish
    for (int index = 0; index < n; index++) {
        if (index >= a - 1 && index <= b - 1) {
            double x = static_cast<double>(array[index]) / min_value;

            // Agar oxirgi raqam 5 bo'lsa, yuqoriga qarab yaxlitlash
            if (static_cast<int>(x * 100) % 10 == 5) {
                x = ceil(x * 10) / 10.0;
            }

            // Qiymatni yangi hisoblangan x bilan almashtirish
            array[index] = static_cast<int>(round(x * 10)); // 0.1 aniqlik uchun 10 ga ko'paytirib saqlaymiz
        }
    }

    // Natijalarni chop etish
    for (int index = 0; index < n; index++) {
        if (index >= a - 1 && index <= b - 1) {
            printf("%.1f ", array[index] / 10.0); // Yaxlitlangan qiymatni qaytarish
        } else {
            printf("%.1f ", static_cast<double>(array[index]));
        }
    }
    cout << endl;
    return 0;
}
