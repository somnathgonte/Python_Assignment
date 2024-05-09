# -*- coding: utf-8 -*-
"""
Created on Thu May  9 14:10:02 2024

@author: Somnath Gonte
Topic : Exception handeling
"""

#Q1
'''
Write a program to accept two numbers from user and use divide function to divide two numbers. 
Implement exception handaling to check it divisor is Zero
'''
def divide(iNo1,iNo2):
    '''
    This function divide two number 
    '''
    division = iNo1/iNo2
    return division

try:
    
    iNo1 = int(input("Enter first number :"))
    iNo2 = int(input("Enter second :"))
    print(divide(iNo1,iNo2))

except ZeroDivisionError:
    print("division by zero is not possible")
    
    
#Q2
'''
ACCEPT AGE,HEIGHT,WEIGHT,NAME AND SURNAMEE FOR USER.
AGE SHOULD BE AN INTEGER ,HEIGHT,WEIGHT ARE FLOAT,NAME AND SURNAME ARE STRING
IF THE USER ENTERS INPUT OF THE INCORRECT TYPE, KEEP
PROMPTING THE USER FOR THE SAME VALUE UNTIL IT ENTERD CORRECTLY.
GIVE THE USER SENSIBLE FEEDBACK
'''

def get_int_input(prompt):
    while (1):
        try :
            value = int(input(prompt))
            return value
        except ValueError :
            print("Please enter an integer value")
            
def get_float_value(prompt):
    while(1):
        try :
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter valid float value")
    
def get_string_input(prompt):
    while True:
        try:
            value=input(prompt)
            if value.isalpha():
                return value
        except ValueError:
            print("Enter string value")
            
age = get_int_input("Enter age :")
height = get_float_value("Enter height :")
weight = get_float_value("Enter weight :")
name=get_string_input("Enter name :")
surname=get_string_input("Enter surname :")

print("---Person Information---")
print("Age :",age)
print("Height :",height)
print("Weight :",weight)
print("Name :",name)
print("Surname :",surname)
print("------------------------")

#Q3
'''
Add a try-except statement to the body of this function
which handles a possible IndexError,which could occur
if the index provided exceeds the length
of the list.Print an error message if this happens :

 def print_list_element(thelist,index):
print(thelist[index])
'''
def print_list_element(thelist,index):
    try :
        print(thelist[index])
    except IndexError :
        print("Error :List index out of range")
    
thelist=[10,20,30,40,50]
index = int(input("Enter index of list :"))
print_list_element(thelist, index)


#Q4
'''
The function adds an element to alist inside a dict of lists 
rewrite it to use a try-except statement which handles
a possible KeyError if the list with the name provided doesn't
exist in the dictionary. Include else and finally clauses in your

'''
def add_to_list_in_dict(thedict, listname, element):
    try:
        l = thedict[listname]
        print("%s already has %d elements." % (listname, len(l)))
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    finally:
        thedict[listname].append(element)

# Example usage:
my_dict = {}

add_to_list_in_dict(my_dict, "numbers", 1)
add_to_list_in_dict(my_dict, "numbers", 2)
add_to_list_in_dict(my_dict, "letters", "a")
add_to_list_in_dict(my_dict, "letters", "b")
add_to_list_in_dict(my_dict, "symbols", "@")
add_to_list_in_dict(my_dict, "symbols", "#")

print(my_dict)


#5
'''
Write a program to accept age from user and check if user age is valid for voting or not.
raise invalidageException if user enter < 18 value.also handle all posible exception

'''
class InvalidageException(Exception):
    pass

try :
    age=int(input("Enter age: "))
    if age >= 18:
        print("You are valid for vote.!")
    else:
        raise InvalidageException("Age should be equal to or greter than 18")
except InvalidageException as e :
    print(e)

#6
'''
Write a program to accept, display list of numbers.
Use SearchByPosition function to search element from list
(by position.acccept pos and element from user).check following things.
1.Check if position is greater than list size.(raise exception)
2.if element is not available.(raise exception)
3.You have to catch all the raise exception also
'''



