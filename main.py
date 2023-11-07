def add_numbers():
    numToAdd = input("How many numbers do you want to add: ")
    total_sum = 0
    for x in range(int(numToAdd)):
        num = input("Add a single number you want to add: ")
        total_sum += int(num)
    return total_sum

if __name__ == "__main__":
    sum_result = add_numbers()
    print(f'Sum is {sum_result}')
