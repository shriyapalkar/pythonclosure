def calculate():
    num=1
    def inner_function():
    
          for num in range(1,10):
            num+=2
            print(num)

    inner_function()
calculate()
       
         
        
    #print("Final value of num:", num)



        
    
            
def calculate():
    num = 1

    def inner_func():
        #we are using "non-local" keyword.
        '''nonlocal' is used to access and modify variables from
        the nearest enclosing scope that is not global'''
        nonlocal num
        num += 2
        return num
    return inner_func

odd = calculate()

print(odd())