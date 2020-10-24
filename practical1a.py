class ArrayModification:
            
    def linear_search(self,lst,n):
        for i in range(len(lst)):
            if lst[i] == n:
                return f'Position :{i}'
        return -1
    
    def insertion_sort(self,lst):
        for i in range(len(lst)):
            
            index = lst[i]
            
            k = i - 1
            
            while k >= 0 and lst[k] > index:
                lst[k + 1] = lst[k]
                k -= 1
                
            lst[k+1]  = index
            
        return lst
    
    def merge(self,lst,lst2):
         lst.extend(lst2)
         print(lst)
    
    def reverse(self,lst):
        return lst[::-1]

lst = [2,9,1,7,3,5,2]
lst2 = [4,6,8,9,4,5]
Arrmod = ArrayModification()
print(Arrmod.linear_search(lst,3))
print(Arrmod.merge(lst,lst2))
print(Arrmod.insertion_sort(lst))
print(Arrmod.reverse(lst))
