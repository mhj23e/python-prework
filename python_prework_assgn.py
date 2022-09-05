# Questoin 1: Prints out Hello USERNAME  
from tkinter import N


def hello_name(user_name):
    print("Hello" + " " + user_name, "\n")
hello_name("Mark")

#Question 2: Prints odd numbers from 1-100 and returns nothing 
def first_odds():
    for num in range(1, 100):
        if (num % 2 != 0):
            print(num)
first_odds()

#Question 3: Prints the max number of a given list
def max_num_in_list(a_list):
    list_num = len(a_list)
    print("\n", list_num, "\n")
b_list = [1, 2, 3, 5]
max_num_in_list(b_list)

#Question 4: Divisible by 4 but not 100 unless also by 400
def is_leap_year(a_year):
    if (a_year % 4 == 0 & a_year % 100 != 0 | a_year % 400 == 0 ):
        return True
    else: 
        return False
leap_year = is_leap_year(2000)
print(leap_year, "\n") 

#Question 5: Checks if list is consecutive numbes and returns Boolean
def is_consecutive(a_list):
    if (a_list == sorted(a_list)):
        return True 
    else:
        return False
n_list = [1, 2, 3, 4]        
results = is_consecutive(n_list)
print(results)


