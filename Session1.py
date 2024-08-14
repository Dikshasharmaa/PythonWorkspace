#Single value Container
from traceback import print_tb

#Creating Operation
instagram_user_name ="diksha"

#Read operation
print(instagram_user_name, id(instagram_user_name))  #id gives the memory location
print(instagram_user_name, hex(id(instagram_user_name)))  #in RAM
print(instagram_user_name, oct(id(instagram_user_name)))
print(instagram_user_name, bin(id(instagram_user_name)))
print(type(instagram_user_name))

user_name = "diksha_sharma"
print(user_name,id(user_name), type(user_name))

#user_name is a reference variable which will be created in Stack.
#Value diksha_sharma is created within the storage container of type string in Heap.

user= "diksha_sharma"
print(user, id(user), type(user))
# here the id will be same because it refers to the same storage container


#Copy Operation
another_user = user
print(another_user, id(another_user), type(another_user))

#Update operation
user = "akash"
print(user, id(user), type(user))

# Delete operation
del user
print(user, id(user), type(user))