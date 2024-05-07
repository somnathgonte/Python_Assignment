# -*- coding: utf-8 -*-
"""
Created on Sat May  4 11:10:18 2024

Assignment No : 4
Assignment Topic : String

@author: Somnath Gonte
"""
print(dir(str))
#.1---------------------------------------------------------------
string = input("Enter string :")
print(string.replace('a', '$'))

# 2---------------------------------------------------------------
s = input("Enter string :")
index=int(input("enter index"))
print(s[:index]+s[index+1:])

# 3---------------------------------------------------------------
s = input("Enter string :")
vowels=0
consonants=0
vowels_str='aeiouAEIOU'
for i in s :
    if i.isalpha():
        if i in vowels_str:
            vowels = vowels+1
        else :
            consonants=consonants+1
print("Vowels is :",vowels,"consonants is :",consonants)

# 4---------------------------------------------------------------
s = input("Enter string :")
print(s.replace(' ','-'))

# 5---------------------------------------------------------------
s = input("Enter string :")
count=0
for i in s :
    count=count+1
print(count)

# 6---------------------------------------------------------------
s = input("Enter string: ")
new_string = ""
for i in range(len(s)):
    if i % 2 == 0:
        new_string += s[i]
print("Result:", new_string)

#7---------------------------------------------------------------
s = input("Enter string: ")
upper_count=0
lower_count=0
for i in s:
    if i.isupper() :
        upper_count=upper_count+1
    elif i.islower() :
        lower_count=lower_count+1
print("Upper :",upper_count,"Lower :",lower_count)

#8---------------------------------------------------------------
s=input("Enter string :")
if s[::-1]==s : print("Palindrome")
else : print("Not palindrome")

#9---------------------------------------------------------------
s=input("Enter string :")
print(s[0:2]+s[-2:len(s)])

#10 -----------------------------------------------------------------
s=input("Enter string :")
c=input("Enter character :")

if s.startswith(c) :
    print("True")
else :
    print("False")
    
#11----------------------------------------------------------------
s= input("Enter string:")
vowel='aeiouAEIOU'
count = 0
for i in s :
    if i.isalpha():
        if i not in vowel :
            count = count+1
print(count)

#12 ----------------------------------------------------------------
name = input("Enter name :")
age=int(input("Enter age :"))
salary=float(input('Enter salary :'))
#Hello,name you are age years old and getting salary salary
#default Format
print("-----Default Format-----")
print("Hello,{} you are {} years old and getting salary {}".format(name,age,salary))
#positional function
print("-----positional format-----")
print("Hello,{0} you are {1} years old and getting salary {2}".format(name,age,salary))
#keyword function
print("-----Keyword format-----")
print("Hello,{n} you are {a} years old and getting salary {s}".format(n=name,s=salary,a=age))
# f function
print("-----f function-----")
print(f"Hello,{name} you are {age} years old and getting salary {salary}")
# % format 
print("-----% format-----")
print("Hello,%s you are %d years old and getting salary %.2f" %(name,age,salary))

#13 -------------------------------------------------------------------
s="AlwaysThinkPositive"
print(s[5:6])
print(s[9:10])
print(s[5:8])
print(s[8:5:-1])
print(s[:])
print(s[2:])
print(s[0:8])
print(s[-19:-5])
print(s[::-1])
print(s[14:17])
print(s[-5:-2])
print(s[0:17])
print(s[13:])
print(s[::2])
st=s[::2]
print(st[::-1])
#14 -------------------------------------------------------------------
s="The Quick brown fox jumps over the lazy dOG"
print(s)
print('-'*40)
print(s.lower())
print('-'*40)
print(s.upper())
print('-'*40)
print(s.title())
a=s.title()
print('-'*40)
print(a.swapcase())
print('-'*40)
print(s.capitalize())

#15 --------------------------------------------------------------------
s=input("Enter string :")
count=0
for i in s:
    if i.isalpha() :
        count=count+1
print("Toatl Alphabet :",count)


#16 --------------------------------------------------------------------
s=input("Enter string :")
sum=0
for i in s :
    if i.isdigit() :
        sum=sum+int(i)
print("Sum of digit is :",sum)

#17 --------------------------------------------------------------------
s = input("Enter string :")
word=s.split()
for i in word :
    if 'a' in i :
        print(i)

#18 --------------------------------------------------------------------
s = input("ENter String :")
for i in range(len(s)) :
    for j in range(i+1) :
        print(s[j],end='\t')
    print()
    
#19 --------------------------------------------------------------------
s=input("Enter string :")
words = s.split()

for i in words :
    print(i[0:2],end=" ")
    
#-------------------------------End--------------------------------------


