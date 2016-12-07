'''
Problem:

Reverse a string in place.


Source:

https://www.interviewcake.com/question/python/reverse-string-in-place
'''

def reverse_string(s):
    s_as_arr = list(s)

    i, j = 0, len(s) - 1
    while i < j:
        s_as_arr[i], s_as_arr[j] = s_as_arr[j], s_as_arr[i]

        i += 1
        j -= 1

    return ''.join(s_as_arr) 


if __name__ == '__main__':
    
    word = 'mississippi'

    str_reversed = reverse_string(word)

    word = list('mississippi')
    word.reverse()
    word = ''.join(word)

    print str_reversed == ''.join(word)