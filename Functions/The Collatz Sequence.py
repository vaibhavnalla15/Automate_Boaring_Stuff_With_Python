""" The Collatz Sequence Rule
For any positive integer n:
If n is even → next number = n // 2
If n is odd → next number = 3 * n + 1
Repeat this process until n = 1.
eg. 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1. """

try:
    # TODO 6. Handle invalid (non-integer) input with a try-except block.
    # TODO 1. Ask the user to enter a number (input() + int() conversion).
    num = int(input("Enter a number:- "))
    # TODO 2. Use a while loop that runs until the number becomes 1.
    while num > 1:
        # TODO 3. Inside the loop:
        # TODO :- If the number is even, divide it by 2 (n //= 2).
        if num % 2 == 0:
            num //= 2

        # TODO :- Else, multiply by 3 and add 1 (n = 3 * n + 1).
        else:
            num = 3 * num + 1

        # TODO 4. Print each new value of n
        print(num, end=" ")

        # TODO 5. End when n == 1, and print a completion message.
        if num == 1:
            print("\nCollatz Sequence Completed")

except ValueError:
    print("Enter a Integer")


