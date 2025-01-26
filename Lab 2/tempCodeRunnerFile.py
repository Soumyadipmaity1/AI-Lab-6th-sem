
# Example usage:
if __name__ == "__main__":
    A = np.array([[3, 1], [1, 2]])
    b = np.array([9, 8])
    print("Solution of linear equations:", solve_linear_equations(A, b))

    matrix_3x3 = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
    print("Determinant of matrix:", determinant_3x3(matrix_3x3))

    matrix_2x2 = np.array([[2, 1], [1, 2]])
    eigenvalues, eigenvectors = eigenvalues_eigenvectors(matrix_2x2)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:\n", eigenvectors)

    matrix_3x3_unsorted = np.array([[3, 2, 5], [1, 4, 6], [2, 3, 8]])
    print("Sorted by 2nd column:\n", sort_by_second_column(matrix_3x3_unsorted))

    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    print("Matrix multiplication:\n", matrix_multiply(matrix1, matrix2))

    array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    max_val, min_val = max_min_2d_array(array_2d)
    print("Max:", max_val, "Min:", min_val)

    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])
    add, sub, mul, div = element_wise_operations(array1, array2)
    print("Addition:", add)
    print("Subtraction:", sub)
    print("Multiplication:", mul)
    print("Division:", div)

    array = np.array([1, 5, 10, 15, 20])
    threshold = 10
    print("Thresholded array:", threshold_array(array, threshold))

    array_with_primes = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print("Prime numbers:", extract_primes(array_with_primes))

    array_for_cumprod = np.array([1, 5, 10, 2, 4, 8])
    print("Cumulative product limited:", cumulative_product_limited(array_for_cumprod))
