def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers) 
    return average

# Example usage (will cause ZeroDivisionError):
my_numbers = []
average = calculate_average(my_numbers)