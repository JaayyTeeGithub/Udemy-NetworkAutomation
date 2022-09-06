'''
Write a Python script that reads the file in a dictionary.
The words in the file will be the dictionary keys and the length of each word the corresponding values.
'''

with open('american-english.txt') as file:
    word_dict = dict()
    words = file.read().splitlines()
    for word in words:
        word_dict[word] = str(len(word))

print(word_dict)

