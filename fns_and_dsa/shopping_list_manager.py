def display_menu():
    """Display the menu options to the user."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to run the shopping list manager."""
    shopping_list = []  # Start with an empty shopping list
    while True:
        display_menu()  # Display the menu options
        choice = input("Enter your choice: ")  # Get user input

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")  # Ask for item name
            shopping_list.append(item)  # Add item to the list
            print(f"Added '{item}' to the shopping list.")
        elif choice == '2':
            # Prompt for and remove an item
            item_to_remove = input("Enter the item to remove: ")  # Ask for item name
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)  # Remove item from the list
                print(f"Removed '{item_to_remove}' from the shopping list.")
            else:
                print(f"Item '{item_to_remove}' not found in the shopping list.")
        elif choice == '3':
            # Display the shopping list
            print("\nCurrent Shopping List:")
            if shopping_list:  # Check if the list is not empty
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")  # Print each item
            else:
                print("The shopping list is empty.")  # Handle empty list case
        elif choice == '4':
            print("Goodbye!")  # Exit message
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

if __name__ == "__main__":
    main()  # Run the main function

