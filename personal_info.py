# --------------------------------------------------
# Name: Kunal Khandpekar
# Project: Personal Information Manager
# Description: Stores and displays personal info
# --------------------------------------------------

# ===== WELCOME MESSAGE =====
print("=" * 45)
print("      PERSONAL INFORMATION MANAGER")
print("=" * 45)
print()

# ===== STATIC INFORMATION (Stored in variables) =====
# String variable storing my name
name = "Kunal Khandpekar"

# Integer variable storing my age
age = 21

# String variable storing city
city = "Pune"

# String variable storing hobby
hobby = "Cooking"

# ===== USER INPUT SECTION =====
print("Tell me about yourself")
print("-" * 30)

# Function for safe input (basic validation)
def get_valid_input(message):
    user_input = input(message).strip()   # removes spaces
    
    # keep asking until valid input
    while user_input == "":
        print("❌ Input cannot be empty. Please try again.")
        user_input = input(message).strip()
    
    # format nicely
    return user_input.title()

# Ask for favorite food
favorite_food = get_valid_input("What's your favorite food? :")

# Ask for favorite color
favorite_color = get_valid_input("What's your favorite color? :")

# ===== CALCULATIONS =====
# Calculate age in months
age_in_months = age * 12

# ===== DISPLAY OUTPUT =====
print()
print("=" * 45)
print("            YOUR INFORMATION")
print("=" * 45)
print()

# Using f-strings for formatting
print(f"Name           : {name.upper()}")
print(f"Age            : {age} years ({age_in_months} months)")
print(f"City           : {city.title()}")
print(f"Hobby          : {hobby.capitalize()}")
print("-" * 45)
print(f"Favorite Food  : {favorite_food}")
print(f"Favorite Color : {favorite_color}")

print()
print("=" * 45)
print("Thank you for using this program! 👋")
print("=" * 45)
