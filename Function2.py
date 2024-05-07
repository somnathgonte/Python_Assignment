# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:15:24 2024

@author: Somnath Gonte
Topics : Function2,userdefined-function,map,filter,lambda,join,split

"""
#1-----------------------------------------------------------------------------
#1.Define a function overlapping () that takes two lists and returns True 
#if they have at least one member in common, False otherwise.

def overlapping(lst1,lst2):
    flag = False
    for i in lst1:
        if i in lst2:
            flag=True
    return flag
    
    
list1_str= input("Enter elements (comma separated) in list1 :")
list2_str = input("Enter elements (comma separated) in list 2:")

list1=eval("["+list1_str+"]")
list2=eval("["+list2_str+"]")

print("Output :",overlapping(list1, list2))  # calling function

#2-----------------------------------------------------------------------------
#Write a function find_longest_word() that takes a list of words and 
#returns the length of the longest one.

def find_longest_word_length(wordList):
    max=0
    for i in wordList :
        if max < len(i):
            max=len(i)
    return max

str_list = input("Enter words in list (comma separated) :")
wordList=eval("["+str_list+"]")
res=find_longest_word_length(wordList)
print("Longest length :",res)

#3-----------------------------------------------------------------------------
#Write a function filter_long_words() that takes a list of words and an 
#integer n and returns the list of words that are longer than n.
d
ef filter_long_words(wordList,n):
    li=list(filter(lambda x:len(x)>n,wordList))
    return li
wordList=eval(input("Enter words in list :"))
n=int(input("Enter number :"))
res=filter_long_words(wordList,n)
print(res)

#4-----------------------------------------------------------------------------
#Define a simple "spelling correction" function correct () that takes a 
#string and sees to it that:
#   1. two or more occurrences of the space character is compressed into one, and
#   2. inserts an extra space after a period if the period is directly followed by a letter.
#e.g. correct ("This is very funny and cool.Indeed!") should 
#return "This is very funny and cool. Indeed!"

def correct(string):
    l=string.split(".")
    string=" ".join(l)
    print(string)

string = "This is very funny and cool.Indeed!"
correct(string)


#---------------------------------End------------------------------------------















