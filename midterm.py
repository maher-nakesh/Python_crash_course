#problem 1 :
def list_to_dictionary(l):
    dic=dict()
    for i in range(0,len(l)):
        if l[i] not in dic:
            dic[l[i]]=[i]
        else:
            dic[l[i]]+=[i]
    return print(dic)
list_to_dictionary([2,1,2,1,5,6,3,2,4,5,5,5,5,7,8,9,0])
#______________________________________________
#problem2:
def net_worth_today(l):
    first_amount = l[0]
    nvalue = l[0] #new rate
    last_worth = 1000 #1000$
    for i in range(0,len(l)):
        if l[i]>nvalue+(nvalue*0.05):
            nvalue=l[i]*last_worth//first_amount
    return nvalue
L = [1500, 1550, 3000, ]
print(net_worth_today(L))
#_________________________________________________________
#problem 3 :
def sort_V_shape (l):
    list_received=merge_sort(l)
    mid=(len(list_received)//2)+1
    new=list_received[:mid]
    new.reverse()
    end=new+list_received[mid:]
    return end

def merge_sort(list_in):
    if len(list_in) <= 1:
        return list_in
    mid = len(list_in) // 2
    left_list = merge_sort(list_in[:mid])
    right_list = merge_sort(list_in[mid:])
    return merge(left_list, right_list)

def merge(left_list, right_list):
        list_out = []
        left_list_index =0
        right_list_index = 0
        left_list_length= len(left_list)
        right_list_length = len(right_list)

        for _ in range(left_list_length + right_list_length):
            if left_list_index < left_list_length and right_list_index < right_list_length:

                if left_list[left_list_index] <= right_list[right_list_index]:
                    list_out.append(left_list[left_list_index])
                    left_list_index += 1
                else:
                    list_out.append(right_list[right_list_index])
                    right_list_index += 1

            elif left_list_index == left_list_length:
                list_out.append(right_list[right_list_index])
                right_list_index += 1

            elif right_list_index == right_list_length:
                list_out.append(left_list[left_list_index])
                left_list_index += 1

        return list_out



print( sort_V_shape( [4, 5, 10, 3, 2, 8, 1]))
#_____________________________________________________________________
#problem4:
def fib(n):
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2
#link:https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series

def fibonacci_reverse(n):
    for i in range(0,n+1):
        if fib(i)== n :
            return print (i)
    return print (-1)

fibonacci_reverse(55)
#______________________________________________________________

#problem 5:
def generate(n, k):
    b=[]
    for i in range(0,n) :
     b.append(i)
     b[i] = str(b[i])
    lenght = len(b)
    m= print_set(b, "", lenght, n)
def print_set(b, mm, lenght, n):
    if (n == 0) :
        print(mm)
        return
    for i in range(lenght):
        new_list = mm + b[i]
        
        print_set(b, new_list, lenght, n - 1)

generate(4,3)
#____________________________________________________________________
#problem6:
def most_occuring_prime(n):

    def check_prime(num):
        if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   print(num, "is not a prime number")
                   break
                   return False
               else:
                return True
        else:
            return None

    def count(l, n):
        first = 0
        last = len(l)-1
        count=0
        while   first <= last :
            mid = (first+last)//2
            if l[mid] == n:
                 count+=1
            else:
                if n<l[mid]:
                    last = mid -1
                else:
                    first = mid +1
        return count
    max=0
    max=()
    for i in range(0,len(n)):
        if check_prime(n[i]):
            b=count(n,n[i])
            if b > max:
                max=b
                max=(n[i],b)
                
                
    return max
#_____________________________________________________________________
#problem7:
def solve_puzzle(pieces):
    all_compination=[]

    def div (left,right,level,all_compination):
        if level >= len(pieces):
            all_compination.append((left,right))
            return

        current=pieces[level]
        div(left + [current], right , level + 1 , all_compination)
        div(left ,right + [current] , level +1 , all_compination)

    div([],[],0,all_compination)
    
    for i in range (0,len(all_compination)):
     left, right = all_compination[i]
	 
