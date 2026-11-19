from custom_exception import DimensionMissMatch

class Vector:

    def __init__(self, vector):
        self.vector = vector.copy()

    def __repr__(self):
        return f"{self.vector}"

    def __add__(self, other)->'Vector':
        if len(self.vector) == 0 or len(other.vector) == 0:
            raise ValueError("No operation can be done with 0 dimensional vector")
        elif len(self.vector) != len(other.vector):
            raise DimensionMissMatch("Vectors must have same length.")
        else:
            result = [a+b for a,b in zip(self.vector, other.vector)]
            return Vector(result)

    def __sub__(self, other)->'Vector':
        if len(self.vector) == 0 or len(other.vector) == 0:
            raise ValueError("No operation can be done with 0 dimensional vector")
        elif len(self.vector) != len(other.vector):
            raise DimensionMissMatch("Vectors must have same length.")
        else:
            result = [a-b for a,b in zip(self.vector, other.vector)]
            return Vector(result)

    def __mul__(self, other)->int|float:
        if len(self.vector) == 0 or len(other.vector) == 0:
            raise ValueError("No operation can be done with 0 dimensional vector")
        elif len(self.vector) != len(other.vector):
            raise DimensionMissMatch("Vectors must have same length.")
        else:
            curr_sum = 0
            for i in range(len(self.vector)):
                temp = self.vector[i]*other.vector[i]
                curr_sum+=temp
            return float(curr_sum)

    def magnitude(self)->int|float:
        if len(self.vector) == 0:
            raise ValueError("No element in this vector")
        else:
            curr_sum = sum(self.vector[i]**2 for i in range(len(self.vector)))
            mag = curr_sum**0.5
            return mag

if __name__ == "__main__":
    a = Vector([2,3,4])
    b = Vector([5,6,7])
    c = Vector([9,10])

    print(a+b)
    print(a-b)
    print(a*b)
    print(a-c)
