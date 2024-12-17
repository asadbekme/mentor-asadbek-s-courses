#include <iostream>
#include <string>
using namespace std;

int main() {
    string N;
    cin >> N;

    int sum = 0;
    for (char number : N) { 
        if (isdigit(number)) { // Agar raqam bo'lsa
            sum += number - '0'; // Belgini raqamga aylantirib yig'indiga qo'shamiz
        }
    }

    cout << sum << endl;
    return 0;
}
