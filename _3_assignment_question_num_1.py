# Assignment_number_3
# Question_number_1 =  Write a Python function to sum all the numbers in a list.



def sum():

    size  = int(input("enter the size : "))
    lst = []
    total = 0
    for i in range (size):
        element = int(input("enter the element : "))
        lst.append(element)
    for i in lst:
         total += i

    print ("List : " , lst)
    print ("Sum of all the number in list : " , total)
    
sum()

