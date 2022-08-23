# This program read n numbers from the user and then search for a number in the list.

import random
import unittest

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


# unit test
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = 5
# 

class TestLinearSearch(unittest.TestCase):
    def test_linearSearch(self):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 5
        self.assertEqual(linearSearch(list, n), True)
        n = 11
        self.assertEqual(linearSearch(list, n), False)
        n = 0
        self.assertEqual(linearSearch(list, n), False)
        n = -1
        self.assertEqual(linearSearch(list, n), False)
        n = 100
        self.assertEqual(linearSearch(list, n), False)
        n = -100
        self.assertEqual(linearSearch(list, n), False)
        n = 0.1
        self.assertEqual(linearSearch(list, n), False)
        n = -0.1
        self.assertEqual(linearSearch(list, n), False)
        n = 1.1
        self.assertEqual(linearSearch(list, n), False)
        n = -1.1
        self.assertEqual(linearSearch(list, n), False)
        n = "1"
        self.assertEqual(linearSearch(list, n), False)
        n = "1.1"
        self.assertEqual(linearSearch(list, n), False)
        n = "1.1.1"
        self.assertEqual(linearSearch(list, n), False)


if __name__ == "__main__":
    unittest.main()
    # main()