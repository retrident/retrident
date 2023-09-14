def main():
    # Initialize variables
    sum = 0
    evens = 0
    odds = 0
    # Continuously ask the user for input
    while True:
        # Prompt the user for a positive integer or -1 to exit
        num = int(input("Enter a positive integer (or -1 to exit): "))
        # Check if the user wants to exit
        if num == -1:
            break
        # Check if the number is positive
        if num > 0:
            # Update the sum
            sum += num
            # Check if the number is even
            if num % 2 == 0:
                evens += 1
            else:
                odds += 1
    # Print the final results
    print("Sum of the numbers:", sum)
    print("Count of even numbers:", evens)
    print("Count of odd numbers:", odds)

main()
