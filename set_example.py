set_1 = {9,8,7,6,5,4,3,2,1}
set_2 = {9,7,6,5,4,2,6,1,0}

# Find if both sets have any common numbers
def common_number(set_1, set_2):
    if (set_1 & set_2):
        return True
    else:
        return False

print(common_number(set_1, set_2))
# True

# Print the numbers that are not in both sets  
print(set_1.symmetric_difference(set_2))
# {0, 3, 8}

# Print the numbers that are in both sets
print(set_1 & set_2)
# {1, 2, 4, 5, 6, 7, 9}