def linear_search(arr, x):
  """Performs a linear search on an array to find a given element.

  Args:
    arr: The array to search.
    x: The element to search for.

  Returns:
    The index of the element in the array if found, otherwise -1.
  """

  n = len(arr)
  for i in range(n):
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
