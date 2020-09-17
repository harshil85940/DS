print ("BINARY SEARCH METHOD\n")
def bsm(arr,start,end,num):
    if end>=start:
        mid=start+(end-start)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return bsm(arr,start,mid-1,x)
        else:
            return bsm(arr,mid+1,end,x)
    else:
        return -1
arr=[10,27,36,49,58,69,70]
x=int(input("Enter the number to be searched : "))
result=bsm(arr,0,len(arr)-1,x)
if result != -1:
    print ("Number is found at ",result)
else:
    print ("Number is not present\n")
   
print ("Linear Search\n")
def linearsearch(arr, x):   
   for i in range(len(arr)):       
      if arr[i] == x:          
        return i    
   return -1 
arr = ['t','u','t','o','r','i','a','l'] 
x = input("enter character you want to search: ") 
print("element found at index "+str(linearsearch(arr,x)))
