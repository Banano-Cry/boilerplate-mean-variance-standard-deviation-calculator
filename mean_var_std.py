import numpy as np

def calculate(list):
    # Check if list has less than 9 numbers
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    # Dictionary of all the calculated values
    calculations = dict()

    # Convert to Numpy Array and shaping to 3x3
    array = np.array(list)
    matrix_3x3 = array.reshape((3,3))

    # Calculate the mean
    calculations['mean'] = [
        matrix_3x3.mean(axis=0).tolist(),
        matrix_3x3.mean(axis=1).tolist(),
        array.mean()
        ]

    # Calculate the variance
    calculations['variance'] = [
        matrix_3x3.var(axis=0).tolist(),
        matrix_3x3.var(axis=1).tolist(),
        array.var()
        ]

    # Calculate the standard deviatoin
    calculations['standard deviation'] = [
        matrix_3x3.std(axis=0).tolist(),
        matrix_3x3.std(axis=1).tolist(),
        array.std()
        ]

    # Calculate the max
    calculations['max'] = [
        matrix_3x3.max(axis=0).tolist(),
        matrix_3x3.max(axis=1).tolist(),
        array.max()
        ]

    # Calculate the min
    calculations['min'] = [
        matrix_3x3.min(axis=0).tolist(),
        matrix_3x3.min(axis=1).tolist(),
        array.min()
        ]

    # Calculate the sum
    calculations['sum'] = [
        matrix_3x3.sum(axis=0).tolist(),
        matrix_3x3.sum(axis=1).tolist(),
        array.sum()
        ]

    print(calculations)

    return calculations
