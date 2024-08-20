def greet():
   name="shriya"
   return lambda:"Hi " + name
#return nested anonymous function 
message=greet()
print(message())
#a function named greet( that returns a nested lambda function)