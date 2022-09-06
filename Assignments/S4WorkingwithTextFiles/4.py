'''
Write a Python program to count the number of lines, words and characters in a text file. This is similar to the Linux
 `wc` command. Create a function if possible.
'''


def wc(filename):
    with open(filename) as f:
        lines = f.readlines()
        char_count = 0
        word_count = 0
        for line in lines:
            char_count += len(line)
            word_count += len(line.split(' '))

        print('Lines: ' + str(len(lines)))
        print('Words: ' + str(word_count))
        print('Characters: ' + str(char_count))


wc('sample_file.txt')