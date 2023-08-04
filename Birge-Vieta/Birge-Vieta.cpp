#include <iostream>
#include <cmath>
using namespace std;    
double birgeVieta(double* a, double x0, int n, double error) {
    double xk = x0;
    int k = 0;
    double* b = new double[n];
    double* c = new double[n - 1];
    for (int i = 0; i < n; i++) b[i] = a[i];
    for (int i = 0; i < n - 1; i++) c[i] = a[i];
    while (abs(b[n-1]) > error) {
        for (int i = 0; i < n - 1; i++) {
            b[i] = a[i] + xk*b[i - 1];
            c[i] = b[i] + xk*c[i - 1];
        }

        b[n - 1] = a[n - 1] + xk*b[n - 2];
        xk = xk - (b[n-1]/c[n - 2]);
        k++;
    }
    cout.precision(16);
    cout << "k: " << k << endl;
    cout << "f(raiz): " << b[n-1] << endl;
    cout << "Raiz: " << xk << endl;
    return b[n - 1];
}

int main() {
    int n = 4;

    double a[4] = {1, 0, 2, -1};
    //printf("%d", sizeof(a)/sizeof(a[0]));
    birgeVieta(a, 1, sizeof(a)/sizeof(a[0]), pow(10, -15));
    return 0;
}