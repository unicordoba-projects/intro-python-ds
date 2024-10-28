days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# print(days)

for day in days:
    print(day)
    
string_ = "Diplomado"
for char in string_:
    print(char)

print(string_.upper())


for num in range(1, 11):
    print(num)


for num in range(1, 11, 2):
    print(num)

for num1 in range(1, 6):
    for num2 in range(1, 2):
        print("Ciclo 1: ", num1, "For 2: ", num2)
        
        

num2 = 400
if num2 % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
    
edad = 91
if edad >= 90:
    print("20+=")
elif edad >= 80:
    print("80-90")
else:
    ...