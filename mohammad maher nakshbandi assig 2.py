def palandrom (word):
    sub1=list(word)
    sub2=list(word)
    count0=2
    lenght1=len(sub1)
    while len(sub1):
    for i in range(0,lenght1,count0):
        count1=1
        if sub1[i]==sub2[i+count1]and sub1[i+count1]==sub2[i]:
            new=[sub[i]+sub2[i+1]]
            count1+=1
    count0+=1
    return max(new)



#-------------------------------------------

def cuberoot(x)
    cube_num=x*x*x
    return cube_num




