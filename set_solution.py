# Your print statements may be in a different order

groceries = {"apples", "bananas", "oranges", "milk", "salad", "beef", "soup"}
add_to_groceries = {"oranges", "beef", "chicken", "pineapple"}

# Print the missing items from groceries
print("Missing food in add_to_groceries:", (set(groceries).difference(add_to_groceries)))
# Missing values in second list: {'salad', 'soup', 'milk', 'bananas', 'apples'}

# Print the additional groceries from add_to_groceries
print("Additional food to be added:", (set(add_to_groceries).difference(groceries)))
# Missing values in second list: {'chicken', 'pineapple'}

# Combine both sets of food into a new set
new_groceries = groceries.union(add_to_groceries)

# Print new grocery set
print(new_groceries)
# {'soup', 'apples', 'salad', 'oranges', 'beef', 'pineapple', 'milk', 'bananas', 'chicken'}

# Add "kiwi" and "butter" to new_groceries
new_groceries.add("kiwi")
new_groceries.add("butter")
print(new_groceries)
# {'beef', 'milk', 'oranges', 'butter', 'pineapple', 'kiwi', 'salad', 'chicken', 'bananas', 'apples', 'soup'}