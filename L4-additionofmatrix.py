"""Addition of matricies
   PAVAN SAI . V
   121910313028"""
# defining a function for a sparse matrix   
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

# addition of two sparse matrices
def add(a1,a2):
    out = [] 
    l1 = len(a1)
    l2 = len(a2)
    if l1==0 : out = a2
    if l2==0 : out = a1
    i = 0
    j = 0
    while l1>0 and l2>0:
        if a1[i][0]==a2[j][0] and a1[i][1]==a2[j][1]:
            out.append([a1[i][0],a1[i][1],a1[i][2]+a2[j][2]])
            i += 1
            j += 1
        else:
            m = min(a1[i],a2[j])
            out.append(m)
            if m==a1[i]:
                i += 1
            else:
                j += 1
        if i>=l1:
            for x in range(j,l2):
                out.append(a2[x])
            break
        if j>=l2:
            for x in range(i,l1):
                out.append(a1[x])
            break
    return out

# Function to print martix
def print_martix(a):
    if a==[]: print('EMPTY MATRIX')
    for i in a:
        print(*i)

# Function to take array input
def input_matrix(r):
    a = [] # Declaring the matrix
    i = 0
    while i<r:
        dup = list(map(int,input().split()))
        a.append(dup)
        i += 1
    return a


# Inputting arrays
row = int(input("Enter the number of rows : "))
col = int(input("Enter the number of columns : "))
print("Enter Martix 1")
a1 = input_matrix(row)
print("Enter Martix 2")
a2 = input_matrix(row)

# Printing Original Matrices
print("The Original Matrices are")
print("Matrix 1")
print_martix(a1)
print("Matrix 2")
print_martix(a2)
print()

# Printing Sparse Matrices
print("The Sparse Matrices are")
sm1 = sparse_matrix(a1)
sm2 = sparse_matrix(a2)
print("Sparse Matrix 1")
print_martix(sm1)
print("Sparse Matrix 2")
print_martix(sm2)
print()

# Printing the result
print("Addition of 2 Sparse Matrices")
result = add(sm1,sm2)
print_martix(result)