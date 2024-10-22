def fibonacci(n):
    """Generates a list of the first n Fibonacci numbers."""
    if type(n) != int or n <= 0: # if datatype of n not a integer or n less than equal to 0
        return "Input must be a positive integer."

    fib_sequence = [] # empty list

    a, b = 0, 1 # 2 fibpnacci numbers

    for x in range(n): # loop
        fib_sequence.append(a)  # Add the current number to the list
        a, b = b, a + b  # Move to the next Fibonacci numbers
    
    return fib_sequence

n = int(input()) 
print(fibonacci(n))
