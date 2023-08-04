from AOP.Rho import Shape, Reshape
from AOP.Tally import Tally
from math import log
from AOP.helpers import verify_args

def Log(vector):
    vector = verify_args(vector)
    return Reshape(Shape(vector), map(log, Reshape([Tally(vector)], vector)))
