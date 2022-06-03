def sorted_matrix_search(matrix,integer):
    row=0
    siz_of_matrix=0
    col=0

    for x in matrix:
        siz_of_matrix+=1

    row=siz_of_matrix-1

    while (col<siz_of_matrix and row >=0):
        if matrix[row][col] == integer:
            return print((row+1,col+1))

        if matrix[row][col] > integer :
            row-=1

        if matrix[row][col] <integer :
            col+=1

    return print('not found')








m=[     [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50],
        ]
sorted_matrix_search( m,29 )

#________________________________________________________
def partition(ratings):
    i=0
    min=ratings[0]
    first_list=ratings[0]
    for i in range (0,len(ratings)):

        seconde_list=[x for b,x in enumerate(ratings) if b!=i]
        if first_list-seconde_list<min:
            min=first_list-seconde_list
            first_list.apper(ratings+i)
        if first_list-seconde_list> min:
            continue

     return (first_list,seconde_list)