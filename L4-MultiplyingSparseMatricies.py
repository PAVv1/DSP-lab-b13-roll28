"""Program to Multiply Sparse Matrices
  PAVAN SAI . V
   121910313028"""
#Function for displaying a Sparse matrix
def sparse_matrix(a):
    sm = []
    row = len(a)
    # Number of Rows
     # Number of columns
    col = len(a[0])
    # Finding the non zero elements
    for i in range(row):
        for j in range(col):
            if a[i][j]!=0:
                sm.append([i,j,a[i][j]])
    return sm

#multiplication of two sparse matrices
def mul(a1,a2):
    row1 = len(a1)
    row2 = len(a2)
    col2 = len(a2[0])
    out= [[0 for _ in range(col2)] for __ in range(row1)]

    for i in range(row1):
        for j in range(col2):
            for k in range(row2):
                out[i][j] += a1[i][k]*a2[k][j]
    X = sparse_matrix(out)
    return X

# printing of martix
def display(a):
    if a==[]: print('EMPTY MATRIX')
    for i in a:
        print(*i)

# Function to take array input
def input_matrix(row):
    a = [] # Declaring the matrix
    i = 0
    while i<row:
        dup = list(map(int,input().split()))
        a.append(dup)
        i += 1
    return a


# Inputting arrays
row1 = int(input("Enter the number of rows in first matrix : "))
col1 = int(input("Enter the number of columns in first matrix : "))
row2 = int(input("Enter the number of rows in second matrix : "))
col2 = int(input("Enter the number of columns in second matrix : "))
if col1!=row2:
    print('You cannot multiply these matrices')
    exit()
print("Enter Martix 1")
a1 = input_matrix(row1)
print("Enter Martix 2")
a2 = input_matrix(row2)

# Printing Original Matrices
print("The Original Matrices are")
print("Matrix 1")
display(a1)
print("Matrix 2")
display(a2)
print()

# Printing Sparse Matrices
print("The Sparse Matrices are")
sm1 = sparse_matrix(a1)
sm2 = sparse_matrix(a2)
print("Sparse Matrix 1")
display(sm1)
print("Sparse Matrix 2")
display(sm2)
print()

# Printing the result
print("Multiplication of 2 Sparse Matrices")
result = mul(a1,a2)
display(result)
print_martix(transpose)