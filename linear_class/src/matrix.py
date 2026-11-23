from exception.custom_exception import DimensionMissMatch,IrregularMatrix, MatrixMultiplicationError
from validation.validation import validation_check_normal, validation_check_multiplication

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

    def __len__(self):
        count = 0
        for _ in self.matrix:
            count+=1
        return count

    def __getitem__(self, index):
        return self.matrix[index]

    def __add__(self, other):
        validation_check_normal(self.matrix, other)
        result = []
        for row in range(len(self.matrix)):
            curr_row = []
            for column in range(len(self.matrix[0])):
                curr_row.append(self.matrix[row][column]+other.matrix[row][column])
            result.append(curr_row)
        return Matrix(result)

    def __sub__(self, other):
        validation_check_normal(self.matrix, other)
        result = []
        for row in range(len(self.matrix)):
            curr_row = []
            for column in range(len(self.matrix[0])):
                curr_row.append(self.matrix[row][column]-other.matrix[row][column])
            result.append(curr_row)
        return Matrix(result)

    def __mul__(self, other):
        validation_check_multiplication(self.matrix, other)

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
    D = Matrix([
        [],
        []
    ])
    print(A-C)
    print(B*C)
