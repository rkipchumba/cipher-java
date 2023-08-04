# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None


# # class LinkedList:
# #     def __init__(self):
# #         self.head = None

# #     def is_empty(self):
# #         return self.head is None

# #     def append(self, data):
# #         new_node = Node(data)
# #         if self.is_empty():
# #             self.head = new_node
# #         else:
# #             current = self.head
# #             while current.next:
# #                 current = current.next
# #             current.next = new_node

# #     def display(self):
# #         if self.is_empty():
# #             print("Linked list is empty")
# #         else:
# #             current = self.head
# #             while current:
# #                 print(current.data, end=" ")
# #                 current = current.next
# #             print()


# # # Create an instance of LinkedList
# # my_list = LinkedList()

# # # Append elements to the linked list
# # my_list.append(10)
# # my_list.append(20)
# # my_list.append(30)
# # my_list.append(40)

# # # Display the linked list
# # my_list.display()

# # from typing import List


# # def find_closest_numbers(arr: List[int], K: int, X: int) -> List[int]:
# #     result = []
# #     length = len(arr)
# #     left = 0
# #     right = length - 1

# #     # Modified binary search to find the position of X or closest element to X
# #     while left <= right:
# #         mid = (left + right) // 2
# #         if arr[mid] == X:
# #             left = mid
# #             break
# #         elif arr[mid] < X:
# #             left = mid + 1
# #         else:
# #             right = mid - 1

# #     while right - left + 1 < K:
# #         if left > 0 and right < length - 1:
# #             if abs(arr[left - 1] - X) <= abs(arr[right + 1] - X):
# #                 left -= 1
# #             else:
# #                 right += 1
# #         elif left > 0:
# #             left -= 1
# #         elif right < length - 1:
# #             right += 1

# #     for i in range(left, right + 1):
# #         result.append(arr[i])

# #     return result


# # arr = [2, 4, 5, 6, 9]
# # K = 3
# # X = 7
# # result = find_closest_numbers(arr, K, X)
# # print(result)


# # def recursive_binary_search(list, target):

# #     if len(list) == 0:
# #         return False
# #     else:
# #         midpoint = (len(list)) // 2
# #         if list[midpoint] == target:
# #             return True
# #         elif list[midpoint] < target:
# #             return recursive_binary_search(list[midpoint + 1:], target)
# #         else:
# #             return recursive_binary_search(list[:midpoint], target)


# # numbers = [num for num in (range(0, 10))]
# # print(numbers)

# # import time

# # # Linear Search


# # def linear_search(arr, target):
# #     for i in range(len(arr)):
# #         if arr[i] == target:
# #             return i
# #     return -1  # Element not found

# # # Hashing


# # def hash_search(arr, target):
# #     hash_table = {}
# #     for i in range(len(arr)):
# #         hash_table[arr[i]] = i

# #     if target in hash_table:
# #         return hash_table[target]
# #     else:
# #         return -1  # Element not found


# # # Test the time complexity
# # input_sizes = [1000, 10000, 100000]  # Different input sizes to test
# # target = 999  # Target element for the search algorithms

# # # Measure time for linear search
# # print("Linear Search:")
# # for size in input_sizes:
# #     arr = list(range(size))
# #     start_time = time.time()
# #     linear_search(arr, target)
# #     end_time = time.time()
# #     execution_time = end_time - start_time
# #     print(f"Input Size: {size}, Execution Time: {execution_time} seconds")

# # # Measure time for hashing
# # print("\nHashing:")
# # for size in input_sizes:
# #     arr = list(range(size))
# #     start_time = time.time()
# #     hash_search(arr, target)
# #     end_time = time.time()
# #     execution_time = end_time - start_time
# #     print(f"Input Size: {size}, Execution Time: {execution_time} seconds")


# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None


# # def reverse_linked_list(head):
# #     previous = None
# #     current = head

# #     while current is not None:
# #         next_node = current.next
# #         current.next = previous
# #         previous = current
# #         current = next_node

# #     head = previous
# #     return head


# # # Create the linked list: 1 -> 2 -> 3 -> 4 -> None
# # node1 = Node(1)
# # node2 = Node(2)
# # node3 = Node(3)
# # node4 = Node(4)

# # node1.next = node2
# # node2.next = node3
# # node3.next = node4

# # # Print the original linked list
# # current = node1
# # while current is not None:
# #     print(current.data, end=" -> ")
# #     current = current.next
# # print("None")

# # # Reverse the linked list
# # new_head = reverse_linked_list(node1)

# # # Print the reversed linked list
# # current = new_head
# # while current is not None:
# #     print(current.data, end=" -> ")
# #     current = current.next
# # print("None")


# # # Compute the cost to make the recipe based on ingredients cost
# # # Example:
# # # computeCost(["bread","meat","bread"], [("bread",1),("meat",2)]) => 4

# # def computeCost(recipe, ingredients_costs):
# #     total_cost = 0
# #     i = 0
# #     while i < len(recipe):
# #         ingredient = recipe[i]
# #         i += 1

# #         # Find and add the cost of the ingredient to the total cost
# #         for cost in ingredients_costs:
# #             if cost[0] == ingredient:
# #                 total_cost += cost[1]

# #     return total_cost


# # def main():
# #     costs = [
# #         ("bread", 1), ("tomatoes", 2),
# #         ("cheese", 4), ("meat", 5)
# #     ]

# #     burger = [
# #         "bread", "meat", "cheese", "tomatoes", "bread"
# #     ]

# #     result = computeCost(burger, costs)
# #     print(result)


# # main()

# # def linear_search(arr, target):
# #     matches = []  # Create an empty list to store the matching elements
# #     for i in range(len(arr)):
# #         if arr[i] == target:
# #             # Add the matching element to the matches list
# #             matches.append(arr[i])
# #             break
# #     return matches  # Return the list of matching elements


# # # Example usage:
# # my_list = [4, 2, 7, 1, 5, 7, 7]
# # target_element = 7
# # result = linear_search(my_list, target_element)
# # if len(result) > 0:
# #     print(f"Elements {result} match the target element {target_element}")
# # else:
# #     print(f"No elements match the target element {target_element}")

# # def merge_sorted_arrays(arr1, arr2):
# #     merged = []
# #     i, j = 0, 0

# #     while i < len(arr1) and j < len(arr2):
# #         if arr1[i] <= arr2[j]:
# #             merged.append(arr1[i])
# #             i += 1
# #         else:
# #             merged.append(arr2[j])
# #             j += 1

# #     # Add remaining elements from arr1, if any
# #     while i < len(arr1):
# #         merged.append(arr1[i])
# #         i += 1

# #     # Add remaining elements from arr2, if any
# #     while j < len(arr2):
# #         merged.append(arr2[j])
# #         j += 1

# #     return merged


# # array1 = [1, 3, 5, 7, 8, 9, 7]
# # array2 = [2, 4, 6, 8, 0]
# # merged_array = merge_sorted_arrays(array1, array2)
# # print(merged_array)

# # def climbStairs(n):
# #     if n <= 1:
# #         return 1

# #     ways = [0] * (n + 1)
# #     ways[0] = 1
# #     ways[1] = 1

# #     for i in range(2, n + 1):
# #         ways[i] = ways[i-1] + ways[i-2]

# #     return ways[n]


# # n = 5
# # distinct_ways = climbStairs(n)
# # print(f"The number of distinct ways to climb {n} steps is: {distinct_ways}")

# # def find_median_sorted_arrays(nums1, nums2):
# #     merged = merge_sorted_arrays(nums1, nums2)  # Step 1
# #     length = len(merged)  # Step 2

# #     if length % 2 == 1:  # Step 3
# #         return merged[length // 2]
# #     else:
# #         mid_right = merged[length // 2]
# #         mid_left = merged[length // 2 - 1]
# #         return (mid_left + mid_right) / 2


# # def merge_sorted_arrays(nums1, nums2):
# #     merged = []
# #     i, j = 0, 0

# #     while i < len(nums1) and j < len(nums2):
# #         if nums1[i] <= nums2[j]:
# #             merged.append(nums1[i])
# #             i += 1
# #         else:
# #             merged.append(nums2[j])
# #             j += 1

# #     while i < len(nums1):
# #         merged.append(nums1[i])
# #         i += 1

# #     while j < len(nums2):
# #         merged.append(nums2[j])
# #         j += 1

# #     return merged

# # for i in range(5):
# #     for j in range(4):
# #         print(i, j)

# # You run a support questions and answers website like StackOverflow.
# # Recently, the amount of questions has grown dramatically.
# # A group of engineers has volunteered to help but each volunteer has a    prioritized list of tags they can support.

# # Volunteers must be assigned questions with tags from their personal tags list.

# # Here is example data in JSON form:

# # {
# #     "questions": [
# #         {
# #             "id": "0",
# #             "title": "how do i install vs code",
# #             "tags": ["mac", "vs code"]
# #         },
# #         {
# #             "id": "1",
# #             "title": "my program is too slow please help",
# #             "tags": ["python", "ai"]
# #         },
# #         {
# #             "id": "2",
# #             "title": "why is the hitbox off by 2 pixels",
# #             "tags": ["c#", "game"]
# #         },
# #         {
# #             "id": "3",
# #             "title": "my dependency injection stack trace is strange",
# #             "tags": ["java", "oop"]
# #         },
# #         {
# #             "id": "4",
# #             "title": "socket.recv is freezing",
# #             "tags": ["python", "networking"]
# #         },
# #         {
# #             "id": "5",
# #             "title": "i have a memory leak",
# #             "tags": ["c++", "networking"]
# #         }
# #     ],
# #     "volunteers": [
# #         {
# #             "id": "sam5k",
# #             "tags": ["python", "networking"]
# #         },
# #         {
# #             "id": "djpat",
# #             "tags": ["ai"]
# #         },
# #         {
# #             "id": "jessg",
# #             "tags": ["java", "networking"]
# #         },
# #         {
# #             "id": "rayo",
# #             "tags": ["java", "networking"]
# #         }
# #     ]
# # }
# # # Create a function that returns an assignments object like so:

# # [{'question': '1', 'volunteer': 'sam5k'},
# #  {'question': '3', 'volunteer': 'jessg'},
# #  {'question': '4', 'volunteer': 'rayo'}]


# # class Solution(object):
# #     def convert(self, s, numRows):
# #         """
# #         :type s: str
# #         :type numRows: int
# #         :rtype: str
# #         """

# #         if numRows == 1 or numRows >= len(s):
# #             return s

# #         L = [''] * numRows
# #         index, step = 0, 1

# #         for x in s:
# #             L[index] += x
# #             if index == 0:
# #                 step = 1
# #             elif index == numRows - 1:
# #                 step = -1
# #             index += step

# #         return ''.join(L)

# # fruits = ['apple', 'banana', 'orange']

# # # Using enumerate to iterate over the list 'fruits'
# # for index, fruit in enumerate(fruits):
# #     print(f"Index {index}: {fruit}")


# # def largest_palindrome_product(n):
# #     if n == 1:
# #         return 9

# #     upper_bound = 10**n - 1
# #     lower_bound = 10**(n - 1)

# #     max_palindrome = 0

# #     for i in range(upper_bound, lower_bound - 1, -1):
# #         num_str = str(i)
# #         palindrome = int(num_str + num_str[::-1])  # Construct palindrome from left half
# #         for j in range(upper_bound, lower_bound - 1, -1):
# #             if palindrome // j > upper_bound:
# #                 break
# #             if palindrome % j == 0:
# #                 return palindrome % 1337

# #     return 0  # If no palindrome is found

# # # Test the function
# # n = 3
# # result = largest_palindrome_product(n)
# # print(result)  # Output will be the largest palindromic integer modulo 1337 for n=3


# # def findOrder(height, infront):
# #     # Combine the height and infront values into pairs
# #     people = list(zip(height, infront))

# #     # Sort the people list in decreasing order of height and increasing order of infront
# #     people.sort(key=lambda x: (-x[0], x[1]))

# #     # Reconstruct the queue based on the infront value
# #     queue = []
# #     for person in people:
# #         queue.insert(person[1], person[0])

# #     return queue


# # # Example usage:
# # height = [5, 3, 2, 6, 1, 4]
# # infront = [0, 1, 2, 0, 3, 2]
# # reconstructed_queue = findOrder(height, infront)
# # print(reconstructed_queue)
# # # Output will be [190, 180, 175, 155, 165, 200]


# # def caesar_cipher_encrypt(plaintext, shift):
# #     encrypted_text = ""
# #     for char in plaintext:
# #         if char.isalpha():
# #             # Determine if the character is uppercase or lowercase
# #             is_uppercase = char.isupper()

# #             # Convert the character to uppercase to simplify the process
# #             char = char.upper()

# #             # Apply the Caesar's cipher shift
# #             shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

# #             # Convert the character back to lowercase if it was originally lowercase
# #             if not is_uppercase:
# #                 shifted_char = shifted_char.lower()

# #             encrypted_text += shifted_char
# #         else:
# #             encrypted_text += char

# #     return encrypted_text


# # def caesar_cipher_decrypt(ciphertext, shift):
# #     # Decryption is just the reverse of encryption, so we use the negative shift value
# #     return caesar_cipher_encrypt(ciphertext, -shift)


# # # Example usage:
# # plaintext = "Hi"
# # shift = 2

# # # Encryption
# # encrypted_text = caesar_cipher_encrypt(plaintext, shift)
# # print("Encrypted:", encrypted_text)

# # # Decryption
# # decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
# # print("Decrypted:", decrypted_text)


# def caesar_cipher_encrypt(plaintext, key):
#     encrypted_text = ""
#     for char in plaintext:
#         if char.isalpha():
#             is_uppercase = char.isupper()
#             char = char.upper()

#             # Apply the Caesar's cipher shift
#             shifted_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))

#             # Convert the character back to lowercase if it was originally lowercase
#             if not is_uppercase:
#                 shifted_char = shifted_char.lower()

#             encrypted_text += shifted_char
#         else:
#             encrypted_text += char

#     return encrypted_text


# def caesar_cipher_decrypt(ciphertext, key):
#     # Decryption is just the reverse of encryption, so we use the negative key value
#     return caesar_cipher_encrypt(ciphertext, -key)


# # Example usage
# plaintext = "HI"
# key = 20

# # Encrypt the plaintext using the key
# ciphertext = caesar_cipher_encrypt(plaintext, key)
# print("Encrypted:", ciphertext)  # Output: "JGNNQ"

# # Decrypt the ciphertext using the same key
# decrypted_text = caesar_cipher_decrypt(ciphertext, key)
# print("Decrypted:", decrypted_text)  # Output: "HELLO"


def generate_braces_combinations(N):
    def backtrack(combination, open_count, close_count):
        if len(combination) == 2 * N:
            combinations.append(combination)
            return

        if open_count < N:
            backtrack(combination + '(', open_count + 1, close_count)

        if close_count < open_count:
            backtrack(combination + ')', open_count, close_count + 1)

    combinations = []
    backtrack('', 0, 0)
    return combinations


def print_braces_combinations(N):
    combinations = generate_braces_combinations(N)
    for combination in combinations:
        print(combination)


N = 3  # Replace this with the desired value of N
print_braces_combinations(N)
