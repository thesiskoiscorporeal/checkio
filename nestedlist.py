output = []

def flat_list(array):
    for i in array: 
        if type(i) == list: 
            flat_list(i) 
        else: 
            output.append(i) 
    return output


print (flat_list([1, [2, 2, 2], 4]))