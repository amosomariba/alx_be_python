# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks (*) side by side
    for col in range(size):
        print("*", end="")
    # Print a newline character to move to the next row
    print()
    # Increment row counter
    row += 1
