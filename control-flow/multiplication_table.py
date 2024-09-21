#Prompt the user for a number
number = int(input("Enter a number to see its' multiplication table: "))

#Generate and print the multiplication table using a for loop
for x in range(1, 11):
    result = number * x
    print(f"{number} * {x} = {result}")