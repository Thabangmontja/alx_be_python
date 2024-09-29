def add_item(shopping_list):
    """Add an item to the shopping list."""
    item = input("Enter the item to add: ")  # Prompt user for input
    shopping_list.append(item)  # Add the item to the shopping list
    print(f"{item} has been added to the shopping list.")

def view_items(shopping_list):
    """Display all items in the shopping list."""
    if shopping_list:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("Your shopping list is empty.")

def main():
    shopping_list = []
    while True:
        print("\n1. Add Item")
        print("2. View Items")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            view_items(shopping_list)
        elif choice == '3':
            print("Exiting the shopping list manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
