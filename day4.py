import string

in_f = open('in.txt')

sum_ids = 0

for line in in_f:
    checksum_loc = line.find("[")
    checksum = line[checksum_loc+1:-2]
    line_short = line[:checksum_loc]
    id_loc = line_short[::-1].find("-")
    line_shortest = line_short[:-id_loc-1]

    id = int(line_short[-id_loc::])
    character_frequency = {}
    for character in line_shortest:
        if character in string.ascii_lowercase:
            if not character in character_frequency:
                character_frequency[character] = 0
            character_frequency[character]+=1
    freq_char = []
    for k in character_frequency.keys():
        freq_char.append((10000000000-character_frequency[k],k))
    freq_char.sort()

    check_correct = True

    for idx,check_char in enumerate(checksum):

        if not check_char == freq_char[idx][1]:
            check_correct = False
    if check_correct:
        sum_ids+=id
        # decrypt time!
        shift = id%26
        new_string = ""
        for character in line_shortest:
            if character == "-":
                new_string+=" "
            else:
                new_char = ord(character) - ord('a')
                new_char += shift
                new_char %= 26
                new_char += ord('a')
                new_string += chr(new_char)
        print(new_string)
        print(id)
print(sum_ids)


for line in in_f:
    checksum_loc = line.find("[")
    checksum = line[checksum_loc+1:-2]
    line_short = line[:checksum_loc]
    id_loc = line_short[::-1].find("-")
    line_shortest = line_short[:-id_loc-1]

    id = int(line_short[-id_loc::])

    "qzmt - zixmtkozy - ivhz343"