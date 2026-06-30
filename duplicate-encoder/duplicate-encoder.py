'''
For each char check if multiple occurences appear in the 'word' string.
If char is only present once then add '(' else ')'
'''

def duplicate_encode(word):
    new_string = ''
    word = word.lower()

    for c in word:
        if word.count(c) > 1:
            new_string += ')'
        else:
            new_string += '('
            
    return new_string


## Tests
duplicate_encode("din"),"((("
duplicate_encode("recede"),"()()()"
duplicate_encode("Success"),")())())","should ignore case"
duplicate_encode("(( @"),"))(("