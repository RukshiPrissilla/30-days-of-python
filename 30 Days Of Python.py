#day 1 intro variable operator 

#DAY  4 STRING 

letter="p"
multiline_string=''' I am very happy about nothing just fun chill do what you want'''
#we can do multiline string using ''' or """ 

#string concatenation (merging or connecting string)

first_name="Rukshi"
second_name="Prissilla"
space=" "
ful_name=first_name + space + second_name 
print(ful_name)  #Rukshi Prissilla

#escape sequence

'''
\n new line
\t tab space
\\ back slash
\' single quote
\" double quote
'''
print("I hope everyone.\nAre you?") # it comes like 2 lines
print("Days\tTopics\tExercise")#Days    Topics  Exercise   (tab means 8 spaces)
print("day 1\t5\t5")           #day 1   5       5        
print("1\t2\t3")               #1       2       3    
print("My name is \"Rukshi\"") #My name is "Rukshi"  

# f string

a=4
b=3
print(f"{a} + {b} = {a+b}")  #4 + 3 = 7
print(f"{a} / {b} = {a/b:.2f}") #4 / 3 = 1.33  :.2f 2decimal

#DAY 9 CONDITIONALS

a=3
if a>0:
    print("a is a positive number")  
elif a<0:
    print("a is a negative number")
else:
    print("a is 0")

#short hand
b=4
print("b is negative") if b<0 else print("b is positive")  # b is positive 

#nested conditions
a=0
if a>0:
    if a % 2 == 0:
        print("a is positive and even")
    else:
        print("a is positive number")
elif a == 0:
    print("a is Rukshi")  
else:
    print("a is negative")
#we can also use (and or) here
     
#DAY 12 MODULE

# module is a python file that contains code such as functions and variables that u can reuse in another python file
# three ways to import code
#1)import the entire module
import math
#2)import only the function u need
from math import sqrt
#3)give a function a shorter name
from math import sqrt as square_root

#important python modules
#1) math
import math
print(math.sqrt(36))  #6
print(math.pi) #3.14...
print(math.ceil(4.2)) #5
print(math.floor(4.8))  #4
print(math.pow(2,2))  #4

#2) random

#3)statistics
from statistics import mean,median,mode #average,middle value after sorting,most frequently occuring value

#4)string
import string
print(string.digits) #0123456789
print(string.ascii_letters) #give all small and capital letters

#5)OS work with file and folder
#6)sys
import sys
print(sys.version)  #this display the python you use
  
#DAY 15 PYTHON TYPE ERrOF

#syntax error - its like missing paranthesis
#name error - we forgot to define a variable name and ask python to print it out
#index error - it occurs when we type a list and ask python to print somethin in a list out of range.Like the list include 0 to 5 we ask to print 6th one
#module not found error - we tell python something wrong that python already define in modules.Like(import math) python knows but not (import maths)
#attribute error - type PI instead of pi like give something not in math module
#key error - we define some thing like (country) and ask python to print (county)
#type error- 4 + "3" we cant add string and integer
#import error - there is no word (power) in maths module it calls like (pow) from math import pow
#value error - int("12a") its wrong because of letter a
#zero division error - we cant devide by 0 like 1/0




              



