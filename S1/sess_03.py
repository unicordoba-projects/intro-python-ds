faculties = ["Ingenierias", "Educación", "Ciencias Básicas", "MVZ", "Ciencias de la salud"]

for faculty in faculties:
    print(faculty)

# throungh string 
string_ = "Educación"
for char in string_:
    print(char)
    
print(string_.upper())
print(string_.lower())


# Nested loops
for faculty in faculties:
    print("Facultad: ",faculty)
    for char in faculty:
        print(char)
    
# Print numbers from 1 to 10 
for num in range(1, 11):
    print(num)
    
# Print numbers from 1 to 100 
for num in range(1, 101):
    print(num)
    
