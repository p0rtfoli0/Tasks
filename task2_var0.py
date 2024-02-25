def reversedStr(variable): 
    if len(variable) == 1:
        return variable
    return variable[-1] + reversedStr(variable[:-1])
