def update_board(array, position, sign):
    if(type(array[position]) != type("X")):
        array[position] = sign
        return array
    else:
        return array
