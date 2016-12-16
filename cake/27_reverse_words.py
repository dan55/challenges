'''
Problem:

Reverse the words in a sentence.


Thoughts:

First we reverse the entire string, and then we reverse each reversed word,

resulting in desired output. Be careful of the indexing. To re-reverse the final word,

we increment one passed the length of the string. 


Source:

https://www.interviewcake.com/question/python/reverse-words
'''

def reverse_string(string_as_list, start, end):
    while start < end:
        string_as_list[start], string_as_list[end] = string_as_list[end], string_as_list[start]

        start += 1
        end -= 1

    return string_as_list


def reverse_sentence(string):
    string_as_list = list(string)
    
    string_len = len(string_as_list)
    start = 0

    reversed_string = reverse_string(string_as_list, start, string_len - 1)

    for i in range(string_len + 1):
        if i == string_len or reversed_string[i] == ' ':
            reverse_string(reversed_string, start, i - 1)
            start = i + 1

    return ''.join(string_as_list)

def main():
    sentence = 'find you will pain only go you recordings security the into if'
    reversed_sentence = 'if into the security recordings you go only pain will you find'

    print reverse_sentence(sentence) == reversed_sentence

if __name__ == '__main__':
    main()