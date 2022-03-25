

def toggle(inp):
    """
    >>> toggle("inc a")
    'dec a'
    >>> toggle("tgl a")
    'inc a'

    :param inp:
    :return:
    """
    if "inc" in inp:
        return inp.replace("inc","dec")
    elif len(inp.split()) == 2:
        to_rep, _ = inp.split()
        return inp.replace(to_rep,"inc")
    elif "jnz" in inp:
        return inp.replace("jnz","cpy")
    elif len(inp.split()) == 3:
        to_rep, _, _ = inp.split()
        return inp.replace(to_rep,"jnz")

def easter_thing(inputs,init_a):
    """
    >>> easter_thing(["inc a"])
    1
    >>> easter_thing(["cpy 2 a","tgl a","tgl a","tgl a","cpy 1 a","dec a","dec a"])
    3
    >>> easter_thing(["cpy 2 a"])
    2
    >>> easter_thing(["cpy 2 a","tgl a","tgl a","tgl a","cpy 1 a"])
    3

    :param inputs:
    :return:
    """
    index_inp = 0
    registers = {"a":init_a,"b":0,"c":0,"d":0}
    total_steps = 0
    while index_inp < len(inputs):
        total_steps +=1

       #  if total_steps%1000==1:
       #      print(registers)
       #      print(inputs)
       #      print(index_inp)
       #      print("now executing " + inputs[index_inp])
       # # f = input("waiting")

        if "inc" in inputs[index_inp]:
            # inc
            _, register_name = inputs[index_inp].split()
            registers[register_name] +=1
            index_inp += 1
        elif "dec" in inputs[index_inp]:
            # dec
            _, register_name = inputs[index_inp].split()
            registers[register_name] -= 1
            index_inp += 1
        elif "cpy" in inputs[index_inp]:
            # copy
            _, reg1, reg2 = inputs[index_inp].split()
            if reg1 in registers:
                registers[reg2] = registers[reg1]
            elif reg2 in registers:
                registers[reg2] = int(reg1)
            else:
                pass
            index_inp += 1
        elif "jnz" in inputs[index_inp]:
            # jump not zero
            #print("doing jump not zero")
            _, reg, steps = inputs[index_inp].split()

            if reg in registers:
                if registers[reg] != 0:
                    index_inp += int(steps)
                else:
                    index_inp +=1

            elif steps not in registers:

                if int(reg) != 0:
                    index_inp += int(steps)
                else:
                    index_inp+=1
            else:
                if int(reg) !=0:
                    index_inp += registers[steps]
          #  print("end of jump not zero")
        elif "tgl" in inputs[index_inp]:
            _, location = inputs[index_inp].split()
            if location in registers:
                to_toggle_loc = index_inp + registers[location]
            else:
                to_toggle_loc = index_inp + int(location)
           # print(to_toggle_loc)
            to_toggle_loc = int(to_toggle_loc)
          #  print("WHooo")
            if to_toggle_loc < len(inputs):
                inputs[to_toggle_loc] = toggle(inputs[to_toggle_loc])
            index_inp +=1
        elif "out" in inputs[index_inp]:
            _,location = inputs[index_inp].split()
            if location in registers:
                yield int(registers[location])
            else:
                yield int(location)
            index_inp +=1

        else:
            raise Exception("No command found with name " + inputs[index_inp])
    #print("value left")
    #print(registers["a"])
    #return registers["a"]

if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        filename='awesomelog.log',
                        filemode='w')
    logging.in
    logging.debug('A debug message')
    logging.info('Some information')
    logging.warning('A shot across the bows')

    #output = easter_thing(["cpy 2 a","tgl a","tgl a","tgl a","cpy 1 a","dec a","dec a"])
    #print(output)

    instructions = [l[:-1] for l in open("input.txt")]
    expected = 0
    import itertools
    for a_start in itertools.count(26000):

        for output in easter_thing(instructions,a_start):
            print(output)
            if output != expected:
                print("nooo: " + str(a_start))
                break
            if expected == 1:
                expected = 0
            else:
                expected = 1
            #print(output)

    #print(easter_thing(instructions))