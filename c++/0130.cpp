#include <iostream>
#include <vector>
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
    
    vector<int> row_sums(n);
    int s = 0, max_value = matrix[0][0], min_value = matrix[0][0];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            s += matrix[i][j];
            if (matrix[i][j] > max_value) {
                max_value = matrix[i][j];
            }
            if (matrix[i][j] < min_value) {
                min_value = matrix[i][j];
            }
        }
        row_sums[i] = s;
        s = 0;
    }
    for (int sum : row_sums) {
        cout << sum << " ";
    }
    cout << endl;
    cout << max_value << " " << min_value;
}