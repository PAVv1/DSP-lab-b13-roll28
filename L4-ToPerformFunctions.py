"""To perform functions on sparse matrix
   PAVAN SAI . V
   121910313028"""
# Function to represent the Sparse Matrix
def sparse_matrix(a):
    sm = []
    # Number of Rows
    row = len(a)
    # Number of columns
    col = len(a[0]) 
    # Finding the non zero elements
    for i in range(row):
        for j in range(col):
            if a[i][j]!=0:
                sm.append([i,j,a[i][j]])
    return sm

# adding two sparse matrices
def add(a1,a2):
    out = [] 
    l1 = len(a1)
    l2 = len(a2)
    if l1==0 : res = a2
    if l2==0 : res = a1
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
                res.append(arr2[x])
            break
        if j>=l2:
            for x in range(i,l1):
                out.append(a1[x])
            break
    return out

#multiplying of two sparse matrices
def mul(a1,a2):
    r1 = len(a1)
    r2 = len(a2)
    c2 = len(a2[0])
    res = [[0 for _ in range(c2)] for __ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                out[i][j] =out[i][j] + a1[i][k]*a2[k][j]
    ans = sparse_matrix(out)
    return ans

#transpose of sparse matrix
def trans(a):
    out = []
    for i in a:
        out.append([i[1],i[0],i[2]])
    out.sort()
    return out

# Function to print martix
def print_martix(a):
    if a==[]: print("EMPTY MATRIX")
    for i in a:
        print(*i)

# Function to take array input
def input_matrix(r):
    a= []
    # Declaring the matrix
    i = 0
    while i<r:
        dup = list(map(int,input().split()))
        a.append(dup)
        i += 1
    return a


# Inputting arrays
r = int(input("Enter the size of the square matrix : "))
print("Enter Martix 1")
arr1 = input_matrix(r)
print("Enter Martix 2")
arr2 = input_matrix(r)
print()

sm1 = sparse_matrix(arr1)
sm2 = sparse_matrix(arr2)

# User choice
print("Choose an operation from below")
print("1. Display the Sparse Matrices \n2. Addition of the Matrices \n3. Multiplication of the Matrices \n4. Transpose of the Matrices")
n = int(input("Enter an option : "))

if n==1:
    # Printing Sparse Matrices
    print("The Sparse Matrices are")
    print("Sparse Matrix 1")
    print_martix(sm1)
    print("Sparse Matrix 2")
    print_martix(sm2)
    print()
elif n==2:
    # Printing the Sum of Sparse Matrices
    print("Addition of 2 Sparse Matrices")
    result = add(sm1,sm2)
    print_martix(result)
elif n==3:
    # Printing the Product of Sparse Matrices
    print("Multiplication of 2 Sparse Matrices")
    result = mul(sm1,sm2)
    print_martix(result)
elif n==4:
    # Printing the Transpose of Sparse Matrices
    print("Transpose of the Matrices")
    print("Transpose of Sparse Matrix 1")
    print_martix(trans(sm1))
    print("Transpose of Sparse Matrix 2")
    print_martix(trans(sm2))