def calculate(start_num):
    def inner_function():
        for num in range(start_num, 10, 3):
            print(num)

    inner_function()

calculate(1)