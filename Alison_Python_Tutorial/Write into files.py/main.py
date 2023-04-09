userInput = input('Enter your message that you wish to save: ')


"""#w denotes writes and write clears all existing data on data.txt
with open('Write into files\data.txt','w') as file:
    file.write(userInput)
    print("your text has been saved")"""


with open('Write into files\data.txt','a') as file:
    file.write(userInput + '\n')
    print("your text has been saved")