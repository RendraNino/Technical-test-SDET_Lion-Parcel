# Assignment 3
# Write a code to solve the problem below with Phyton

def sort_even_odd(arr):
    # Separate even and odd numbers
    even_numbers = [x for x in arr if x % 2 == 0]
    odd_numbers = [x for x in arr if x % 2 != 0]

    # Sort both lists in descending order
    even_numbers.sort(reverse=True)
    odd_numbers.sort(reverse=True)

    # Combine the even numbers first and then the odd numbers
    return even_numbers + odd_numbers

# Test the function with the given input
input_list = [3, 2, 5, 1, 8, 9, 6]
output_list = sort_even_odd(input_list)

# Print the output
print(output_list)
