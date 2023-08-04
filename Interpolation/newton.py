from functools import lru_cache

def pol_newton(xs, ys):
    a = []
    @lru_cache
    def dividedDifferences(xs, ys, s):
        if len(xs) == 1:
            return ys[0]
        else:
            d = dividedDifferences(xs[:-1], ys[:-1], s)
            if xs[:-1][0] == s:
                a.append(d)
            r =  (dividedDifferences(xs[1:], ys[1:], s) - d)/(xs[-1] - xs[0])
            return r
        
    r = dividedDifferences(tuple(xs), tuple(ys), xs[0])
    a.append(r)
    s = "lambda x: "
    for i in range(len(xs)):
        h = ""
        for j in range(i):
            h += "*(" + "x - " + str(xs[j])  + ")"
        s += "( " + str(a[i]) + h + ") +"  

    print(s[:-1])
    return eval(s[:-1])

def evaluate_point(p, x):
    
    return p(x)

xs = [0, 0.5, 1]
ys = [-1, -1.14872, -1.71828]
# xs = [-3, -2, 1, 3]
# ys = [-1, 2, -1, 10]

p = pol_newton(xs, ys)
print(evaluate_point(p, 0.7))
