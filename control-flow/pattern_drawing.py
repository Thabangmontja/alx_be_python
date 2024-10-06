# Prompt the user for the size of the pattern 
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Using a loop to print asterisks(*) side by side
    for _ in range(size):
        print("*", end="")  # To print without a newline
    print()  # To move to the next line after each row
    row += 1  # Increment the row counter
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
