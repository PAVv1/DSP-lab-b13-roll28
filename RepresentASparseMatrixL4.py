"""PAVAN SAI . V
   121910313028
   represent a sparse matrix"""

#matrix initialization
matrix = ([0,0,0,1],
	      [1,0,0,2],
	      [3,0,0,0],
	      [0,4,0,2])
#printing initialized matrix
print("Given Matrix: ")
for i in matrix:
	for j in i:
		print(j, end=" ")
	print()

#SparseMatrix
sparsematrix = [] #declare empty list
#looping and checking for non-zero elements
for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		if matrix[i][j] != 0:

			temp=[] 

			temp.append(i) 
			temp.append(j) 
			temp.append(matrix[i][j]) 

			sparsematrix.append(temp) 

#printing SparseMatrix
print("\nSparseMatrix: ")
for i in sparsematrix:
	for j in i:
		print(j, end =" ")
	print()