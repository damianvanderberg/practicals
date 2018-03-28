# take 5 numbers- put them in a list - call the start, end, biggest, smallest and

numbers = []

for i in range(5):
    number = int(input("enter numbers: "))
    numbers.append(number)

    print(numbers)

# works

# now need to print min, max, first, last and average

print("the minimum number is: ", min(numbers))
print("the maximum number is: ", max(numbers))
print("The first number is: ", numbers[0])
print("The last number is: ", numbers[-1])
# average = sum numbers / amount(len) numbers
print("The average number is: ", sum(numbers) / len(numbers))

# question - if i wanted to only print after the 5 numbers have been inputted? (indents) :)
