#include <stdio.h>
#include <math.h>
#include <stdlib.h>
double f(double x) {
    return exp(x) - (2 * cos(x));
}

double df(double x) {
    return exp(x) + (2 * sin(x));
}

double* newton(double a, double b, double error) {
    double fa = f(a);
    double fb = f(b);
    if (fa*fb > 0) {
        printf("Não há raízes no intervalo dado");
        return NULL;
    }
    double k = 0.0;
    double xk = a;
    double fxk = f(xk);
    double dfxk = df(xk);
    while (fabs(fxk) > error) {
        if (dfxk == 0) {
            printf("Derivada igual à zero");
            return NULL;
        }
        xk = xk - (fxk/dfxk);
        fxk = f(xk);
        dfxk = df(xk);
        k++;
    }
    double* result = (double *) malloc(3*sizeof(double));
    result[0] = xk;
    result[1] = fxk;
    result[2] = k;

    return result;  
}

int main() {
    double* result = newton(0, 2, pow(10, -15));
    if (result != NULL) {
        printf("%.16Lf\n", result[0]);
        printf("%.16Lf\n", result[1]);
        printf("%f\n", result[2]);
        free(result);
    }
    return 0;
}