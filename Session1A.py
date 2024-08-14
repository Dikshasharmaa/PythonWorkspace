# Multi Value Container

#Create operation -> Homogeneous
numbers = 10, 20, 30, 40

#Read operation
print(numbers, id (numbers), type(numbers))

#Create Operation -> Hetrogeneous
data = [10, 10.2, "hello", "wow", 200]
print(data, id(data), type(data))
print(data[0], id(data[0]), type(data[0]))
print(data[1], id(data[1]), type(data[1]))
print(data[2], id(data[2]), type(data[2]))

#Reference Copy Operation
my_data= data
print(my_data, id(my_data))
print(my_data[3])

#Update Operation -> tuple is immutable so can't update the values
 # my_data[3] = "awesome"
# to support immutable property I am gonna put square brackets and make it list. -> List is immutable
my_data[3] = "awesome"
print(my_data)