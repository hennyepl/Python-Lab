# This program read n numbers from the user and then search for a number in the list.

import random

def linearSearch(list, n):
    for i in range(len(list)):
        if list[i] == n:
            return True
    return False


def main():
    n = int(input("Enter the number of elements in the list: "))
    list = []
    for i in range(n):
        list.append(random.randint(1, 100))
    print(list)
    n = int(input("Enter the number to search: "))
    if linearSearch(list, n):
        print("Found")
    else:
        print("Not found")

# print out
if __name__ == "__main__":
    main()
    