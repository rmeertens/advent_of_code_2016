# in_f = open('input.txt')
#
# count = 0
#
# def has_abba(input):
#   #  print("Checking")
#   #  print(input)
#     for i in range(len(input)-4):
#         substr = input[i:i+4]
#         if substr[0]==substr[3] and substr[1]==substr[2]:
#             print(input + " is good")
#             return True
#
# def get_has_negative_stuff(input):
#     if input.find("[") >= 0:
#         return has_abba(input[input.find("[")+1:input.find("]")]) or get_has_negative_stuff(input[input.find("]")+1::])
#     return False
# def get_has_positive_stuff(input):
#     if input.find("[") >= 0:
#         return has_abba(input[:input.find("[")]) or get_has_positive_stuff(input[input.find("]")+1::])
#
#     return has_abba(input)
# def get_is_TLS(input):
#     return get_has_positive_stuff(input) and not get_has_negative_stuff(input)
# for line in in_f:
#     if get_is_TLS(line):
#         count+=1
# print(count)
in_f = open('input.txt')

count = 0

def get_supernet_and_hypernet(line):
    chunks = []
    hypernet_chunks = []
    while True:
        if line.find("[") >= 0:
            chunks.append(line[:line.find("[")])
            hypernet_chunks.append(line[line.find("[") + 1:line.find("]")])
            line = line[line.find("]") + 1::]
        else:
            chunks.append(line)
            break
    return chunks,hypernet_chunks

for line in in_f:
    super,hyper = get_supernet_and_hypernet(line)
    print(str(len(super)) + " " + str(len(hyper)))
    found = False
    for sequence in super:
        if found:
            break
        for i in range(len(sequence)-2):
            if found:
                break
            if sequence[i] == sequence[i+2]:
                # ABA
                BAB = sequence[i+1]+sequence[i]+sequence[i+1]
                for hy in hyper:
                    if BAB in hy:
                        found = True
                        count+=1
                        break
print(count)


