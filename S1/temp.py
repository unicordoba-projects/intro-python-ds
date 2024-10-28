x=10
y=4.5
name = "Módulo 1 - Intro Python"
status=True
# muestra los atributos y métodos de un objeto

print(name)
print(dir(name))
print(name.upper())
print(type(x))
print(type(y))
print(type(status))
print(type(name))

# help(str)

# Muesra lo que esta en la memoria
print(dir())

# Rangos
for i in range(3):
    print(name)
    
for i in range(3):
    print(i)
    
for i in range(2, 20, 2):
    print(i)

# help(list)


var15 = list(range(5))
print(var15)
# # Creating Integer Variables
# x_int_1 = -100
# x_int_2 = 12

# # Summing Integer Variables
# X_int_sum = x_int_1 + x_int_2

# # Subtracting Integer Variables
# X_int_sub = x_int_1 - x_int_2
# print(x_int_1)
# print(x_int_2)
# print("Sum of two integer values of x_int_1 and x_int_2", X_int_sum)
# print(X_int_sub)

# # Creating Floating Number Variables
# X_flout = -0.25

# # Summing Floating Number and Integer Variable
# x_flout_int_sum = X_flout + x_int_1
# print(X_flout)
# print(x_flout_int_sum)

# # Creating String Type of Variable
# X_string = "Hellow to the world of Data Science"
# print(X_string)

# # Creating Arrays
# X_array = [1.0, 0.25, 0.55, -0.0009]
# X_array2 = [2.33, 0.955, 0.66, 0.33]
# print(X_array)
# print(X_array2)

# # Creating Lists
# X_list1 = [2, "three", 5.0, True]
# X_list2 = [4.0, 4.667, False, True, X_string, 6]
# print(X_list1)
# print(X_list2)