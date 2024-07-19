height_x=int(input())
weight_x=int(input())
height_y=int(input())
weight_y=int(input())
x_selected=0
y_selected=0

if(height_x==140 and weight_x%2==0  and (height_y >=118 and height_y>=148) and weight_y%7==0 ):
    x_selected+=1
    y_selected+=1
    print("both selected")
else:
    print("not selected") 
if(x_selected==1 and y_selected==1):
    print("all three freinds meet")       


        