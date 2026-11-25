
def validation_check_normal(a:"Matrix", b:"Matrix"):
    if len(a) == 0 or len(b) == 0:
        raise ValueError("Input should be matrix.")
    elif len(a[0]) != len(b[0]):
        raise DimensionMissMatch("Matrix Dimension miss matched.")
    elif len(a) != len(b):
        raise DimensionMissMatch("Matrix Dimension miss matched.")


def validation_check_multiplication(a:"Matrix", b:"Matrix"):
    if len(a) == 0 or len(b) == 0:
        raise ValueError("Input should be matrix.")
    elif len(a[0]) != len(b):
        raise DimensionMissMatch("Matrix Dimension miss matched.")

def validation_check_vector(a:"Vector", b:"Vector"):
    if len(a) == 0 or len(b) == 0:
        raise ValueError("No operation can be done with 0 dimensional vector")
    elif len(a) != len(b):
        raise DimensionMissMatch("Vectors must have same length.")
