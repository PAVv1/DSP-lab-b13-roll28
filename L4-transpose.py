"""Program to transpose a sparse matrix 
   PAVAN SAI . V
   121910313028"""
#Function to represent the Sparse Matrix
def sparse_matrix(a):
    sm = []
    row = len(a) # Number of Rows
    col = len(a[0]) # Number of columns
    # Finding the non zero elements
    for i in range(row):
        for j in range(col):
            if a[i][j]!=0:
                sm.append([i,j,a[i][j]])
    return sm
# Function to transpose sparse matrix
def trans(a):
    out = []
    for i in a:
        out.append([i[1],i[0],i[2]])
    out.sort()
    return out
# Function to print martix
def print_matrix(a):
    if a==[]: print("Empty Matrix")
    for i in a:
        print(*i)
a = [] # Declaring the matrix
# Taking the matrix input
row = int(input("Enter the number of rows : "))
col = int(input("Enter the number of columns : "))
for i in range(row):
    dup = list(map(int,input().split()))
    a.append(dup)

print("The Original Matrix")
print_matrix(a)

print()
# Printing the sparse matrix
sparse = sparse_matrix(a)
print("The Sparse Matrix")
print_matrix(sparse)

# Printing the transpose of a sparse matrix
transpose = trans(sparse)
print("The transpose of sparse matrix")
print_matrix(transpose)