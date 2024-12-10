def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage with an empty list, now handled correctly
average = calculate_average([])
print(f"Average: {average}")

# Example with non-empty list
average2 = calculate_average([10,20,30])
print(f"Average: {average2}") 