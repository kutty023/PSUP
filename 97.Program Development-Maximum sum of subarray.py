# Maximum sum of subarray

n = int(input())  # Read the number of elements in the array
numbers = list(map(int, input().split()))[:n]  # Read the array elements

def max_subarray_sum(nums):
    current_sum = nums[0]  # Initialize current sum with the first element
    max_sum = nums[0]  # Initialize max sum with the first element

    for i in range(1, len(nums)):  # Iterate from the second element to the end
        # Calculate the current sum as the maximum between the current element
        # and the sum of the current element and the previous sum
        current_sum = max(nums[i], current_sum + nums[i])
        # Update the max sum if the current sum is greater
        max_sum = max(max_sum, current_sum)

    return max_sum  # Return the maximum subarray sum

result = max_subarray_sum(numbers)  # Call the max_subarray_sum function

if result < 0:
    print(0)  # If the maximum subarray sum is negative, output 0
else:
    print(result)  # Otherwise, print the maximum subarray sum
