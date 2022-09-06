'''
Consider the dictionary file from the previous challenge.

Write a Python script that finds the first 100 longest words in the file.
'''

with open('american-english.txt') as file:
    word_dict = dict()
    words = file.read().splitlines()
    for word in words:
        word_dict[word] = str(len(word))

print(word_dict)

sorted_dict = sorted(word_dict.items(), key=lambda x: x[1])
count = 0
for item in list(reversed(list(sorted_dict)))[0:100]:
    print(item)
