from exception_class import InvalidDimension, OperationalError

class Vector:

    def __init__(self, vector):
        self.vector = vector.copy() #shallow copy: to avoid data manupulation from outside


    def add(self,B):
        try:
            if len(self.vector) == 0 or len(B.vector) == 0:
                raise ValueError("No Operation can be applied in blank vector.")
            elif len(self.vector) == len(B.vector):
                result = []
                for i in range(len(self.vector)):
                    result.append(self.vector[i]+B.vector[i])
                return Vector(result)
            else:
                return f"Dimension did not matched."
        except Exception as e:
            raise OperationalError(f"{e}")

    def dot(self, B):
        try:
            if len(self.vector) == 0 or len(B.vector) == 0:
                raise ValueError("No Operation can be applied in blank vector.")
            elif len(self.vector) == len(B.vector):
                    result = 0
                    for i in range(len(self.vector)):
                        temp = self.vector[i] * B.vector[i]
                        result+=temp
                    return Vector(result)
            else:
                return f"Dimension did not matched."
        except Exception as e:
            raise OperationalError(f"{e}")
    
    def magnitude_product(self, B):
        try:
            if len(self.vector) == 0 or len(B.vector) == 0:
                raise ValueError("No Operation can be applied in blank vector.")

            elif len(self.vector) == len(B.vector):
                a = 0
                b = 0
                for i in range(len(self.vector)):
                    temp_a = (self.vector[i]**2)
                    temp_b = (B.vector[i]**2)
                    a+=temp_a
                    b+=temp_b
                result = (a**0.5)*(b**0.5)
                return Vector(result)
            else:
                return f"Dimension did not matched."
        except Exception as e:
            raise OperationalError(f"{e}")

    @staticmethod
    def cos_similarity(A,B):
        dot_product = A.dot(B)
        magnitude_product = A.magnitude_product(B)

        if magnitude_product == 0:
            raise ValueError("Cosine similarity is undefined for zero vectors.")

        return dot_product/magnitude_product

    @staticmethod
    def angle(x: int|float)-> int|float:
        from math import acos
        theta = acos(x)
        return theta


    def __add__(self, other):
        try:

            if len(self.vector) == 0 or len(other.vector) == 0:
                raise ValueError("No operation can be applied on zero vector")
            elif len(self.vector) != len(other.vector):
                raise InvalidDimension("Dimension Mismatched.")
            elif len(self.vector) == len(other.vector):
                result = []
                for i in range(len(self.vector)):
                    result.append(self.vector[i] + other.vector[i])
                return Vector(result)
        except Exception as e:
            raise OperationalError(f"{e}")




