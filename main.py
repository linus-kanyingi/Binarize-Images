import numpy as np

def matrix_arithmetic(A, B, operation):
    A = np.array(A)
    B = np.array(B)

    if operation in ['add', 'subtract', 'divide']:
        if A.shape != B.shape:
            return "Error: Matrices must have the same dimensions."

    if operation == 'multiply':
        if A.shape[1] != B.shape[0]:
            return "Error: Columns of A must equal rows of B."

    if operation == 'add':
        return A + B
    elif operation == 'subtract':
        return A - B
    elif operation == 'multiply':
        return np.matmul(A, B)
    elif operation == 'divide':
        return A / B
    else:
        return "Invalid operation"


# user input
A = eval(input("Enter matrix A (example [[1,2],[3,4]]): "))
B = eval(input("Enter matrix B (example [[5,6],[7,8]]): "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

result = matrix_arithmetic(A, B, operation)

print("Result:")
print(result)