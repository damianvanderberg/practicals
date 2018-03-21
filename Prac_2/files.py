
output_file = open("name.txt", "w")         # opens file location and write the file
user_name = (input("What is your name"))    # input
print(user_name, file=output_file)           # wheres the input going
output_file.close()



input_file = open("name.txt", "r")             # open file and read it
name = input_file.read().strip()               #read file and take out breaks whitespace
print("Your name is", name)                    #input name
input_file.close()





input_file = open("numbers.txt", "r")
number1 = int(input_file.readline().strip())
number2 = int(input_file.readline().strip())
print(number1 + number2)
input_file.close()



