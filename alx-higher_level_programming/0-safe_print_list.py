#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    total = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            total += 1
        except IndexError:
            break
    print("")
    return (total)


'''
def safe_print_list(my_list=[], x=0):
    try:
        # Initialize a count for the number of elements printed
        count = 0

        # Iterate through the list
        for item in my_list:
            # Print the item
            print(item, end=' ')
            count += 1

            # Check if the desired number of elements has been printed
            if count == x:
                break

    except Exception as e:
        # Handle any exceptions that might occur during the iteration
        print(f"An exception occurred: {e}")

    # Print a newline to separate the output from other print statements
    print()

    return count

# Example usage:
my_list = [1, 2, 3, 4, 5]
x = 3
printed_elements = safe_print_list(my_list, x)
print(f"Printed {printed_elements} elements from the list.")
'''
