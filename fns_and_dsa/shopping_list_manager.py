def display_menu():
    """Display the menu options to the user."""
    print("\n--- Shopping List Manager ---")
    print("1. Add item to the shopping list")
    print("2. View shopping list")
    print("3. Remove item from the shopping list")
    print("4. Exit")

def main():
    shopping_list = []  # Implement an array (list) for the shopping list
    
    while True:
        display_menu()  # Call the display_menu function
        choice = input("Enter your choice (1-4): ")  # Implement choice input as a number

        # Validate if the input is a number
        if not choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        choice = int(choice)  # Convert choice to an integer
        
        if choice == 1:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"Added '{item}' to the shopping list.")
        elif choice == 2:
            print("\nShopping List:")
            for idx, item in enumerate(shopping_list, start=1):
                print(f"{idx}. {item}")
        elif choice == 3:
            item_to_remove = input("Enter the item to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"Removed '{item_to_remove}' from the shopping list.")
            else:
                print(f"Item '{item_to_remove}' not found in the shopping list.")
        elif choice == 4:
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
