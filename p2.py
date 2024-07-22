'''swap 2 elements without using the third variable
'''
'''method -1'''
# a,b=map(int,input().split(" "))
# print(b,a)
'''method-2'''
# a,b=map(int,input().split(" "))
# b=(a*b)//a
# a=(a*b)//b
# print(b,a)
'''method -3'''
# a,b=map(int,input().split(" "))
# a=a+b
# b=a-b
# a=a-b
# print(a,b)

'''method -4===xor method'''
a,b=map(int,input().split(" "))
a=a^b
b=a^b
a=a^b
print(a,b)
'''sum of elements in array'''
# n=int(input())
# #list1=list(map(int,input().split(" ")))
# s=0
# for i in range(1,n+1):
#     s+=i
# print(s)    


