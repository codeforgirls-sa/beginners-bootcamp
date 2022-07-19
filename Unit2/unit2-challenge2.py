# Slide 117
# Step 1: Assign values
current_year=2022
# Step 2: obtain year of birth
birth_year = input("Enter year of birth (Ex:1997): ")

# Step 3: turn the value from string to number
birth_year = eval(birth_year)

# Step 4: calculate the age
age = current_year - birth_year

# Step 5: display the age
print("Your age now is ", age)