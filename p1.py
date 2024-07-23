''''substring questions
strings are sequence of chars
strings are mutable
cant be modified
indexing and "for i in str"
advantages:personal details
different string  methods:len,cancatenate="+",is_digit,is_alpha,is_prime,is_alphabumeric==isalnum,title==combination,
trip,islower(),isupper(),swap()
ASCII  VALUES
65-91===A-Z=====
97-122====a-z
digits-====48-57====0-9

'''
# n=int(input())
# c=0
# for i in range(2,int(n**(0.5))):
#     if n%i==0:
#         c+=1
# if(c==0):
#     print("prime")  
# else:
#     print("not prime")          

str=input()
l=len(str)
print(l)
# #print(isLowerCase(str))
# #print(str.LowerCase())
# print(isAlpha(str))
print(str.lower(),"29")
print(str.upper(),"30")
print(str.title(),"31")
print(str.swapcase(),"32")
print(str.capitalize(),"33")# in midddle of a string if any capital letters it will remove
print(str.strip(),"36")# start and end spaces are removed
print(str.replace('a','s'),"37")
print(str.split(),"38")#default it will the 2 different strings
print(str.split('a'),"39")# it will split at the particular character
print(str.swapcase(),"40")


