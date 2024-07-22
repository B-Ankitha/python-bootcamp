''''password verifier
mister x is trying to create a new password for his insta account these are required conditions for creating a new password
condition -1:minimum length-8 and maximum length-15
condition-2: only "@,/"is allowed in a password
condition-3: no spaces are allowed 
condition -4:only alphanumerics are allowed 

you are supposed to print weak if length is exact 8
medium length is between 8 to 12
strong if lenght is between 12 to 15
'''
# str=input()
# contains=str
# a=len(str)
# c=0
# #s="@,/"
# if(str=" "):
#     print("follow conditions")
# for i in str:
#     if(a>8 and a<=12 and i=='@' or i=='/'):
#         print("medium")
#         break
#     elif(a>12 and a<=15 and i=='@' or i=='/'):
#         print("strong")    
#         break
#     elif(a==8 and i=='@' or i=='/'):
#         print("weak")  
#         break
    


password=input()
n=len(password)
count=0
if n<8:
    print("follow conditions")
str="@,/"  
str[0]='@' 
str[1]='/'
for i in password:
    if(i in str[0] or str[i] and i!=" "):
        count+=1
        if(n==8):
            print("weak")
        elif(n>8 and n<=12):
            print("medium")
        elif(n<12 and n<=15):
            print("strong")


        




