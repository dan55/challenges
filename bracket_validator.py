'''
Problem:

Determine whether every opening delimiter has a matching closing one.


Source:

https://www.interviewcake.com/question/python/bracket-validator

https://www.hackerrank.com/challenges/ctci-balanced-brackets
'''

def validate_brackets(string):
    stack = []

    for char in string:
        if char == '{': 
            stack.append('}')
        elif char == '[':
            stack.append(']')
        elif char == '(':
            stack.append(')')
        elif stack.pop() != char:
            return False

    return True


'''
Interview Cake has some pretty code for this one. Blind copy attempt.
'''

def validate_brackets_(string):
    openers_to_closers_map = {
        '{' : '}',
        '(' : ')',
        '[' : ']',
    }

    openers = openers_to_closers_map.keys()
    closers = openers_to_closers_map.items()
    stack = []

    for char in string:
        if char in openers:
            stack.append(openers_to_closers_map[char])
        else:
            try:
                if char != stack.pop():
                    return False
            except IndexError: 
                # unmatched closing character
                return False

    return True


if __name__ == '__main__':

    string = '{[()]}'
    print validate_brackets(string) == validate_brackets_(string) == True
    
    string = '{[(]}'
    print validate_brackets(string) == validate_brackets_(string) == False
    
    print validate_brackets_('}}}}') == False