# shopping_list_manager.py

def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("----------------------------")

def main():
    """
    Main function to run the Shopping List Manager application.
    It initializes the shopping list and handles user interactions.
    """
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Option to add an item
            item = input("Enter the item to add: ").strip()
            if item: # Ensure item is not empty
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            # Option to remove an item
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.")
                continue

            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' was not found in the list.")
        elif choice == '3':
            # Option to view the current list
            print("\n--- Your Shopping List ---")
            if not shopping_list:
                print("The list is currently empty.")
            else:
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            print("--------------------------")
        elif choice == '4':
                  # Option to exit the application
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please enter a number between 1 and 4.")

# This ensures that main() is called only when the script is executed directly
if __name__ == "__main__":
    main()