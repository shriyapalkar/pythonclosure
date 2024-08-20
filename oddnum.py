def calculate():
    
        def inner_function(start_num):
            for i in range(100):  
                start_num += 2
                print(start_num)

        inner_function(1)
calculate()