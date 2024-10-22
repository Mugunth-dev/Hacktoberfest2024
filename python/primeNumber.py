# hacktoberfest_challenge.py
# A simple Python script that contains a few bugs. Feel free to fix them and improve the code!

def is_prime(number):
    """Returns True if the number is prime, else False."""
    if number <= 1:
        return False  # Fixed: 1 is not prime!
    for i in range(2, int(number**0.5) + 1):  # Fixed: Optimized range for prime check
        if number % i == 0:
            return False
    return True

def sum_of_primes(limit):
    """Returns the sum of all prime numbers up to the given limit."""
    total = 0
    for num in range(2, limit):  # Fixed: Start from 2, since 1 is not prime
        if is_prime(num):
            total += num
    return total

def get_integer_input(prompt):
    """Helper function to get validated integer input from the user."""
    while True:
        try:
            return int(input(prompt))  # Attempts to convert input to an integer
        except ValueError:  # Catches non-integer inputs
            print("Invalid input. Please enter an integer.")

def main():
    """Main function to demonstrate the prime number functions."""
    number = get_integer_input("Enter a number: ")
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
    
    limit = get_integer_input("Enter the upper limit for sum of primes: ")
    print(f"The sum of primes up to {limit} is: {sum_of_primes(limit)}")

if __name__ == "__main__":
    main()
