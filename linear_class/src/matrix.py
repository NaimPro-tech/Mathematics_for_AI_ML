from custom_exception import DimensionMissMatch,IrregularMatrix, MatrixMultiplicationError

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix.copy()
        if len(self.matrix) == 0:
            raise ValueError("Invalid Matrix. Iniatialize the values.")
        self.__expected_length = len(self.matrix[0])
        for row in range(len(self.matrix)):    
            if len(self.matrix[row]) != self.__expected_length:
                raise IrregularMatrix("Class Matrix can't create irregular matrix.")

    def __repr__(self):
        return f"{self.matrix}"
    
    def __str__(self):
        rows = []
        for row in self.matrix:
            formatted_row = " ".join(str(num) for num in row)
            rows.append(formatted_row)

        return "\n".join(rows)

    def __add__(self, other):
        if len(self.matrix) == 0 or len(other.matrix) == 0:
            raise ValueError("Input should be matrix.")
        elif len(self.matrix[0]) != len(other.matrix[0]):
            raise DimensionMissMatch("Matrix Dimension miss matched.")
        elif len(self.matrix) != len(other.matrix):
            raise DimensionMissMatch("Matrix Dimension miss matched.")
        else:
            result = []
            for row in range(len(self.matrix)):
                curr_row = []
                for column in range(len(self.matrix[0])):
                    curr_row.append(self.matrix[row][column]+other.matrix[row][column])
                result.append(curr_row)
            return Matrix(result)

    def __sub__(self, other):
        if len(self.matrix) == 0 or len(other.matrix) == 0:
            raise ValueError("Input should be matrix.")
        elif len(self.matrix[0]) != len(other.matrix[0]):
            raise DimensionMissMatch("Matrix Dimension miss matched.")
        elif len(self.matrix) != len(other.matrix):
            raise DimensionMissMatch("Matrix Dimension miss matched.")
        else:
            result = []
            for row in range(len(self.matrix)):
                curr_row = []
                for column in range(len(self.matrix[0])):
                    curr_row.append(self.matrix[row][column]-other.matrix[row][column])
                result.append(curr_row)
            return Matrix(result)

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise MatrixMultiplicationError("Length of Column and Row did't match.")
        else:
            result = []

            for row in range(len(self.matrix)):
                curr_row = []
                for column in range(len(other.matrix[0])):
                    curr_el = 0
                    for el in range(len(self.matrix[row])):
                        curr_el += self.matrix[row][el]*other.matrix[el][column]
                    curr_row.append(curr_el)
                result.append(curr_row)

            return Matrix(result)


if __name__ == "__main__":
    A = Matrix([
        [1,2],
        [3,4]
        ])
    B = Matrix([[5,6],
                [7,8]])
    C = Matrix([[7,8],
                [9,10]])
    D = Matrix([[1,2,3],
                [4,5,6]])

    print(A-C)
    print(B*C)