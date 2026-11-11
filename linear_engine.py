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
                return result
            else:
                return f"Dimension did not matched."
        except Exception as e:
            return f"Error: {e}"

    def dot(self, B):
        try:
            if len(self.vector) == 0 or len(B.vector) == 0:
                raise ValueError("No Operation can be applied in blank vector.")
            elif len(self.vector) == len(B.vector):
                    result = 0
                    for i in range(len(self.vector)):
                        temp = self.vector[i] * B.vector[i]
                        result+=temp
                return result
            else:
                return f"Dimension did not matched."
        except Exception as e:
            return f"Error: {e}"
    
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
                return result
            else:
                return f"Dimension did not matched."
        except Exception as e:
            return f"Error: {e}"
                

    @staticmethod
    def cosine_similarity(x: float|int, y: float|int)->float|int:
        from math import acos
        theta = acos(x/y)
        return theta






