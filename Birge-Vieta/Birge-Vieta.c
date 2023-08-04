#include <stdio.h>
#include <math.h>
#include <stdlib.h>
double birgeVieta(double* a, double x0, int n, double error) {
    double xk = x0;
    int k = 0;
    double* b =(double *) malloc(sizeof(double) * n);
    double* c = (double *) malloc(sizeof(double)*(n-1));
    for (int i = 0; i < n; i++) b[i] = a[i];
    for (int i = 0; i < n - 1; i++) c[i] = a[i];
    while (fabs(b[n-1]) > error) {
        for (int i = 0; i < n - 1; i++) {
            b[i] = a[i] + xk*b[i - 1];
            c[i] = b[i] + xk*c[i - 1];
        }

        b[n - 1] = a[n - 1] + xk*b[n - 2];
        xk = xk - (b[n-1]/c[n - 2]);
        k++;
    }
    printf("k: %d\n", k);
    printf("f(raiz): %.16lf\n", b[n-1]);
    printf("Raiz: %.16lf\n", xk);
    return b[n - 1];
}

int main() {
    int n = 4;

    double a[4] = {1, 0, 2, -1};
    //printf("%d", sizeof(a)/sizeof(a[0]));
    birgeVieta(a, 1, sizeof(a)/sizeof(a[0]), pow(10, -15));
    return 0;
}