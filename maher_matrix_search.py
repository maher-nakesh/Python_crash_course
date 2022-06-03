def sorted_matrix_search(matrix,integer):
    i=0
    #size of matrix
    for x in matrix:
        i+=1


    for a in range (0,len(matrix)):
        for j in range(0,i-1):
            if matrix[a][j] == integer:
                return print((a+1,j+1))

    return print('none')






m=[     [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50],
        ]
sorted_matrix_search( m,29 )