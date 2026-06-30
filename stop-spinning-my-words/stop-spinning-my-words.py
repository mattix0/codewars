'''
take all words from sentence
check if the length is greater than 4
    if true take the word and reverse it to a new string / array

return the array
'''

def spin_words(sentence):
    sentence_arr = sentence.split()
    sentence_string = ''

    for word in sentence_arr:
        if len(word) > 4:
            sentence_string += word[::-1] + ' '
        else:
            sentence_string += word + ' '

    sentence_string = sentence_string.strip()
    return sentence_string    


##Tests
spin_words("Hey fellow warriors"), "Hey wollef sroirraw"
spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes"