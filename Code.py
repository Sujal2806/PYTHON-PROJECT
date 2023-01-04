#Function that will return last number of fibonacci series upto the argument passed[x]. 
def fib(x): 
 a=0
 b=1
 c=1 
 while a<x: 
 a=b+c 
 b=c 
 c=a 
 return a 
#Taking single or multiple numbers as input in a list[n]. 
n=input("Enter a number or numbers: ").split(",") 
l=[] 
#For loop to convert each element of list into integer and add to another list[l]. 
for i in n: 
 l.append(int(i)) 
#For loop to check every number of list[l] ,whether a number is part of fibonacci series and print valid if yes and invalid if no. 
for i in l: 
#As 0 & 1 are part of fibonacci series, we will check if i is equal to 0 or 1. If yes, then we will print valid. 
 if (i==0 or i==1): 
 print(i,'is valid in fibonacci series') 
#If number returned by function fib() after passing argument that we want to check[i] is same as argument, then we will print valid. 
 elif (fib(i)==i): 
 print(i,"is valid in fibonacci series") 
#If number returned by function fib() after passing argument that we want to check[i] is not same as argument, then we will print invalid. 
 else: 
 print(i,"is invalid in fibonacci series")
