'''
Problem: 

Is any permutaion of a string a palindrome? 


Source:

https://www.interviewcake.com/question/python/permutation-palindrome
'''

from collections import defaultdict

def is_any_permutation_a_palindrome(string):
    char_instances = defaultdict(int)

    for char in string:
        char_instances[char] += 1

    num_odds = 0

    for value in char_instances.values(): 
        if value % 2 != 0:
            num_odds += 1

            if num_odds > 1:
                return False

    return True

def is_any_permutation_a_palindrome_not_ugly(string):
    unmatched_chars = set()

    for char in string:
        if char in unmatched_chars:
            unmatched_chars.remove(char)
        else:
            unmatched_chars.add(char)

    return len(unmatched_chars) <= 1


def main():
    print is_any_permutation_a_palindrome('civic') == \
        is_any_permutation_a_palindrome_not_ugly('civic') == True
    
    print is_any_permutation_a_palindrome('ivicc') == \
        is_any_permutation_a_palindrome_not_ugly('ivicc') == True
    
    print is_any_permutation_a_palindrome('civil') == \
        is_any_permutation_a_palindrome_not_ugly('civil') == False
    
    print is_any_permutation_a_palindrome('livci') == \
        is_any_permutation_a_palindrome_not_ugly('livci') == False

if __name__ == '__main__':
    main()