def calculate_statistics(numbers):
    """
    Calculate sum, cumulative sum, average, minimum, and max of a list of numbers.
    Args:
       A list of numbers
    Returns:
            - 'sum': 
            - 'cumulative_sum':  cumulative sums.
            - 'average': average 
            - 'min': The minimum value 
            - 'max': The maximum value 
    """
    total_sum = 0
    cumulative_sum = []
    for num in numbers:
        total_sum += num
        cumulative_sum.append(total_sum)
    
    average = total_sum / len(numbers) if numbers else 0
    min_value = min(numbers) if numbers else None
    max_value = max(numbers) if numbers else None

    return {
        'sum': total_sum,
        'cumulative_sum': cumulative_sum,
        'average': average,
        'min': min_value,
        'max': max_value
    }

# Example
numbers = [5, 3, 8, 2, 10]
result = calculate_statistics(numbers)
print(result)

