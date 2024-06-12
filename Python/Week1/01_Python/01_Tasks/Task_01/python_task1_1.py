find=[1,4,6,7,4,4,5]


def find_in_list(find,num):
    count = 0
    for num_to_find_count in find:
        if num_to_find_count == num:
            count = count+1
    return count

print(find_in_list(find,4))

#for i in range(0,5):
#    if find[i] == 4:
#        count = count+1

#for i in find:
#    if i == 4:
#        count = count+1
#print(count)
