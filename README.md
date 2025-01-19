# ZeroDivisionError in Python Average Calculation
This example demonstrates a common error in Python: a ZeroDivisionError that occurs when dividing by zero. The `calculate_average` function attempts to compute the average of a list of numbers. However, if the list is empty, it leads to division by zero.

The solution involves checking if the input list is empty and handling this case appropriately, typically by returning 0 or raising a more informative exception. 