# '''print the ascii values'''
# print(ord('A'))
# for i in range(32,128):
#     print(chr(i),end=" ")
# for i in range(65,65+26):
#     print(chr(i),end=" ")  
# for i in range(91,91+26):
#     print(chr(i),end=" ")
''' ascii values for 0-9 is 40 to 58
sum of the all ascii values'''
# s=0
#print(ord('0'))

# for i in range(chr(48),chr(58)):
#     s+=chr(i)
# print(s)    

# s=0
# for i in range(48,59):
#     c=chr(i)
#     #print(c)
#     r=int(c)
#     # sint(c)
#     print(r)
    

# '''wap to print all the capital letters in a given string'''
# str=input()
# #sum=0
# for i in str:
#     if(ord(i)>=65 and ord(i)<=90):
#         print(i) 
#         break      


'''Remove all the characters from the alzebric expression'''

# str=input()
# s=" "
# for i in str:
#     if(ord(i)==40 and ord(i)==41 and ord(i)==123 and ord(i)==125 and ord(i)==93 and ord(i)==91):
#         print(i)
'''method-2'''
'''chr means character values==int to chr
ord means ascii values to int'''
str=input()
s=" "
for i in str:
    if(ord(i)==40 or ord(i)==41 or ord(i)==123 or ord(i)==125 or ord(i)==93 or ord(i)==91):
        pass
    else:
        print(i,end="")
print        



'''remove all the brackets in string
{==123,}==125
(==41,40==)
[==91.93==]'''     
str=input()
c="(,),{,},[,]" 
a=" "
for i in str:
    if i not in c:
        a+=i
print(a)





