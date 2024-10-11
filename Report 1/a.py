def find_pivot_column(arr, horSize, verSize, accuracy):
    mi = 1000000
    pivotColumn = -1
    for i in range(0, horSize):
        if arr[verSize - 1][i] < -accuracy and arr[verSize - 1][i] < mi:
            mi = arr[verSize - 1][i]
            pivotColumn = i
    return pivotColumn


def find_variable_values(arr, horSize, verSize, accuracy):
    variableValues = [0] * (horSize - 1)
    for i in range(horSize - 1):
        countOnes = 0
        rowIndex = -1
        for j in range(verSize - 1):
            if abs(arr[j][i] - 1) < accuracy:
                countOnes += 1
                rowIndex = j
            elif abs(arr[j][i]) > accuracy:
                countOnes = 0
                break

        if countOnes == 1:
            variableValues[i] = arr[rowIndex][horSize - 1]
    return variableValues


def find_pivot_line(arr, horSize, verSize, pivot_col, accuracy):
    mi = 1000000
    pivot_line = -1
    for i in range(0, verSize - 1):
        if arr[i][pivot_col] > accuracy:
            ratio = arr[i][horSize - 1] / arr[i][pivot_col]
            if 0 < ratio < mi:
                mi = ratio
                pivot_line = i
    return pivot_line


def simplex_method(arr, horSize, verSize, accuracy):
    while True:
        pivotCol = find_pivot_column(arr, horSize, verSize, accuracy)
        if pivotCol == -1:
            break

        pivotLine = find_pivot_line(arr, horSize, verSize, pivotCol, accuracy)
        if pivotLine == -1:
            return None, None

        pivot_elem = arr[pivotLine][pivotCol]
        for i in range(horSize):
            arr[pivotLine][i] /= pivot_elem
        for i in range(verSize):
            if i != pivotLine:
                k = arr[i][pivotCol]
                for j in range(horSize):
                    arr[i][j] -= k * arr[pivotLine][j]

    maxValue = arr[verSize - 1][horSize - 1]
    variableValues = find_variable_values(arr, horSize, verSize, accuracy)
    return maxValue, variableValues


if __name__ == "__main__":
    print('Enter the vector of coefficients of the objective function (C)')
    coefficients = list(map(int, input().split()))
    print('Enter the vector of right-hand sides (b)')
    rightHandNumbers = list(map(int, input().split()))
    print('Enter the matrix of constraint coefficients (A)')
    matrix = []
    for i in range(len(rightHandNumbers)):
        coefficientsOfConstraints = list(map(int, input().split()))
        matrix.append(coefficientsOfConstraints)

    subMatrix = []
    for i in range(len(rightHandNumbers)):
        subArr = [0] * len(rightHandNumbers)
        subArr[i] = 1
        subMatrix.append(subArr)

    arr = []
    for i in range(len(rightHandNumbers)):
        subArr = []
        subArr += matrix[i]
        subArr += subMatrix[i]
        subArr += [rightHandNumbers[i]]
        arr.append(subArr)

    for i in range(len(coefficients)):
        coefficients[i] = -1 * coefficients[i]

    function = []
    function += coefficients + [0] * len(rightHandNumbers) + [0]
    arr.append(function)

    horSize = len(arr[0])
    verSize = len(arr)

    print("Enter the approximation accuracy (e.g. 1e-6)")
    accuracy = float(input())

    max_value, variable_values = simplex_method(arr, horSize, verSize, accuracy)

    if max_value is None:
        print("The method is not applicable!")
    else:
        print("Maximum value:", max_value)

        print("Variable values:")
        for x in range(len(coefficients)):
            print(f'x{x + 1}: {variable_values[x]}')
