# find en algoritme der kan udregne strong numbers produktværdi
    # eks 1! = 1*1 = 1 
    # eks 3! = 3*2*1 = 6
    # eks 6! = 6*5*4*3*2*1 = 720

# find summen af strong numbers (normale int tal) 
    # eks 1! + 4! + 5! = 1 + 24 + 120 = 145
    # så strong numbers 1! + 4! + 5! er 145 og hvis summen af dette er det samme så er det STRONG ellers NOT STRONG

def strong_num(number):
    total = 0

    for num in str(number):       
        factorial = 1

        for i in range (1, int(num) + 1):
            factorial *= i

        total += factorial

    return "STRONG!!!!" if total == number else "Not Strong !!"
        
## Tests
strong_num(1)    , "STRONG!!!!"
strong_num(2)    , "STRONG!!!!"
strong_num(145)  , "STRONG!!!!"
strong_num(40585), "STRONG!!!!"
strong_num(7)      , "Not Strong !!"
strong_num(93)     , "Not Strong !!"
strong_num(185)    , "Not Strong !!"
strong_num(2999999), "Not Strong !!"