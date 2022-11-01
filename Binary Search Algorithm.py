# a function that takes a list and target parameter
# multiple variables: middle, start, end, steps
# recursion or while loop
# increase the steps each time a split is done
# conditions to track target position

def binary_search(num_list, element):
    start = 0
    end = len(num_list)
    steps = 0

    while start <= end:
        print("Steps", steps, " : ", str(num_list[start: end + 1]))

        steps = steps + 1
        middle = (start + end) // 2

        if element == num_list[middle]:
            print(f"Found the target: {element}")
            return middle
        elif element < num_list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 6

binary_search(my_list, target)
