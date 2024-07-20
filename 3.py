''''find the max element in a given list

TC-1
12 23 36 44 45 57
57==output
------------
tc-2
56 78 -8 12 34 -99
78==output

'''

list1=list(map(int,input().split(" ")))
a=len(list1)
for i in range(a):
    max1=list1[1]
    if(max1>list1[i]):
        print(max1)  

list1=list(map(int,input().split(" ")))
a=len(list1)
for i in range(a):
    max1=list1[1]
    if(max1>list1[i]):
        max1=list1[i]


''' another method using for loop with accessing elements directlt
'''
list1=list(map(int,input().split(" ")))
for i in list1:
    max1=list1[1]
    if(max1>i):
        print(max1)  
        break  
''''directly using max() function '''
list1=list(map(int,input().split(" ")))
print(max(list1))