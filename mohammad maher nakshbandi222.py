def find_farthest_points(points):
     xs = [lis[0] for lis in points ]
     ys = [lis[1] for lis in points ]
     max=0
     point=''
     for i in range (0,len(xs),2):
         euclidean=(((xs[i+1]-xs[i])**2)+(ys[i+1]-ys[i]**2))**1/2
         if euclidean>max:
             max=euclidean
             point='the distance between ({},{}) and ({},{}) is :'.format(xs[i],ys[i],xs[i+1],ys[i+1])+max
     return point

find_farthest_points([(222, 2333), (122, 23)])

#--------------------------------------------------
def is_permutation(str1, str2):
    if len(str1)!=len(str2):
        return False
    a=sorted(str1)
    b=sorted(str2)
    if a==b:
        return True
    else:
        return False



#print (is_permutation(['a','b','c'],['c','b','a']))

def get_permutation_list(input_str, output_str):
    for i in range (0,len(input_str)):
        for j in range (i,len(output_str)):
            if input_str[i]==output_str[j]:
                temp=input_str[j]
                input_str[i]=input_str[j]
                input_str[j]=temp

    return input_str

print(get_permutation_list(['1','2','3'],['3','2','1']))
