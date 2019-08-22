lst1=[]
lst2=[]

n=int(input("enter the number of elements"))

for i in range(0,n):
     ele=int(input())
     lst1.append(ele)
print(lst1)

for i in lst1:
    if (i%2==0):
        lst2.append(i)
print(lst2)   

    
	
