#include <iostream>
#include <cmath>
using namespace std;

double f(double x) {
    return exp(x) - 2*cos(x);
}

struct result {
    double xm, fxm;
    int k;
};

result* bissection(double a, double b, double error) {
    int k = 0;
    double xm = (a + b) / 2;
    while (abs(f(xm)) > error) {
        k++;
        if (f(a)*f(xm)<0) {
            b = xm; 
        } else {
            a = xm;
        }
        xm = (a + b) / 2;
    }
    result * res = new result;
    res->xm = xm;
    res->fxm = f(xm);
    res->k = k; 
    return res;
}

int main() {
    cout << "Bissection method" << endl;
    cout << "f(x) = exp(x) - 2*cos(x)" << endl;
    cout << "Interval: [-2, 2]" << endl;
    cout << "Error: 10**(-15)" << endl;
    result* res = bissection(-2, 2, 1e-15);
    cout << "xm = " << res->xm << endl;
    cout << "f(xm) = " << res->fxm << endl;
    cout << "Iterations: " << res->k << endl;
    delete res;
    return 0;
}