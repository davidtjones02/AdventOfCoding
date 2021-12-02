# open numbers.txt
# read each line

with open("numbers.txt", "r") as file:
    numbers = file.readlines()
    sum = 0
     # compare the previous line with the current line
    for i in range(len(numbers)):
        # dont compare the first line
        if i > 0:
            if int(numbers[i]) > int(numbers[i-1]):
                sum += 1
    print(sum)