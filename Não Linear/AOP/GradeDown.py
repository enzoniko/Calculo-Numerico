from AOP.Rho import Reshape
from AOP.Tally import Tally
def GradeDown(vector):
    vector = Reshape([Tally(vector)], vector)
    # Return a list of indices which would sort the vector in descending order
    return sorted(range(len(vector)), key=lambda k: vector[k], reverse=True)
