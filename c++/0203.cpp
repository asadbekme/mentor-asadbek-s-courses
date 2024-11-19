// * 1-st way
#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n, m;
    cin >> n;
    vector<int> array(n);
    for (int i = 0; i < n; i++){
        cin >> array[i];
    }
    cin >> m;
    vector<int> new_array(m);
    int i = 1;
    while (i <= m) {
        int l, r, p;
        cin >> l >> r >> p;
        long long pp = 1;
        for (int j = l - 1; j < r; j++) {
            pp = (pp * array[j]) % p; 
        }
        new_array[i - 1] = pp;
        i += 1;
    }

    for (int element : new_array) {
        cout << element << endl;
    }
}


// * 2-nd way
// #include <iostream>
// #include <vector>
// using namespace std;

// int main() {
//     int n;
//     cin >> n;
//     vector<int> array(n);
//     for (int i = 0; i < n; i++) {
//         cin >> array[i];
//     }

//     int m;
//     cin >> m;
//     vector<int> new_array;
//     for (int i = 0; i < m; i++) {
//         int l, r, p;
//         cin >> l >> r >> p;
//         long long pp = 1;
//         for (int j = l - 1; j < r; j++) {
//             pp = (pp * array[j]) % p;
//         }
//         new_array.push_back(pp); 
//     }

//     for (int result : new_array) {
//         cout << result << endl;
//     }
//     return 0;
// }
