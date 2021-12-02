with open("numbers.txt", "r") as file:
    numbers = file.readlines()
    sum = 607
    greaterThan = 0
    group = []
    for i in range(len(numbers) - 2):

        group = numbers[int(i) : int(i + 3)]

        # convert group to integers
        group = [int(x) for x in group]

        # print(group)

        # print(len(group))

        tempSum = 0
        tempSum += group[0] + group[1] + group[2]

        if tempSum > sum:
            greaterThan += 1

        sum = tempSum

    print(greaterThan)
