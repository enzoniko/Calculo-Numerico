#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double f(double x) {
    return exp(x) - (2 * cos(x));
}

double* secante(double a, double b, double error) {
    double k = 0.0;
    double xkm1 = a;
    double xk = b;
    double fxkm1 = f(xkm1);
    double fxk = f(xk);
    double xkp1 = xk - (((xk - xkm1)*fxk) / (fxk - fxkm1));
    double fxkp1 = f(xkp1);

    while (fabs(fxkp1) > error) {
        xkm1 = xk;
        xk = xkp1;
        fxkm1 = f(xkm1);
        fxk = f(xk);
        xkp1 = xk - (((xk - xkm1)*fxk) / (fxk - fxkm1));
        fxkp1 = f(xkp1);
        k++;
    }
    double* result = (double *) malloc(3*sizeof(double));
    result[0] = xkp1;
    result[1] = fxkp1;
    result[2] = k;
    return result;
}

int main() {
    double* result = secante(0, 2, pow(10, -15));
    if (result != NULL) {
        printf("%.16Lf\n", result[0]);
        printf("%.16Lf\n", result[1]);
        printf("%f\n", result[2]);
        free(result);
    } else printf("Something went wrong!");
    return 0;
}
