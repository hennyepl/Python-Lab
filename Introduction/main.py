# Call source code from other file

import source

# Create a binary search tree
# ask user to enter data and interact with the data
# menu 

def main():
    bst = source.BinarySearchTree()
    while True:
        print("""
        1. Insert
        2. Delete
        3. Find
        4. Print
        5. Exit
        """)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter data: "))
            bst.insert(data)
        elif choice == 2:
            data = int(input("Enter data: "))
            bst.delete(data)
        elif choice == 3:
            data = int(input("Enter data: "))
            if bst.find(data):
                print("Found")
            else:
                print("Not found")
        elif choice == 4:
            bst.print()
        elif choice == 5:
            break
        else:
            print("Invalid choice")