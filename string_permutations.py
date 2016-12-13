'''
Problem:

Recursively generate all permutations of a string.


Thoughts:

Another nice explanation from Interview Cake. We insert a single character 

(the last) in each position for every permutation of the characters that 

preceed it. For a two-character string, we insert the last character before

and after the first character. For a three-character string, we insert the

last character before, in the middle of, and at the end of each permutation 

we obtained from the two-character string. And so on and so forth.


Note: While long, descriptive variable names are useful in understanding the program, 

they can be a little tricky when debugging. Be careful not to confuse mixup 

plural and singular variables when they coexist.


Source: 

https://www.interviewcake.com/question/python/recursive-string-permutations
'''

def get_permutations(string):
    
    # base case
    if len(string) == 1:
        return [string]

    head_chars = string[:-1]
    tail_char = string[-1]

    permutations_of_head = get_permutations(head_chars)

    permutations = []
    
    for permutation_of_head in permutations_of_head:
        for position in range(len(permutations_of_head) + 1):        
            full_permutation = permutation_of_head[:position] + tail_char + permutation_of_head[position:]
  
            permutations.append(full_permutation)

    return permutations


def main():
    import itertools

    string = 'abc'
    
    print  set(get_permutations(string)) == set([''.join(perm) for perm in get_permutations(string)])

if __name__ == '__main__':
    main()