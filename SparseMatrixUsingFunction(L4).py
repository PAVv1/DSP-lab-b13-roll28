"""PAVAN SAI .V
   121910313028
   Matrix to SparseMatrix using functions"""

#function to print a matrix
def displaymatrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()

#matrix initialization
arr  = ([0,5,0,1],
       [1,0,6,0],
       [3,0,7,0],
       [0,1,0,2])

#print given matrix
print("Given Matrix:")
displaymatrix(arr)


#SparseMatrix
def sparseMatrix(matrix):

    sparsematrix = [] #declare empty list

    #looping
    #and checking for non-zero elements
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:

                temp=[] #temporary list

                temp.append(i) #adding row index
                temp.append(j) # adding column index
                temp.append(matrix[i][j]) #value of tht non-zero element

                #appending temp to sparsematrix
                sparsematrix.append(temp)

    #display sparsematrix
    print("\nSparseMatrix:")
    displaymatrix(sparsematrix)


#conversion
sparseMatrix(arr) #using function