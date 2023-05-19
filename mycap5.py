def fibonacci(n):
    fib_seq = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers

    # Generate Fibonacci numbers
    while len(fib_seq) < n:
        next_num = fib_seq[-1] + fib_seq[-2]  # Calculate the next number
        fib_seq.append(next_num)  # Add the next number to the sequence

    return fib_seq

# Prompt the user for input
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

# Generate Fibonacci sequence
fibonacci_seq = fibonacci(num_terms)

# Display the Fibonacci sequence
print("Fibonacci Sequence:")
for num in fibonacci_seq:
    print(num, end=" ")
