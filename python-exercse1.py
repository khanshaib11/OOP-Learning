# User Authentication & Setup
captain_name = input("Enter Captain Name: ").strip().title()   # Capitalized
ship_id = input("Enter Ship ID: ").strip().upper()             # Uppercase

credits = 1000.0   # float
fuel = 100         # int
inventory = []     # list

print(f"\nWelcome, Captain {captain_name}!")
print(f"Ship ID: {ship_id}")
print(f"Credits: {credits}, Fuel: {fuel}, Inventory: {inventory}\n")

# Navigation System (3x3 2D list)
sector_map = [
    ["Empty Space", "Station",     "Empty Space"],
    ["Empty Space", "Empty Space", "Empty Space"],
    ["Empty Space", "Empty Space", "Station"]
]

print("=== Star Sector Map ===")
for row in sector_map:
    for cell in row:
        print(f"{cell:13}", end=" ")
    print()
  
    
while True:
    user = input("Enter a command: ")
    if user == "move":
        print("Please enter X and Y coordinates inside the 3x3 coordinates only! ")
        x_input = input(" X ").strip()
        y_input = input(" Y ").strip()
        if not x_input.isdigit() or not y_input.isdigit():
            print("Invalid input. Coordinates must be numbers from 0 to 2.\n")
            continue
        x = int(input()).strip()
        y = int(input()).strip()
        
        if x < 0 or x > 2 and y < 0 or y > 2 :
            print("please enter between 0 to 2 not lower or upper between (0-2) ")
            continue
        ## moving cost using fuel sir g 
        if fuel < 10:
            print("Fuel is less then required 10 condition sorry sir we cannot go anymore :(: )")
        
        fuel -= 10
        current_x = x
        current_y = y
        print(f"Move to ({current_x}), {current_y}. Fuel left: {fuel}") 
        print(f"sector: {sector_map[current_y][current_x]}")  
        
       
        
            
    
            