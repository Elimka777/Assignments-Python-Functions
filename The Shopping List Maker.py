def add_item(shopping_list, item):   # Function to add items to the shopping list
    shopping_list.append(item)
    print(f"Item {item} added to the list.")

def remove_item(shopping_list, item):   # Function to remove items from the shopping list
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'{item} removed from the list.')
    else:
        print(f'{item} not found in the list.')

def print_list(shopping_list):
    if shopping_list:
        print("Shopping list:")
        for index in range(len(shopping_list)):
          print(f'{index+1}. {shopping_list[index]}')
    else:
        print('Shopping list is empty.')
    
# Function to run the program
def make_list():
    shopping_list = []
    while True:
        print("\nOptions:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Print List")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            item = input("Enter item to add: ")
            add_item(shopping_list, item)
        elif choice == '2':
            item = input("Enter item to remove: ")
            remove_item(shopping_list, item)
        elif choice == '3':
            print_list(shopping_list)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")
            
if __name__ == "__main__":
    make_list()
    
    
    