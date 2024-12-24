import keyword 
print(keyword.kwlist)

# collect details of player information  
'''print("\nEnter details for player 1: ")  
name1 = input('Name for player1: ')  
age1 = int(input('Player1 age: '))  
height1 = float(input("Player1 Height: "))
position1 = input("Player1 Position: ")
is_player_captain1 = input("Ïs player1 captain? (yes/no): ").lower()=="yes"'''

# display the player details  
'''print("\n Team members Details: ")  
print("Player Name: ", name1)  
print("Player age: ", age1)  
print("Player Height: ", height1)
print("Player Position:", position1)
print("Player is captain:" , is_player_captain1)'''

# predict employee salaries based on years of experience  
'''print("\n predict salary based on Experience")  
years_of_experience = int(input("Enter years of experience: "))
curent_salary = int(input("Enter current salary: "))
growth_rate = float(input("Enter growth rate per year in (%): "))
predicted_salary = curent_salary*(1+growth_rate/100)**years_of_experience
print(predicted_salary)'''

## circle area  
r = float(input("Enter Radius: "))  
PI = 3.1416  
area = PI * r *  r
print("Area of Circle:", area)

##triangle area
b = float(input("Enter Base: "))
h = float(input("Enter Height: "))
area = 0.5 * b * h
print("Area of Triangle:", area)