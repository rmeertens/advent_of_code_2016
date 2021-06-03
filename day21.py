
import re


def swap_pos(input_str,posx,posy):
    """

    >>> swap_pos('hallo',0,1)
    'ahllo'
    >>> swap_pos('abcde',4,0)
    'ebcda'

    :param input_str:
    :param posx:
    :param posy:
    :return:
    """
    #temp = input_str[posx]
    #input_str[posx] = input_str[posy]
    #input_str[posy] = temp
    if posx > posy:
        posx,posy = posy,posx
    return input_str[:posx]+input_str[posy]+input_str[posx+1:posy]+input_str[posx]+input_str[posy+1:]


def swap_letter(input_str,letterx,lettery):
    """
    >>> swap_letter('hallo','a','l')
    'hlaao'
    >>> swap_letter('ebcda','d','b')
    'edcba'
    """
    input_str = input_str.replace(letterx,"@")
    input_str = input_str.replace(lettery,letterx)
    input_str = input_str.replace("@",lettery)
    return input_str

def reverse_positions(input_str,start,end):
    '''
    >>> reverse_positions('hallo',1,3)
    'hllao'
    >>> reverse_positions('edcba',0,4)
    'abcde'
    '''

    return input_str[:start] + ''.join(reversed(input_str[start:end+1])) + input_str[end+1:]

def rotate(input_str,amount):
    '''
    amount positive means rotate right
    >>> rotate('abcde',-1)
    'bcdea'
    >>> rotate('abdec',2)
    'ecabd'
    >>> rotate('ecabd',6)
    'decab'

    :param input_str:
    :param amount:
    :return:
    '''
    if amount == 0:
        return input_str
    if amount > 0:
        return rotate(input_str[-1]+input_str[:-1],amount-1)
    else:
        return rotate(input_str[1:]+input_str[0],amount+1)

def move_positions(input_str,posx,posy):
    '''
    >>> move_positions('bcdea',1,4)
    'bdeac'
    >>> move_positions('bdeac',3,0)
    'abdec'
    '''
    if posx > posy:
        return input_str[:posy] + input_str[posx] + input_str[posy:posx] +  input_str[posx + 1:]
    else:
        return input_str[:posx]+input_str[posx+1:posy+1]+input_str[posx]+input_str[posy+1:]



def rotate_based_on_position_of_letter(input_str,character):
    '''
    >>> rotate_based_on_position_of_letter('abdec','b')
    'ecabd'
    >>> rotate_based_on_position_of_letter('ecabd','d')
    'decab'

    :param input_str:
    :param character:
    :return:
    '''
    location_character = input_str.find(character)
    if location_character >= 4:
        location_character+=1
    location_character +=1

    return rotate(input_str,location_character)

def reverse_rotate_based_on_position_of_letter(input_str,character):

    '''
    >>> reverse_rotate_based_on_position_of_letter('decab','d')
    'ecabd'
    >>> reverse_rotate_based_on_position_of_letter('ecabd','b')
    'abdec'
    '''

    def rotate_based_on_position_of_letter(input_str, character):

        location_character = input_str.find(character)
        if location_character >= 4:
            location_character += 1
        location_character += 1

        return rotate(input_str, location_character)
    test = str(input_str)
    for i in range(10):
        test = rotate(test,-1)
        if rotate_based_on_position_of_letter(test,character) == input_str:
            return test
      #  print(test + " leads to " + rotate_based_on_position_of_letter(test,character))
    return 'abdec'


def reverse_interpret_single_command(line,start):

    swapdigitpattern = re.compile("^swap position (\d) with position (\d)$")
    swapletterpattern = re.compile("^swap letter (.) with letter (.)$")
    reversepattern = re.compile("^reverse positions (\d) through (\d)$")
    rotate_letterpattern = re.compile("^rotate based on position of letter (.)$")
    rotate_left_pattern = re.compile("^rotate left (\d) step.*$")
    rotate_right_pattern = re.compile("^rotate right (\d) step.*$")
    move_position_pattern = re.compile("^move position (\d) to position (\d)$")
    if swapdigitpattern.search(line):
        posx,posy = int(swapdigitpattern.search(line).group(1)),int(swapdigitpattern.search(line).group(2))
        start = swap_pos(start,posx,posy)
    elif swapletterpattern.search(line):
        posx,posy = swapletterpattern.search(line).group(1),swapletterpattern.search(line).group(2)
        start = swap_letter(start,posx,posy)
    elif reversepattern.search(line):
        posx,posy = int(reversepattern.search(line).group(1)),int(reversepattern.search(line).group(2))
        start = reverse_positions(start,posx,posy)
    elif rotate_letterpattern.search(line):
        posx= rotate_letterpattern.search(line).group(1)
        start = reverse_rotate_based_on_position_of_letter(start, posx)
    elif rotate_left_pattern.search(line):
        posx = int(rotate_left_pattern.search(line).group(1))
        start = rotate(start, 1*posx)
    elif rotate_right_pattern.search(line):
        posx = int(rotate_right_pattern.search(line).group(1))
        start = rotate(start, -1*posx)
    elif move_position_pattern.search(line):
        posx,posy = int(move_position_pattern.search(line).group(1)),int(move_position_pattern.search(line).group(2))
        start = move_positions(start,posy,posx)
    else:
        raise Exception(line)

    return start


def interpret_single_command(line,start):

    swapdigitpattern = re.compile("^swap position (\d) with position (\d)$")
    swapletterpattern = re.compile("^swap letter (.) with letter (.)$")
    reversepattern = re.compile("^reverse positions (\d) through (\d)$")
    rotate_letterpattern = re.compile("^rotate based on position of letter (.)$")
    rotate_left_pattern = re.compile("^rotate left (\d) step.*$")
    rotate_right_pattern = re.compile("^rotate right (\d) step.*$")
    move_position_pattern = re.compile("^move position (\d) to position (\d)$")
    if swapdigitpattern.search(line):
        posx,posy = int(swapdigitpattern.search(line).group(1)),int(swapdigitpattern.search(line).group(2))
        start = swap_pos(start,posx,posy)
    elif swapletterpattern.search(line):
        posx,posy = swapletterpattern.search(line).group(1),swapletterpattern.search(line).group(2)
        start = swap_letter(start,posx,posy)
    elif reversepattern.search(line):
        posx,posy = int(reversepattern.search(line).group(1)),int(reversepattern.search(line).group(2))
        start = reverse_positions(start,posx,posy)
    elif rotate_letterpattern.search(line):
        posx= rotate_letterpattern.search(line).group(1)
        start = rotate_based_on_position_of_letter(start, posx)
    elif rotate_left_pattern.search(line):
        posx = int(rotate_left_pattern.search(line).group(1))
        start = rotate(start, -1*posx)
    elif rotate_right_pattern.search(line):
        posx = int(rotate_right_pattern.search(line).group(1))
        start = rotate(start, posx)
    elif move_position_pattern.search(line):
        posx,posy = int(move_position_pattern.search(line).group(1)),int(move_position_pattern.search(line).group(2))
        start = move_positions(start,posx,posy)
    else:
        raise Exception(line)

    return start


def interpret_input(name_input,start):
    '''
    >>> interpret_input('testinput.txt','abcde')
    'decab'

    :param name_input:
    :param start:
    :return:
    '''
    f = open(name_input)
    for line in f:

        start = interpret_single_command(line,start)
       # print("After command: " + line + " : " + start)

    return start

def reverse_interpret_input(name_input,start):
    '''
    >>> reverse_interpret_input('testinput.txt','decab')
    'abcde'

    :param name_input:
    :param start:
    :return:
    '''
    f = open(name_input)
    lines = [l for l in f]
    lines=lines[::-1]
    for line in lines:
        start = reverse_interpret_single_command(line,start)
    #    print("After command: " + line + " : " + start)
    return start
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doing this")
    print(reverse_interpret_input('input.txt','fbgdceah'))