import numpy as np

def get_matrix_input(name):
    rows = int(input(f"\nEnter the number of rows for Matrix {name}: "))
    cols = int(input(f"Enter the number of columns for Matrix {name}: "))
    print(f"Enter the elements of Matrix {name} row-wise (separated by space):")

    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").strip().split()))
        if len(row) != cols:
            print(f"Error: Expected {cols} columns, got {len(row)}.")
            return None
        matrix.append(row)

    return np.array(matrix)

def display_menu():
    print("\nSelect Operation:")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Transpose of a Matrix")
    print("5. Determinant of a Matrix")
    print("6. Exit")

def main():
    print("========== Matrix Operations Tool ==========")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")

        if choice in ['1', '2', '3']:
            A = get_matrix_input('A')
            B = get_matrix_input('B')
            if A is None or B is None:
                continue

            try:
                if choice == '1':
                    result = A + B
                    print("\nResult of Addition:\n", result)
                elif choice == '2':
                    result = A - B
                    print("\nResult of Subtraction:\n", result)
                elif choice == '3':
                    result = A @ B
                    print("\nResult of Multiplication:\n", result)
            except ValueError as e:
                print("\nError:", e)

        elif choice == '4':
            A = get_matrix_input('A')
            if A is not None:
                print("\nTranspose of Matrix A:\n", A.T)

        elif choice == '5':
            A = get_matrix_input('A')
            if A is not None:
                if A.shape[0] == A.shape[1]:
                    det = np.linalg.det(A)
                    print("\nDeterminant of Matrix A:", round(det, 2))
                else:
                    print("\nError: Determinant can only be calculated for square matrices.")
        
        elif choice == '6':
            print("\nThank you for using the Matrix Operations Tool.")
            break

        else:
            print("\nInvalid choice. Please select a valid option (1-6).")

if __name__ == "__main__":
    main()
