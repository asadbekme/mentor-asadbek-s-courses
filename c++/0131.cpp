#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int matrix[n][m];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> matrix[i][j];
        }
    }

    int column_sums[m], max_value = matrix[0][0], min_value = matrix[0][0];
    for (int j = 0; j < m; j++) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += matrix[i][j];
        }
        column_sums[j] = sum;
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (matrix[i][j] > max_value) {
                max_value = matrix[i][j];
            }
            if (matrix[i][j] < min_value) {
                min_value = matrix[i][j];
            }
        }
    }
    for (int sum : column_sums) {
        cout << sum << " ";
    }
    cout << endl << max_value << " " << min_value;
}