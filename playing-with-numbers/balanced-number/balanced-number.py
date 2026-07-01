balanced = 'Balanced'
not_balanced = 'Not Balanced'

def balanced_num(number):
    str_number = str(number)
    length = len(str_number)
    middle = length // 2
    left_sum = int()
    right_sum = int()
    
    # if number is between 0 and 99 it's always balanced since 0 will be on both sides
    if length < 3:
        return balanced
    
    if length % 2 == 0:
        left = str_number[:middle - 1]
        right = str_number[middle + 1:]

        for digit in left:
            left_sum += int(digit)

        for digit in right:
            right_sum += int(digit)
        
        if left_sum == right_sum:
            return balanced
        else:
            return not_balanced

    else:
        left = str_number[:middle]
        right = str_number[middle + 1:]

        for digit in left:
            left_sum += int(digit)

        for digit in right:
            right_sum += int(digit)

        if left_sum == right_sum:
            return balanced
        else:
            return not_balanced




## Tests
balanced_num(7)  , "Balanced"
balanced_num(959), "Balanced"
balanced_num(13) , "Balanced"
balanced_num(432), "Not Balanced"
balanced_num(424), "Balanced"
balanced_num(1024)    , "Not Balanced"
balanced_num(66545)   , "Not Balanced"
balanced_num(295591)  , "Not Balanced"
balanced_num(1230987) , "Not Balanced"
balanced_num(56239814), "Balanced"