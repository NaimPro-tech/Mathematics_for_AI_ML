from exception.custom_exception import DimensionMissMatch, ZeroMagnitudeError
from validation.validation import validation_check_vector
from src.linear_algebra import LinearAlgebra
import copy

class Vector(LinearAlgebra):

    def __init__(self, vector):
        self.vector = copy.deepcopy(vector)
        if len(self.vector) == 0:
            raise DimensionMissMatch("Invalid Vector. Initialize the values.")


    def __repr__(self):
        return f"{self.vector}"

    def __len__(self):
        return len(self.vector)

    @property
    def shape(self):
        return (len(self.vector),)

    def __add__(self, other)->'Vector':
        validation_check_vector(self, other)
        result = [a+b for a,b in zip(self.vector, other.vector)]
        return Vector(result)

    def __sub__(self, other)->'Vector':
        validation_check_vector(self, other)
        result = [a-b for a,b in zip(self.vector, other.vector)]
        return Vector(result)

    def __mul__(self, other)->int|float:
        if isinstance(other, Vector):
            validation_check_vector(self, other)
            curr_sum = 0
            for i in range(len(self.vector)):
                temp = self.vector[i]*other.vector[i]
                curr_sum+=temp
            return float(curr_sum)
        else:
            if len(self.vector) == 0:
                raise ValueError("No operation can be done with 0 dimensional vector")
            new = []
            for i in range(len(self.vector)):
                new.append(self.vector[i]*other)
            return Vector(new)


    def magnitude(self:"Vector")->int|float:
        if len(self.vector) == 0:
            raise ValueError("No element in this vector")
        else:
            curr_sum = sum(self.vector[i]**2 for i in range(len(self.vector)))
            mag = curr_sum**0.5
            return mag
    
    def magnitude_product(self, other:"Vector")->int|float:
        mag_other = other.magnitude()
        mag_self = self.magnitude()
        return mag_self*mag_other

    def dot(self:"Vector", other:"Vector")->int|float:
        validation_check_vector(self, other)
        result = 0
        for i in range(len(self.vector)):
            result+= self.vector[i]*other.vector[i]
        return result

    def cosine_similarity(self, other):
        validation_check_vector(self, other)
        dot_product = self*other
        mag_product = self.magnitude_product(other)
        if mag_product == 0:
            raise ZeroMagnitudeError("Can't calculate cosine similarity.\nZero magnitude vectors have no defined direction.")
        result = dot_product/mag_product
        return result

    def projection(self, other):
        validation_check_vector(self, other)
        c = self.dot(other)
        d = other.dot(other)
        if d == 0:
            raise ZeroMagnitudeError("Can't Divide by zero.")
        result = c/d
        proj = other.scalar_multiplication(result)
        return proj
    
    def angle(self,other):
        validation_check_vector(self, other)
        from math import acos

        norm = self.cosine_similarity(other)
        theta = acos(norm)
        return theta

        

if __name__ == "__main__":
    a = Vector([2,3,4])
    b = Vector([5,6,7])
    c = Vector([9,10,11])
    d = Vector([1,1])
    e = Vector([1,0])
    print(a+b)
    print(a-b)
    print(a*b)
    print(a-c)
    print(a.magnitude_product(b))
    print(d.dot(e))
    print(a.angle(b))
    print(a*3)

