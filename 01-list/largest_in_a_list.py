number_of_items = int(input('Please enter how many numbers you would like to enter: '))


myList = []

for i in range(number_of_items):
    myNumber = int(input(f'Enter a number {i+1}: '))
    myList.append(myNumber)

largest = myList[0]

for item in myList:
    if (item > largest):
        largest = item

print(f'The largest number is {largest}')
