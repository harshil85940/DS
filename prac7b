size_list = 6

def hash_function(val):
    global size_list
    return val%size_list

def map_hash_function(hash_return_values):
    return hash_return_values
    
def create_hash_table(list_values,main_list):
    for  values in list_values:
        hash_return_values = hash_function(values)
        list_index = map_hash_function(hash_return_values)
        if main_list[list_index]:
            print("collision detected")
            linear_probing(list_index,values,main_list)
        else:
            main_list[list_index]=values

def linear_probing(list_index,value,main_list):
    global size_list
    list_full = False
    old_list_index=list_index
    if list_index == size_list - 1:
        list_index = 0
    else:
        list_index += 1

    while main_list[list_index]:
        if list_index+1 == size_list:
            list_index = 0
        else:
            list_index += 1
        if list_index == old_list_index:
            list_full = True
            break
    if list_full == True:
         print("list was full. could not saved")


         
        
    
        

def search_list(key,main_list):
    #for i in range(size_list):
    val = hash_function(key)
    if main_list[val] == key:
        print("list found",val)
    else:
        print("not found")
            

list_values = [1,3,8,6,5,14]

main_list = [None for x in range(size_list)]
print(main_list)
create_hash_table(list_values,main_list)
print(main_list)
search_list(5,main_list)
