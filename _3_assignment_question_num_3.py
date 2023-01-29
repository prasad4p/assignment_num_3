# Assignment_number_3
# Question_number_3 = Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.


string = input("enter the string : ")

def count_upper_lower(string):
    
    lowercase = 0
    uppercase = 0
    for letter in string:
        if letter.isupper():
            uppercase += 1
        elif letter.islower():
            lowercase += 1

    print("Number of Upper case letters : ", uppercase)
    print("Number of Lower case letters : ", lowercase)
    
count_upper_lower(string)



