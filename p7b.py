def pattern(n):
    for x in range(n):
        for x in range(n):
            print('--- ', end = "")
        print()
        for x in range(n+1):
            print('|  ', end = "")
        print()
    for x in range(n):
        print('--- ', end ="")
    print()

x = int(input("Enter size of board: "))
pattern(x)

'''
Enter size of board: 3
--- --- --- 
|  |  |  |  
--- --- --- 
|  |  |  |  
--- --- --- 
|  |  |  |  
--- --- --- 
'''
