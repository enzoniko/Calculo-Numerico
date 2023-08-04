#include <iostream>
#include <cmath>
using namespace std;

double f(double x) {
    return exp(x) - 1;
}

struct result {
    double xk, fxk;
    int k; 
};

result* fakePos(double a, double b, double error) {
    int k = 0;

    double xk = a - ((f(a)*(b - a))/(f(b) - f(a)));

    while (abs(f(xk)) > error) {
        k++;

        if (f(a)*f(xk) < 0) {
            b = xk;
        } else {
            a = xk;
        }

        xk = a - ((f(a)*(b - a))/(f(b) - f(a)));
    }

    result* res = new result;
    res->xk = xk;
    res->fxk = f(xk);
    res->k = k;
    return res;
}

int main() {
    result* res = fakePos(-2, 2, 1e-15); 
    cout << "xk: " << res->xk << endl;
    cout << "fxk: " << res->fxk << endl;
    cout << "k: " << res->k << endl;
    delete res;
    return 0;
}