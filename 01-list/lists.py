# Creating a list
shopping_list = ["Chocolates", "Chips", "Coke"]

# Printing a list
print(shopping_list)

# Access the item in a list
print(shopping_list[1])

# Access items from end of the list
print(shopping_list[-1])

# Changing item in the list
shopping_list[2] = "Juice"
print(shopping_list)

# Loop through the list
for item in shopping_list:
    print(item)

# How to find length of the list
print(len(shopping_list))

# Add element in the list
shopping_list.append('Lolipop')
print(shopping_list)

# Remove an item from the list
shopping_list.remove('Lolipop')
print(shopping_list)

# Delete an item at a particular position
del shopping_list[2]
print(shopping_list)

# Clearing the list
shopping_list.clear()
print(shopping_list)

# Delete the list
#del shopping_list
#print(shopping_list)

# Copy one list to another
numbers = [1, 2, 3, 4]
copy_of_numbers = numbers.copy()
print(copy_of_numbers)
