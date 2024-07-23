''''WAP to print the all the consonents count'''
# check=['a','e','i','o','u']
# c=0
# str=input()
# convert=str.lower()
# for i in convert:
#     if i not in check:
#         c+=1
# print(c)       


# check=['a','e','i','o','u']
# c=0
# c1=0
# str=input()
# for i in str:
#     if i in check:
#         c+=1
#     else:
#         c1+=1
# print(c1)        

check=['a','e','i','o','u']
atoz="bcdfghjklmnpqrstvwxyz"
c=0
count=0
str=input()
for i in str:
    if i in check:
        c+=1
print(c)        
for i in str:
    if i in atoz:
        count+=1        
print(count)        
