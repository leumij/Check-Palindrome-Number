# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

# Pseudocode
# Ask user for input
number = input("Enter a 3 digit number: ")
print("Original number ",number)
reverse_num = str(number[::-1])

# If else for original number and reserve number
if int(number) == int(reverse_num):
    print("Yes. given number is palindrome number")
else:
    print("No. given number is not palindrome number")