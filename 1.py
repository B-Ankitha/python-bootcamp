

#9
'''find the  element that is prsent in the k+n(th) index
TC 1
k== given by user ==3
n=2
input parametrers 3 6 8 4 61 2
the output is 2 
TC-2
k=3
n=4
80 70 54 36 72'''



''''solution
input of a k
input of A N
INPUT OF LIST
a variable took and stored the k+n th value 
l is var in which we consider the length function 




for i in range(len(list1)):
break
print(list1[a])

break ----it will come out loop after finding the particular elememt '''

k=int(input())
n=int(input())
list1=list(map(int,input().split(" ")))
a=k+n
l=len(list1)
if(l<a):
    print("ERROR")
else:
    for i in range(0,l):
        print(list1[a])
        break

