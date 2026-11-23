
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