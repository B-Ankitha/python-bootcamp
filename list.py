'''list are similar to arrays,but not exactly,list are capable of having heterogeneous values,list are mutable(can me modified,alterd after declaration easily),
list1=[]#declaration 
list is ordered
append in the elemets at  end of the list
* will remove the "," and "[]" in the output
sort==asscend and desecend()
copy==same thing,,,if we r 
clear
reverse
slice
count == one parameter
pop===delete the last element 
insert (at a particular index and value to which u want insert )
sort tales tc as (nlogn)===similar to quick sort
 '''
#declaration
my_list=[1,2,3,4]
#print(*my_list,end="")
#print(*my_list)
#print(my_list,end="")
my_list.append(9999)#default at last the value is stored
print(my_list)
my_list.insert(0,9999)# insert at particular 
print(my_list)
my_list.pop()
print(my_list)
my_list.pop(3)#particular index
#if out of index we gave it will through an errror as out of range 
#my_list.pop(45)
print(my_list)
my_list_2=[5,6,7,8]
new_list=my_list+my_list_2#"+" concatenate not the addition
print(*new_list)
new_list=my_list.copy()#no effect  on the new list
print(new_list)
cnt=my_list.count(2)
print(cnt)
list11=[-1,2,1,5,3,7,8,9,22,6]
print(list11.sort())
list11.sort()
print(*list11)
list12=[]
list12=list11.sort()
print(list12)
'''arrgregate functions
count
max
min
sum
'''
print(sum(my_list))
print(min(my_list))
print(max(my_list))
#print(count(my_list))
print(my_list.count(1))





