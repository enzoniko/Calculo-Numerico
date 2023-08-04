#include <iostream>
#include <cmath>
using namespace std;
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
        cout << "Não há raízes no intervalo dado" << endl;
        return NULL;
    }
    double k = 0.0;
    double xk = a;
    double fxk = f(xk);
    double dfxk = df(xk);
    while (abs(fxk) > error) {
        if (dfxk == 0) {
            cout << "Derivada igual à zero" << endl;
            return NULL;
        }
        xk = xk - (fxk/dfxk);
        fxk = f(xk);
        dfxk = df(xk);
        k++;
    }
    double* result = new double[3];
    result[0] = xk;
    result[1] = fxk;
    result[2] = k;

    return result;  
}

int main() {
    double* result = newton(0, 2, pow(10, -15));
    if (result != NULL) {
        cout.precision(16);
        cout << result[0] << endl;
        cout << result[1] << endl;
        cout << result[2] << endl;
    
        delete [] result;
    }
    return 0;
}