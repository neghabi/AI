import matplotlib.pyplot as plt
import time

def linear_search(arr, x):
    """Performs a linear search on an array to find a given element with animation.

    Args:
        arr: The array to search.
        x: The element to search for.

    Returns:
        The index of the element in the array if found, otherwise -1.
    """

    n = len(arr)
    for i in range(n):
        plt.clf()  # Clear the previous plot
        plt.bar(range(n), arr, color='blue')
        plt.title(f"Linear Search: Iteration {i+1}")
        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.annotate(f"Comparing: {arr[i]}", xy=(i, arr[i]), xytext=(10, 10), textcoords="offset points", arrowprops=dict(arrowstyle="->"))
        plt.show(block=False)  # Show the plot without blocking
        time.sleep(1)  # Pause for 1 second

        if arr[i] == x:
            return i
    return -1

# Example usage:
arr = [10, 20, 30, 40, 50]
x = 30
result = linear_search(arr, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
