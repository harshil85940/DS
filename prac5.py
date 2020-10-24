class Array:
    
    def __init__(self,array,number):
        self.lst = sorted(array)
        self.number = number
    def binary_search(self,lst,n,start,end):
    
        if start <= end:
            mid = (end + start) // 2
            if lst[mid] == n:

                return f'position: {mid}'
            elif lst[mid] > n:
                return binary_search(lst,n,start,mid-1)
            else:
                return binary_search(lst,n,mid + 1,end)
        else:
            return -1
            
    
    def linear_search(self,lst,n):
        for i in range(len(lst)):
            if lst[i] == n:
                return f'Position :{i}'
        return -1
    
    def run_search(self):
        while True:
            print('Select the searching algorithm:')
            print('1. Linear Search.')
            print('2. Binary Search.')
            print('3. quit.')
            opt = int(input('Option: '))
            if opt == 2:
                print(search.binary_search(self.lst,self.number,0,len(lst)-1))
            elif opt == 1:
                print(search.linear_search(self.lst,self.number))
            else:
                break
        

lst = [1,2,3,4,5,6,7,8]
number = 4
search = Array(lst,number)
search.run_search()    
