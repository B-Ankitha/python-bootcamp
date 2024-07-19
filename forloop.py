'''we have two different types
one is range-----indexing 
normal===value
'''
s="hello world!"
for i in s:
    print(i)

list11=list(map(int,input().split(",")))
for i in range(len(list11)):
    print(list11[i])

list1=list(map(int,input().split(",")))
for i in list1:
    print(i)
