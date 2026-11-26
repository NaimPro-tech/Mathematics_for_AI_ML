from exception.custom_exception import DimensionMissMatch,IrregularMatrix, MatrixMultiplicationError
from validation.validation import validation_check_normal, validation_check_multiplication
import copy
from src.linear_algebra import LinearAlgebra

class Matrix(LinearAlgebra):

    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)
        if len(self.matrix) == 0 or len(self.matrix[0]) == 0:
            raise ValueError("Invalid Matrix. Iniatialize the values.")
        #irregular matrix catch and stop implimention
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

    @property
    def shape(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, index):
        return self.matrix[index]

    def __add__(self, other):
        validation_check_normal(self, other)
        result = []
        for row in range(len(self.matrix)):
            curr_row = []
            for column in range(len(self.matrix[0])):
                curr_row.append(self.matrix[row][column]+other.matrix[row][column])
            result.append(curr_row)
        return Matrix(result)

    def __sub__(self, other):
        validation_check_normal(self, other)
        result = []
        for row in range(len(self.matrix)):
            curr_row = []
            for column in range(len(self.matrix[0])):
                curr_row.append(self.matrix[row][column]-other.matrix[row][column])
            result.append(curr_row)
        return Matrix(result)

    def __mul__(self, other):
        validation_check_multiplication(self, other)

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
        [1,2,8],
        [3,4,7]
        ])
    B = Matrix([[5,6],
                [7,8],
                [9,10]])
    C = Matrix([[7,8,10],
                [9,10,5]])
    data = [
        [100,200],
        [300,400]
    ]
    D = Matrix(data)
    data[0][0] = 900
    print(A-C)
    print("Multiplication:",A*B)
    print(D)
    print(C.shape)

