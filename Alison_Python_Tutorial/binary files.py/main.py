import pickle


# phonebook = {
#     'a': '1',
#     'b': '2',
#     'c': '3'
# }


#dump data... write in the phonebook
# with open('binary files/phone book.txt', 'wb') as bin:#we are also creating a new file in doing soo
#     pickle.dump(phonebook, bin)


#load data... read data from the phone book
with open('binary files/phone book.txt', 'rb') as bin:
    data = pickle.load(bin)
    print(data)