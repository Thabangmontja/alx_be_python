# Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Loop through numbers 1 to 10
for i in range(1, 11):
    # Print the multiplication table in the format X * Y = Z
    print(f"{number} * {i} = {number * i}")
