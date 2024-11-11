# Recursive Fibonacci Function to print the sequence up to n elements
def fibonacci(n, sequence=None):
    # Initialize the sequence on the first call
    if sequence is None:
        sequence = [0, 1]  # Starting sequence [0, 1]

    # Base case: stop when the sequence has n numbers
    if len(sequence) == n:
        return sequence  # Return the sequence when it has n numbers
    
    # Recursive case: calculate the next Fibonacci number and append to the sequence
    next_number = sequence[-1] + sequence[-2]
    sequence.append(next_number)
    
    # Recursively call for the next number
    return fibonacci(n, sequence)

