def sum_evens(file_name):
    '''
    >>> sum_evens('numbers_1.txt')
    '164 12 0 '
    >>> sum_evens('numbers_2.txt')
    '7654 5360 1569200 46574 7635754 0 9859896 '
    '''
    lines = open(file_name).read().split()
    out = ""
    for line in lines:
        total = 0
        for number in line.split(","):
            if(int(number) % 2 == 0):
                total += int(number)

        out += str(total) + " "
    return out


def print_words_longer_than(file_name, x):
    '''
    >>> print_words_longer_than('words_1.txt', 5)
    Line 1: apricot nectarine rockmelon
    Line 2: parsnip turnip pumpkin carrot
    Line 3: oregano rosemary
    >>> print_words_longer_than('words_2.txt', 7)
    Line 1: elephant
    Line 2: crocodile alligator
    Line 3: blackbird
    '''
    lines = open(file_name).read().split()
    for i, line in enumerate(lines):
        print("Line " + str(i + 1) + ":", end="")
        for word in line.split(","):
            if(len(word) > x):
                print(word + " ", end="")
            
        print()


def seating_plan_opt1(num_rows, num_seats):
    '''
    >>> seating_plan_opt1(4,6)== open('school_play_simple.txt').read()
    True
    >>> seating_plan_opt1(15,15)== open('opera_simple.txt').read()
    True
    '''
    out = ""
    for i in range(num_rows):
        if(j == 9 or j == 15):
            num_rows += 1
            continue
        for j in range(num_seats):
            if(j == 13):
                num_seats += 1
                continue
            out += chr(i + 65) + str(j + 1) + " "
        
        if(i < num_rows - 1):
            out += "\n"
    return out


def seating_plan_simple(num_rows, num_seats):
    '''
    >>> seating_plan_simple(4,6)== open('school_play_simple.txt').read()
    True
    >>> seating_plan_simple(15,15)== open('opera_simple.txt').read()
    True
    '''
    out = ""
    for i in range(num_rows):
        for j in range(num_seats):
            out += chr(i + 65) + str(j + 1) + " "
        
        if(i < num_rows - 1):
            out += "\n"
    return out

def to_oct_nums(num_string):
    '''
    >>> to_oct_nums('100 23 44 32 6 17 ')
    '144 27 54 40 6 21 '
    >>> to_oct_nums('0 1 8 64 512 4096 ')
    '0 1 10 100 1000 10000 '
    '''
    in_nums = num_string.split()
    out = ""
    for num in in_nums:
        octal_num = ""
        while int(num) > 0:
            octal_num += str(int(num) % 8)
            num = int(num) // 8
        
        octal_num = octal_num [::-1]
        
        if(octal_num == ""):
            octal_num = "0"
        
        out += octal_num + " "
    
    return out


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
