def pol_lagrange(xs):
    l = [0]*len(xs)
    for i in range(len(xs)):
        s = "lambda x: "
        for j in range(len(xs)):
            if i != j:
                s += "((x - " + str(xs[j]) + ") / (" + str(xs[i]) + " - " + str(xs[j]) + ")" + ") * "
        print(i, s[:-3])
        l[i] = eval(s[:-3])

    return l

def lagrange(xs, ys, x):
    l = [1]*len(xs)
    for i in range(len(xs)):
        num = 1
        den = 1
        for j in range(len(xs)):
            if i != j:
                num *= x - xs[j]
                den *= xs[i] - xs[j]
        l[i] = num/den

    y = 0
    for i in range(len(xs)):
        y += ys[i]*l[i]
    return y

x = [0, 0.5, 1]
y = [-1, -1.14872, -1.71828]
def point_evaluation(p, y, x):
    result = 0
    for i in range(len(y)):
        result += p[i](x)*y[i]
    print(result)

p = pol_lagrange(x)
point_evaluation(p, y, 0.7)

