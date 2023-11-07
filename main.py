numToAdd = input("How many numbers do you want to add: ")
sum =0
for x in range(int(numToAdd)):
    num = input("Add a single number you want to add: ")
    sum += int(num)
print(f'Sum is {sum}')