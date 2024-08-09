f = open("C://Users//ABIJITH//Downloads//csv.csv",'r')
all_list_data=[]
tag = []
for x in f.read().splitlines():
    re = x.replace('"',"").split(",")
    if len(re[5]) == 0:
       re[5] = "Unallocated"
    all_list_data.append(re)
length_of_list = len(all_list_data[1:])
#get tag names
for i in range(1,length_of_list+1):
    if all_list_data[i][5] not in tag:
       tag.append(all_list_data[i][5])
#calculate all tags durations    
# print(tag)
dummy = []
result={}
add = 0
for x in tag:
    for y in all_list_data:
        if x not in dummy:
            dummy.append(x)
        for z in dummy:
            if z in y:
                # print(y)
                add += float(y[3])
                result[z] = f'{round(add,1)}h'
            else:
                dummy.remove(z)
    add*=0
#calculate total
total=0
for x in result.keys():
    total_add = float(result[x][:-1])
    total+=total_add
result["total for all tags"]=round(total,1)
print(result)

    






