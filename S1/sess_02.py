# Creating Lists
days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sundayyyyyy']
# index = [0, 1, 2, 3, 4, 5, 6]

# Accessing elements
print(days[0])
print(days[1])
print(days[2])
print(days[-1])

# Accessing the last element
print("Last element: ", days[len(days)-1])
print("Last element: ", days[-1])

# Modifying an element
days[6] = 'Sunday'
print(days)

# Creating matrix
matrix = [[3,4,8], [8,2,7], [1,3,9]]
print(matrix)

print(matrix[0][0])
print(matrix[1][1])
print(matrix[2][2])

matrix[1][2]=100
print(matrix)


# Creating dictionary
user = {"name": "LARRY PACHECO AYAZO", "city": "Monteriaaaaaaaaaaaaa"}
print(user)
print(user["name"])
print(user["city"])

user['city'] = "Monteria"
print(user)