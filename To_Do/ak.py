my_list=[]
for i in range(0,6):
    temp_list=[]
    for j in range(0,6):
         temp_list.append(i==j)
    my_list.append(temp_list)
print (my_list)
